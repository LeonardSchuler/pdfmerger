# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a simple PDF merger application built with Python and tkinter. The application provides a GUI for selecting multiple PDF files and merging them into a single output file.

## Architecture

- **main.py**: Single-file application containing the `PDFMergerApp` class
- Uses `tkinter` for the GUI interface
- Uses `pypdf` library for PDF manipulation
- Self-contained desktop application with no external dependencies beyond Python packages

## Development Commands

**Install dependencies:**
```bash
uv sync
```

**Run the application:**
```bash
python main.py
```

**Build executable (when pyinstaller is installed):**
```bash
uv sync --group install
pyinstaller --add-data "THIRD_PARTY_LICENSES.txt:." --add-data "LICENSE:." --onefile --windowed main.py
```

**Update the third party licenses:**
```bash
uv sync --group license
pip-licenses --format=plain-vertical --with-license-file --no-license-path > THIRD_PARTY_LICENSES
```

## Key Implementation Details

- The application maintains a list of selected PDF files in `self.files`
- GUI components are created in `__init__` with tkinter widgets
- PDF merging is handled by the `pypdf.PdfWriter` class
- File operations include error handling with messagebox dialogs
- No external configuration files or complex project structure