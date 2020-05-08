import cv2
import pytesseract

filename = 'C:/Users/LGPC/Desktop/Study/multicampus/MachineLearning/ml/cnn/hue.JPG'

# read the image and get the dimensions
img = cv2.imread(filename)
h, w, _ = img.shape # assumes color image

# # run tesseract, returning the bounding boxes
boxes = pytesseract.image_to_boxes(img) # also include any config options you use

# # draw the bounding boxes on the image
for b in boxes.splitlines():
    b = b.split(' ')
    img = cv2.rectangle(img, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)
    # print(b)
    

# show annotated image and wait for keypress
cv2.imshow(filename, img)
# cv2.imshow(filename,boxes)

cv2.waitKey(0)




# from pytesseract import pytesseract as pt

# pt.run_tesseract('ori.jpg', 'output', lang=None, boxes=True, config="hocr")

# To read the coordinates
# boxes = []
# with open('output.box', 'rb') as f:
#     reader = csv.reader(f, delimiter = ' ')
#     for row in reader:
#         if(len(row)==6):
#             boxes.append(row)

# # Draw the bounding box
# img = cv2.imread('ori.jpg')
# h, w, _ = img.shape
# for b in boxes:
#     img = cv2.rectangle(img,(int(b[1]),h-int(b[2])),(int(b[3]),h-int(b[4])),(255,0,0),2)

# cv2.imshow('output',img)

# boxes = pytesseract.image_to_data(img, config='')
# cv2.imshow(filename,boxes)    
