# Quick OCR Parser and Pattern Matcher

## Functionality
Run app by opening a prompt in the same directory as the `tesseract_start.py` file and executing the **$ streamlit run tesseract_start.py** command.

[Tesseract](https://tesseract-ocr.github.io/tessdoc/Installation.html) is a time tested tool for optical character recognition (OCR) in scanned documents. The common implementation of the tesseract library is in C++, but the library [pytesseract](https://pypi.org/project/pytesseract/) makes this available in a simple Python API. In order to select some basic patterns through a GUI, I've added a simple [streamlit](https://streamlit.io/) web app to select a directory and run OCR on all of the directory's images, then match string patterns afteward. All data is saved to a CSV acknowledging the source file and pattern being matched.

This is not meant to be a full fledged app in any sense of the word, however it should provide a **very** simple framework for adding more complex OCR (such as with [convolutional networks](https://en.wikipedia.org/wiki/Convolutional_neural_network)) and more complex patterns (such as with [regex](https://en.wikipedia.org/wiki/Regular_expression)). Other considerations like pattern complexity and internal state backups have been considered but are only added for the simplest uses.

## Requirements
[Tesseract](https://github.com/tesseract-ocr/tesseract): Primary library, installed independent of Python API. Tested on Windows, but available on all major OSs. 
- [Windows Install](https://github.com/UB-Mannheim/tesseract/wiki) 
- [Ubuntu Install](https://notesalexp.org/tesseract-ocr/packages5/) 
- [macOS Install](https://github.com/scott0123/Tesseract-macOS)

### Python Pip Libraries
Install all libraries with the `requirements.txt` file by entering **$ python -m pip install -r requirements.txt** in a command prompt.

[`pytesseract`](https://pypi.org/project/pytesseract/): Provides API for accessing Tesseract
[`streamlit`](https://streamlit.io/): Quick & simple interactive web app API
[`opencv`](https://opencv.org/): For reading in images (can also perform OCR)
[`pandas`](https://pandas.pydata.org/): For storing and exporting text findings
[`joblib`](https://joblib.readthedocs.io/en/stable/): Used for saving internal state