import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import threading
from PIL import Image, ImageTk, ImageFilter, ImageDraw
import colorsys

class ModernButton(tk.Canvas):
    def __init__(self, parent, text, command=None, width=120, height=40, color="#2196F3"):
        super().__init__(parent, width=width, height=height, highlightthickness=0)
        self.configure(background='#f0f0f0')  # Set default background
        self.color = color
        self.command = command
        self.text = text
        self.width = width
        self.height = height
        
        # Create rounded rectangle button
        self.normal_bg = self._create_button_image(color)
        self.hover_bg = self._create_button_image(self._adjust_color(color, 1.1))
        
        self.bg_image = self.create_image(width/2, height/2, image=self.normal_bg)
        self.text_item = self.create_text(width/2, height/2, text=text, fill="white", font=("Segoe UI", 10, "bold"))
        
        self.bind("<Enter>", self._on_enter)
        self.bind("<Leave>", self._on_leave)
        self.bind("<Button-1>", self._on_click)
        
    def _create_button_image(self, color):
        img = Image.new('RGBA', (self.width, self.height), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        draw.rounded_rectangle([2, 2, self.width-2, self.height-2], radius=self.height//2, fill=color)
        return ImageTk.PhotoImage(img)
    
    def _adjust_color(self, color, factor):
        color = color.lstrip('#')
        r, g, b = tuple(int(color[i:i+2], 16) for i in (0, 2, 4))
        h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)
        v = min(1.0, v * factor)
        r, g, b = colorsys.hsv_to_rgb(h, s, v)
        return f"#{int(r*255):02x}{int(g*255):02x}{int(b*255):02x}"
    
    def _on_enter(self, e):
        self.itemconfig(self.bg_image, image=self.hover_bg)
        
    def _on_leave(self, e):
        self.itemconfig(self.bg_image, image=self.normal_bg)
        
    def _on_click(self, e):
        if self.command:
            self.command()

class ModernFileSplitter:
    def __init__(self, root):
        self.root = root
        self.root.title("Modern File Splitter")
        self.root.geometry("800x600")
        
        # Variables
        self.input_file = tk.StringVar()
        self.output_dir = tk.StringVar()
        self.chunk_size = tk.IntVar(value=1)
        self.num_workers = tk.IntVar(value=4)
        self.is_running = False
        
        # Configure style
        self.style = ttk.Style()
        self.style.configure("TFrame", background="#f0f0f0")
        self.style.configure("TLabel", background="#f0f0f0")
        self.style.configure("TLabelframe", background="#f0f0f0")
        self.style.configure("TLabelframe.Label", background="#f0f0f0")
        
        # Create main frame
        self.main_frame = ttk.Frame(root, style="TFrame")
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        self.create_gui()
        
    def create_gui(self):
        # Title
        title_frame = ttk.Frame(self.main_frame, style="TFrame")
        title_frame.pack(fill=tk.X, pady=(0, 20))
        
        title_label = ttk.Label(
            title_frame, 
            text="File Splitter",
            font=("Segoe UI", 24, "bold"),
            foreground="#2196F3",
            style="TLabel"
        )
        title_label.pack()
        
        # Input file frame
        file_frame = ttk.LabelFrame(self.main_frame, text="File Selection", padding="10")
        file_frame.pack(fill=tk.X, pady=(0, 20))
        
        # Input file
        ttk.Label(file_frame, text="Input File:").pack(anchor='w')
        input_frame = ttk.Frame(file_frame)
        input_frame.pack(fill=tk.X, pady=5)
        
        ttk.Entry(input_frame, textvariable=self.input_file).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        ModernButton(input_frame, "Browse", self.browse_input, width=100).pack(side=tk.RIGHT)
        
        # Output directory
        ttk.Label(file_frame, text="Output Directory:").pack(anchor='w', pady=(10, 0))
        output_frame = ttk.Frame(file_frame)
        output_frame.pack(fill=tk.X, pady=5)
        
        ttk.Entry(output_frame, textvariable=self.output_dir).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        ModernButton(output_frame, "Browse", self.browse_output, width=100).pack(side=tk.RIGHT)
        
        # Settings frame
        settings_frame = ttk.LabelFrame(self.main_frame, text="Settings", padding="10")
        settings_frame.pack(fill=tk.X, pady=(0, 20))
        
        # Chunk size
        size_frame = ttk.Frame(settings_frame)
        size_frame.pack(fill=tk.X, pady=5)
        ttk.Label(size_frame, text="Chunk Size (GB):").pack(side=tk.LEFT)
        ttk.Spinbox(size_frame, from_=1, to=100, textvariable=self.chunk_size, width=10).pack(side=tk.LEFT, padx=10)
        
        # Workers
        workers_frame = ttk.Frame(settings_frame)
        workers_frame.pack(fill=tk.X, pady=5)
        ttk.Label(workers_frame, text="Number of Workers:").pack(side=tk.LEFT)
        ttk.Spinbox(workers_frame, from_=1, to=16, textvariable=self.num_workers, width=10).pack(side=tk.LEFT, padx=10)
        
        # Progress frame
        progress_frame = ttk.LabelFrame(self.main_frame, text="Progress", padding="10")
        progress_frame.pack(fill=tk.X, pady=(0, 20))
        
        self.progress = ttk.Progressbar(progress_frame, mode='determinate')
        self.progress.pack(fill=tk.X)
        
        self.status_var = tk.StringVar(value="Ready")
        status_label = ttk.Label(progress_frame, textvariable=self.status_var)
        status_label.pack(pady=5)
        
        # Start button
        button_frame = ttk.Frame(self.main_frame)
        button_frame.pack(fill=tk.X)
        
        self.start_button = ModernButton(
            button_frame, 
            "Start Splitting",
            self.start_splitting,
            width=150
        )
        self.start_button.pack(pady=1)
    
    def browse_input(self):
        filename = filedialog.askopenfilename(title="Select Input File")
        if filename:
            self.input_file.set(filename)
            
    def browse_output(self):
        dirname = filedialog.askdirectory(title="Select Output Directory")
        if dirname:
            self.output_dir.set(dirname)
    
    def start_splitting(self):
        if not self.is_running:
            if not self.input_file.get() or not self.output_dir.get():
                messagebox.showerror("Error", "Please select input file and output directory")
                return
                
            self.is_running = True
            self.start_button.configure(state='disabled')
            self.progress['value'] = 0
            
            thread = threading.Thread(target=self.split_file)
            thread.daemon = True
            thread.start()
    
    def split_file(self):
        try:
            input_file = self.input_file.get()
            output_dir = self.output_dir.get()
            chunk_size_bytes = self.chunk_size.get() * 1024 * 1024 * 1024  # Convert GB to bytes
            
            # Get total file size
            total_size = os.path.getsize(input_file)
            num_chunks = (total_size + chunk_size_bytes - 1) // chunk_size_bytes
            
            # Open the input file
            with open(input_file, 'rb') as f:
                for chunk_num in range(num_chunks):
                    # Calculate progress
                    progress = (chunk_num / num_chunks) * 100
                    self.progress['value'] = progress
                    self.status_var.set(f"Processing chunk {chunk_num + 1} of {num_chunks}")
                    self.root.update_idletasks()
                    
                    # Read chunk
                    chunk_data = f.read(chunk_size_bytes)
                    
                    # Create output filename
                    base_name = os.path.basename(input_file)
                    name, ext = os.path.splitext(base_name)
                    output_file = os.path.join(
                        output_dir,
                        f"{name}_part{chunk_num + 1:03d}{ext}"
                    )
                    
                    # Write chunk to file
                    with open(output_file, 'wb') as chunk_file:
                        chunk_file.write(chunk_data)
            
            self.progress['value'] = 100
            self.status_var.set("File splitting completed!")
            messagebox.showinfo("Success", "File splitting completed successfully!")
            
        except Exception as e:
            self.status_var.set(f"Error: {str(e)}")
            messagebox.showerror("Error", str(e))
            
        finally:
            self.is_running = False
            self.start_button.configure(state='normal')

if __name__ == "__main__":
    root = tk.Tk()
    app = ModernFileSplitter(root)
    root.mainloop()