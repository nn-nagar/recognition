from django.test import TestCase

# Create your tests here.
from PIL import Image
from pytesseract import image_to_string
print("------------------------")

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'


img = Image.open('api/backside.jpg')

img.show()

text = image_to_string(img)
print("<<<<<<<<>>>>>>>>>>>>>>>>>>")
print(text)

