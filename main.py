import Image_text_convertor
import Text_translator
import pytesseract
from PIL import Image
import sys
import os

filepath = sys.argv[1]

assert os.path.exists(filepath), 'Invalid path'

img = Image.open(filepath)
text = Image_text_convertor.to_text(img)
trans = Text_translator.translate_to_text(text)
print(trans)