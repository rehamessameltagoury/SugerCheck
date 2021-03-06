import cv2
import numpy as np
import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
from pytesseract import Output
import os
import re
from difflib import SequenceMatcher
from PIL import Image

img = cv2.imread('Image.PNG')



# get grayscale image
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# thresholding
def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]



def cleaning(text):
	text= re.sub('[*|\n|\|(|)|.]',' ',text)
	text = re.sub('[}|{|\|/|,|:]',' ',text)
	text = re.sub(' +',' ',text)
	ingredients = text.split()
	return ingredients


if __name__ == '__main__':
            gray = get_grayscale(img)
            thresh = thresholding(gray)
            text = pytesseract.image_to_string(Image.open(os.path.abspath("Image.PNG")))
            inglist = cleaning(text)
            print(inglist)
