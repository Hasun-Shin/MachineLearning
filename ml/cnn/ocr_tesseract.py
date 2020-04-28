from PIL import Image
from pytesseract import*


filename = "C:/Users/LGPC/Desktop/fonts_inc/00_0.jpg"
image = Image.open(filename)
text = image_to_string(image,lang="kor")
with open("sample.txt","w") as f:
    f.write(text)