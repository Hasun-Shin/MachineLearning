try:
    import Image
except ImportError:
    from PIL import Image

import pytesseract

import pytesseract

# 영어 인식
# print(pytesseract.image_to_string(Image.open('ori.jpg')))

# 한글 인식

print(pytesseract.image_to_string(Image.open('ori2.JPG'), lang='Kor'))


