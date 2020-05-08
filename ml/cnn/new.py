from PIL import Image

import pytesseract
import argparse
import cv2
import os

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                help="path to input image to be OCR' d")
ap.add_argument("-p", "--preprocess", type=str, default="thresh",
                help="type of preprocessing to be done")
args = vars(ap.parse_args())

# load the example image and convert it to grayscale
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# check to see if we should apply thresholding to preprocess the
# image
if args["preprocess"] == "thresh":
    gray = cv2.threshold(gray, 0, 255,
                         cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

# make a check to see if median blurring should be done to remove
# noise
elif args["preprocess"] == "blur":
    gray = cv2.medianBlur(gray, 3)

# write the grayscale image to disk as a temporary file so we can
# apply OCR to it
filename = "{}.JPG".format(os.getpid()) #현재 프로세스 아이디. 
cv2.imwrite(filename, gray)

print(filename)
print("되나?1")
# load the image as a PIL/Pillow image, apply OCR, and then delete
# the temporary file
img = Image.open(filename)

print("되나?2")

tessdata_dir_config = '--tessdata-dir "C:/Program Files/Tesseract-OCR/tessdata"'
# Example config: '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'
# It's important to include double quotes around the dir path.
print("되나?3")

text = pytesseract.image_to_string(img, lang='kor', config=tessdata_dir_config)

print("되나?4")
# os.remove(filename)

print("되나?5")
print(text)

print("되나?6")
# with open("sample3.txt","w") as f:
#     f.write(text)


