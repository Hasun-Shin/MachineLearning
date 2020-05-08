import pytesseract
import cv2
originalImg = cv2.imread('hue.jpg')
originalImg = cv2.resize(originalImg, None, fx=2.5, fy=2.5)
img = cv2.cvtColor(originalImg, cv2.COLOR_BGR2GRAY)
_,img = cv2.threshold(img,100,255,cv2.THRESH_BINARY)
h, w = img.shape
letters = pytesseract.image_to_boxes(img)
letters = letters.split('\n')
letters = [letter.split() for letter in letters]
for letter in letters:    
    cv2.rectangle(originalImg, (int(letter[1]), h - int(letter[2])), (int(letter[3]), h - int(letter[4])), (0,0,255), 1)

# cv2.imshow('', originalImg)

cv2.imshow('hue.jpg', originalImg)
