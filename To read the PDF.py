# To read the PDF
import PyPDF2

# To analyze the PDF layout and extract text
from pdfminer.high_level import extract_pages, extract_text
from pdfminer.layout import LTTextContainer, LTChar, LTRect, LTFigure

# To extract text from tables in PDF
import pdfplumber

# To extract the images from the PDFs
from PIL import Image
from pdf2image import convert_from_path

# To perform OCR to extract text from images
import pytesseract

# To remove the additional created files
import os
from PyPDF2 import PdfFileReader

# create pdf file reader object
from PyPDF2 import PdfReader
pdf = PdfReader(r"C:\Users\joshu\OneDrive\FYP final\HRM Braily.pdf")
number_of_pages = len(pdf.pages)
page = pdf.pages[6]
text = page.extract_text()

#print output
print(text)

import re

skills = ["HRM","examine","batman"]

print("Extracted skills:")

for word in skills:
    search_string = text
    # find the word in the string using regular expressions
    match = re.search(word, search_string)
    if match:
        # extract the word using slicing
        start_index = match.start()
        lword = len(word)
        extracted_word = search_string[start_index:start_index + lword]
        print(extracted_word)