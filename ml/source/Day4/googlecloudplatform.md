구글 API 이용 Keras 사진 분류. 

- 구글 계정 로그인하기

- google cloud platform 
- 상단의 새 프로젝트 생성하기.  (예:ImageDetect)
- 왼쪽 API서비스 , Credential(사용자 인증 정보 ) (이때 프로젝트 선택하기 !)
- +사용자 인증 정보 만들기 선택 API 생성 키 기억하기.  
- 왼쪽 라이브러리 클릭하기. 여러 라이브러리들이 나온다.  여기에서 Custom Search API 를 사용설정 누른다. 
- 검색할 수 있는 엔진(구글) 을 설정해보자.  https://cse.google.com/cse/all 접속하기
- 추가 -> 구글 www.google.com 
-  검색엔진 수정하기.  (제어판 클릭)
- 검색엔진 ID가 생겨남. 
- 이미지 검색 : 사용함.  /전체 웹검색 : 사용함. 
- 왼쪽 상단 맞춤검색 클릭.  수정할 수 있음. 
- 가상환경 만들고 싶으면 만들고
  - pip install pylint
  - pip install requests
  - pip install python-dotenv
  - pip install google-api-python-client

------------------------

- 새 폴더 생성 (cnn_project)
- API 생성키, 검색엔진 ID를 seetings.py로 만들어서 폴더 내  저장하기.
- 01.img.dl.gcs.py 를 통해 사진을 불러들어온다.

---------------------------------

얼굴검출 프로그램

- pip install opencv-python
- Haar Cascade
  -  머신러닝 기반 오브젝트 검출 알고리즘 . 
  - https://docs.opencv.org/4.1.0/dc/d88/tutorial_traincascade.html
  - https://github.com/opencv/opencv/tree/master/data/haarcascades 눈검출, 등등 파일이 올라와있음. 다운받기

- 이미지를 api 에서 불러들어온다. 예: 전지현 100장, 송혜교 100장
- 불러들어온 이미지에서 얼굴을 인식하는 프로그램 실행하고, 64x64로 얼굴부분만 만든다.
- data augmentation을 실시한다. (flip, rotate, blur...)
- Graphvize 설치하고 직접 학습 모델을 실시한다(conv....... 등등.  )

---------------

Graphvize

- 모델 summary 부분을 그림으로 나타내준다. 
- pip install graphviz
- pip install pydotplus 설치. 
  - https://graphviz.gitlab.io/_pages/Download/Download_windows.html 
  - msi 설치. 