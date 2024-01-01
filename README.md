# Image to PDF Converter

This Python script utilizes the Pillow library to convert a collection of image files (JPG, PNG, and JBEG) in a specified directory into a single PDF file named "photos.pdf."

## Features

- **File Compatibility:** The script recognizes and processes image files with extensions .jpg, .png, and .jbeg.

- **Conversion to PDF:** Converts the eligible image files into a single PDF file using the Pillow library.

- **Resolution Setting:** Allows for setting the resolution of the output PDF.

## Usage

1. Place the image files you want to convert in a directory (default: "photos").
2. Run the script, and it will create a PDF file named "photos.pdf" in the same directory.

## requirements
The requirements are under requirements.txt

## How to Run

```bash
pip install -r requirements.txt
python script.py
```
