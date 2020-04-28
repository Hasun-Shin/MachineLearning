import sys
import os
import cv2
import keras
import numpy as np
import matplotlib.pyplot as plt
import settings
import pathlib
import glob

RETURN_SUCCESS = 0
RETURN_FAILURE = -1
# Inpou Model Directory
INPUT_MODEL_PATH = "./model/model_laplacian.h5"

def main():
    IMAGE_PATH_PATTERN = "./testset/*"
    image_paths = glob.glob(IMAGE_PATH_PATTERN)
    # 파일별로 읽기
    for image_path in image_paths:
        path = pathlib.Path(image_path)
        # 파일 경로
        fullpath = str(path.resolve())
        # 파일명
        filename = path.name
        print(f"이미지파일(파일명):{filename}")
        # 이미지 읽기
        image = cv2.imread(fullpath)
        image = cv2.resize(image, (76,76))
        image = cv2.Laplacian(image, cv2.CV_8U)
        image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        image = np.expand_dims(image, axis=(0,3))
        if image is None:
            print(f"이미지 파일을 읽을 수 없습니다({image_file_path})")
            return RETURN_FAILURE
        # 모델 파일 읽기
        if not os.path.exists(INPUT_MODEL_PATH):
            print("MODEL 파일이 존재하지 않습니다.")
            return RETURN_FAILURE
        
        model = keras.models.load_model(INPUT_MODEL_PATH)

        result_image = model.predict(image)
        print("after predict", np.argmax(result_image[0]))

    return RETURN_SUCCESS



if __name__ == "__main__":
    main()