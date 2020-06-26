import pytesseract
from PIL import Image

def to_text(fr):
    text = pytesseract.image_to_string(fr)
    return text