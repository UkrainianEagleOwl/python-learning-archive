# Clean Folder Package

## Overview
This Python package transforms the folder sorting script into a convenient, installable package that can be executed from anywhere in the system using the console command `clean-folder`. It organizes files in a specified directory by their types and includes features like file normalization and categorization.

## Package Structure
```
clean_folder/
├── clean_folder/
│   ├── clean.py         # Main script with sorting logic
│   └── __init__.py      # Initializes the package
└── setup.py             # Setup script for package installation
```

## Features
- **System-Wide Installation**: Installable via pip or setup.py.
- **Console Command**: Executable as `clean-folder` from any location in the system.
- **Directory Sorting**: Sorts files in a given directory into categorized folders.
- **File Normalization**: Renames files to maintain a consistent naming convention.
- **Argument Handling**: Processes command-line arguments like the original script.

## Installation
1. Clone the repository.
2. Navigate to the root directory (`clean_folder/`).
3. Install the package using one of the following commands:
   - With pip (editable mode): `pip install -e .`
   - With setup.py (may require administrator rights): `python setup.py install`

## Usage
After installation, use the package from any location in your system:
```
clean-folder [path_to_directory]
```
Replace `[path_to_directory]` with the path of the directory you want to organize.

## Requirements for setup.py
- Properly configure `setup.py` to enable system-wide installation and command-line execution.
- Ensure the package is recognized as `clean_folder` in the system.
- The script `clean.py` should handle command-line arguments as the original Python script did.

## Development and Contribution
Feel free to contribute to the development of this package by submitting pull requests or issues on the repository page.
