### README

# File Organizer Script

## Overview
This Python script efficiently organizes files in a specified directory. It sorts files by type, renames them for consistency, and removes unnecessary empty folders. The script is versatile and can be customized to suit individual sorting preferences.

## Features
- **File Sorting**: Categorizes files into images, videos, documents, audio files, and archives. Unknown file types are handled separately.
- **Supported File Types**:
  - Images: JPEG, PNG, JPG, SVG
  - Videos: AVI, MP4, MOV, MKV
  - Documents: DOC, DOCX, TXT, PDF, XLSX, PPTX
  - Audio: MP3, OGG, WAV, AMR
  - Archives: ZIP, GZ, TAR
- **Transliteration**: Converts Cyrillic characters to Latin script.
- **Normalization**: Renames files by replacing non-Latin characters and numbers with '_'.
- **Empty Folder Cleanup**: Automatically removes empty directories.
- **Archive Handling**: Extracts archives and organizes contents into dedicated folders.

## Usage
Run the script with the folder path as an argument. For example:
```
python sort.py /user/Desktop/Мотлох
```

## Functionality
- **normalize Function**:
  - Transliterates Cyrillic to Latin.
  - Replaces non-Latin, non-numeric characters with '_'.
  - Maintains the case of letters after transliteration.
- **File Processing**:
  - Images to `images/`
  - Documents to `documents/`
  - Audio files to `audio/`
  - Video files to `video/`
  - Extracts archives to `archives/`, with subfolders named after the archive.
- **Criteria**:
  - File extensions remain unchanged after renaming.
  - Empty folders are deleted.
  - Ignores predefined directories (`archives`, `video`, `audio`, `documents`, `images`).
  - Files with unknown extensions remain unaltered.

## Installation
Clone the repository and run the script in your Python environment. Ensure you have necessary permissions for file operations in the target directory.
