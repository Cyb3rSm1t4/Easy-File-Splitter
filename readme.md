# Modern File Splitter

A modern, user-friendly GUI application for splitting large files into smaller chunks. Built with Python and Tkinter, featuring a clean interface and progress tracking.

![File Splitter Interface](screenshots/interface.png)

## Features

- 🎯 Split large files into specified chunk sizes
- 💻 Modern, intuitive GUI interface
- 📊 Real-time progress tracking
- 🚀 Multi-threaded processing for better performance
- 🎨 Animated, modern UI elements
- 📁 Custom output directory selection
- ⚙️ Configurable chunk size and worker threads

## Installation

### Option 1: Download the Executable
1. Go to the [Releases](https://github.com/YourUsername/file-splitter/releases) section
2. Download the latest `filesplitter_gui.exe`
3. Run the application directly - no installation needed!

### Option 2: Run from Source
```bash
# Clone the repository
git clone https://github.com/YourUsername/file-splitter.git

# Navigate to the directory
cd file-splitter

# Create a virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Install requirements
pip install -r requirements.txt

# Run the application
python filesplitter_gui.py
```

## Usage

1. Launch the application
2. Click "Browse" to select your input file
3. Choose an output directory for the split files
4. Set your desired chunk size (in GB)
5. Adjust the number of workers if needed
6. Click "Start Splitting"
7. Monitor progress through the progress bar

## Requirements

- Windows 7/8/10/11
- No additional software required for executable
- For source code:
  - Python 3.8+
  - Pillow
  - tkinter (usually comes with Python)

## Building from Source

To create your own executable:
```bash
pip install pyinstaller
pyinstaller --onefile --windowed filesplitter_gui.py
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built using Python and Tkinter
- UI inspired by modern design principles
