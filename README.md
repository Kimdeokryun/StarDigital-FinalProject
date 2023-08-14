# StarDigital-FinalProject
스타디지털육성프로그램 개인 심화 프로젝트 - 요구 명세서 총 3개에 따른 결과값을 도출

## 프로젝트 개요

이 프로젝트는 제공된 총 3개의 요구 명세서에 맞춰서 개발을 진행하는 개인 심화 프로젝트 입니다. 

## 주요 기능

### 메인 페이지
- 웹페이지를 통해 제공된 총 3개의 요구 명세서를 모두 개발하는 것으로 진행
- 메인 화면에 요구 명세서에 대한 주제와, 목표가  간략히 적혀있음
- 깃허브의 프로젝트를 정리하고, 앞으로 진행할 프로젝트에 대한 정리를 통해 메인 페이지를 개인 블로그화 예정

  
### 필요한 데이터를 수집하여 저장히기
- requests 라이브러리를 통해, 세종특별자치시의 흡연구역 위치 데이터를 수집
- pandas 라이브러리를 통해 데이터 프레임화
- 경도값이 클 수록 동쪽에 가깝다는 것을 이용해 데이터 프레임을 경도 기준으로 역순 정렬
- 웹 페이지의 세종특별자치시의 흡연구역 위치 데이터 수집 탭을 통해 확인 가능하도록 진행
- csv 파일 다운로드 버튼을 통해 데이터프레임화 값을 .csv 파일로 다운로드 받을 수 있음


### 학습한 ML/DL 엔진을 .py로 실행
- 웹페이지를 통한 이미지 input 은 파일 선택 뿐만이 아닌 드래그 앤 드롭을 통해 input 할 수 있도록 구현
- 번호판이 보이는 자동차의 이미지 input을 통해 번호판의 이미지만을 crop 하는 yolov5 모델
- 사전 학습된 yolov5 모델을 통해 번호판을 crop 하고, 이미지를 저장
- 저장된 이미지를 easyocr 라이브러리를 활용하여 번호판에 적힌 값을 읽어 반화
- 반환된 값을 웹페이지에 이미지와 같이 띄움

### 학습한 엔진을 .py로 실행
- Flask를 활용하여 요구 명세서에 명시된 기능들을 서비스화
- 간단한 로그인과 회원가입 기능을 구현
- MySQL을 활용하여 중복된 아이디로 회원가입 시 회원 가입 실패 알림
- Flask session을 통해 로그인 한 사용자만 번호판 값 인식 기능 사용 가능
- 웹 페이지의 디자인은 부트스트랩을 활용

## 사용 기술 및 도구
- 언어: Python
- 웹 프론트엔드: HTML, CSS, JavaScript
- 프레임워크: Flask
- 데이터베이스: MySQL, AWS RDS


### 메인 화면
![image](https://github.com/Kimdeokryun/StarDigital-FinalProject/assets/96904134/89b6baf0-fa7f-4091-9f00-06b32d55b70a)

### 기능 1 화면 
![image](https://github.com/Kimdeokryun/StarDigital-FinalProject/assets/96904134/f122c562-3d24-443e-b396-17a937a3822a)

### 기능 2 화면
![image](https://github.com/Kimdeokryun/StarDigital-FinalProject/assets/96904134/4906872b-a389-4c94-aec6-e095c3f91663)
![image](https://github.com/Kimdeokryun/StarDigital-FinalProject/assets/96904134/81b59203-e7bd-49f7-b801-54530a378f01)

### 기능 2  AI 기술 향후 확장 가능
링크: https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=&topMenu=&aihubDataSe=realm&dataSetSn=172
![image](https://github.com/Kimdeokryun/StarDigital-FinalProject/assets/96904134/076278e3-f19e-43a9-86a6-d2524657f4c9)



### 기능 3 화면
![image](https://github.com/Kimdeokryun/StarDigital-FinalProject/assets/96904134/e3760fb3-9d1d-413a-9a8c-b54f034ef72c)
![image](https://github.com/Kimdeokryun/StarDigital-FinalProject/assets/96904134/bd63a279-4740-4ee4-a1f1-140dc841bf3f)

