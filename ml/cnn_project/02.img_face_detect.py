#-*- coding: utf-8 -*- 
import os
import pathlib
import glob
import cv2
import settings

def load_name_images(image_path_pattern):
    name_images = []
    # 지정한 Path Pattern에 일치하는 파일 얻기
    image_paths = glob.glob(image_path_pattern)
    # 파일별로 읽기
    for image_path in image_paths:
        path = pathlib.Path(image_path)
        # 파일 경로
        fullpath = str(path.resolve()) #절대 경로로 읽어들임. 
        print(f"이미지 파일(절대경로):{fullpath}")
        # 파일명
        filename = path.name
        print(f"이미지 파일(파일명):{filename}")

        # 이미지 읽기
        image = cv2.imread(fullpath)
        if image is None:
            print(f"이미지 파일[{fullpath}]을 읽을 수 없습니다.")
            continue
        name_images.append((filename, image))
    return name_images


        # TO-DO 


def detect_image_face(file_path, image, cascade_filepath):
    # 이미지 파일의 Grayscale화
    image_gs = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # 캐스케이드 파일 읽기
    cascade = cv2.CascadeClassifier(cascade_filepath)
    print(file_path)
    # 얼굴인식
    faces=cascade.detectMultiScale(image_gs, scaleFactor=1.1, minNeighbors=15, minSize=(64,64))
    if len(faces) ==0:
        print("얼굴인식 실패")
        # return
    print("얼굴인식 성공")

    #1개 이상의 얼굴 인식
    #[76 31 83 83] -> x_pos, y_pos, width, height 
    face_count = 1
    for (x_pos, y_pos, width, height) in faces:
        face_image = image[y_pos:y_pos+height, x_pos:x_pos+width] #y,x 행부터 읽어들임 ! 행(세로)부터 지정하기. 
        if face_image.shape[0] >64:
            face_image = cv2.resize(face_image, (64,64))
        print(face_image.shape)
        #저장 
        #00_001.jpg -> 00_001-1.jpg
                #   -> 00_001-2.jpg 두개 얼굴이 검출되면 나눠서 저장하겠다. 
        path = pathlib.Path(file_path)
        directory = str(path.parent.resolve())
        filename = path.stem
        extension = path.suffix
        output_path = os.path.join(directory, f"{filename}_{face_count:03}{extension}")

        print("출력파일(절대경로):{output_path}")
        try:
            cv2.imwrite(output_path, face_image)
            face_count = face_count +1
        except:
            print("EXception occured:{},{}".format(output_path))
            # pass

    return
    # TO-DO 

    # 1개 이상의 얼굴인식
    # TO-DO 
    return RETURN_SUCCESS

def delete_dir(dir_path, is_delete_top_dir=True):
    for root, dirs, files in os.walk(dir_path, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))
    if is_delete_top_dir:
        os.rmdir(dir_path)
    

RETURN_SUCCESS = 0
RETURN_FAILURE = -1
# Origin Image Pattern
IMAGE_PATH_PATTERN = "./origin_image/*"
# Output Directory
OUTPUT_IMAGE_DIR = "./face_image"

def main():
    print("===================================================================")
    print("이미지 얼굴인식 OpenCV 이용")
    print("지정한 이미지 파일의 정면얼굴을 인식하고, 64x64 사이즈로 변경")
    print("===================================================================")

    # 디렉토리 작성
    if not os.path.isdir(OUTPUT_IMAGE_DIR):
        os.mkdir(OUTPUT_IMAGE_DIR)
    # 디렉토리 내의 파일 제거
    delete_dir(OUTPUT_IMAGE_DIR, False)

    # 이미지 파일 읽기
    # TO-DO 
    name_images = load_name_images(IMAGE_PATH_PATTERN)

    
    # 이미지별로 얼굴인식 -> 2명 -> 200개 
    # for name_image in name_images:
        # TO-DO ->197
    for name_image in name_images:
        file_path = os.path.join(OUTPUT_IMAGE_DIR, f"{name_image[0]}")
        image = name_image[1]
        cascade_filepath = settings.CASCADE_FILE_PATH
        detect_image_face(file_path, image, cascade_filepath)


    return RETURN_SUCCESS

if __name__ == "__main__":
    main()