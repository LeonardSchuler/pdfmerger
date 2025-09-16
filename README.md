# PDF Merger

A simple desktop application for merging multiple PDF files into a single document using Python and tkinter.

## Features

- Select multiple PDF files through a user-friendly GUI
- Drag-and-drop file selection with file browser
- Merge selected PDFs in the order they were added
- Save merged PDF to a location of your choice
- Clear file list to start over

## Requirements

- Python 3.13+
- pypdf library

## Installation

1. Clone or download this repository
2. Install dependencies using uv:
   ```bash
   uv sync
   ```

## Usage

Run the application:
```bash
python main.py
```

1. Click "Add PDFs" to select PDF files
2. Files will appear in the list in the order selected
3. Click "Merge PDFs" to combine them and save the result
4. Choose where to save your merged PDF file

## Building an Executable

To create a standalone executable:

1. Install pyinstaller:
   ```bash
   uv sync --group install
   ```

2. Build the executable:
   ```bash
   pyinstaller --add-data "THIRD_PARTY_LICENSES.txt:." --add-data "LICENSE:." --onefile --windowed main.py
   ```

The executable will be created in the `dist/` directory.

## License

This project is open source and available under the MIT License.