from PIL import Image
from pytesseract import*
import cv2


# import pytesseract
# from pytesseract import Output


# filename = "C:/Users/LGPC/Desktop/fonts_inc/00_0.jpg"
filename = "C:/Users/LGPC/Desktop/Study/multicampus/MachineLearning/ml/cnn/ori3.jpg"

image = Image.open(filename)

text = image_to_string(image,lang="kor")
print(text)
# with open("sample2.txt","w") as f:
#     f.write(text)




# img = cv2.imread('oo.jpg')

# # d = pytesseract.image_to_data(img, output_type=Output.DICT)
# d = pytesseract.image_to_data(img, output_type=Output.DICT)
# print(d)

# n_boxes = len(d['level'])
# print(d['level'])

# for i in range(n_boxes-1):
#     (x, y, w, h) = (d['left'][i+1], d['top'][i+1], d['width'][i+1], d['height'][i+1])
#     cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

# cv2.imshow('img', img)
# cv2.waitKey(0)



# print(pytesseract.image_to_boxes(Image.open('01_0.jpg')))

# b = pytesseract.image_to_boxes(Image.open('01_0.jpg'))


