Modern File Splitter

A modern, user-friendly GUI application for splitting large files into smaller chunks. Built with Python and Tkinter, featuring a clean interface and progress tracking.

File Splitter Interface
Features

    🎯 Split large files into specified chunk sizes
    💻 Modern, intuitive GUI interface
    📊 Real-time progress tracking
    🚀 Multi-threaded processing for better performance
    🎨 Animated, modern UI elements
    📁 Custom output directory selection
    ⚙️ Configurable chunk size and worker threads

Installation
Option 1: Download the Executable

    Go to the Releases section
    Download the latest filesplitter_gui.exe
    Run the application directly - no installation needed!

Option 2: Run from Source

# Clone the repository
git clone https://github.com/Cyb3rSm1t4/Easy-File-Splitter.git

# Navigate to the directory
cd Easy-File-Splitter

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

Usage

    Launch the application
    Click "Browse" to select your input file
    Choose an output directory for the split files
    Set your desired chunk size (in GB)
    Adjust the number of workers if needed
    Click "Start Splitting"
    Monitor progress through the progress bar

Requirements

    Windows 7/8/10/11
    No additional software required for executable
    For source code:
        Python 3.8+
        Pillow
        tkinter (usually comes with Python)

Building from Source

To create your own executable:

pip install pyinstaller
pyinstaller --onefile --windowed filesplitter_gui.py

Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
License

This project is licensed under the MIT License - see the LICENSE file for details.
Acknowledgments

    Built using Python and Tkinter
    UI inspired by modern design principles
