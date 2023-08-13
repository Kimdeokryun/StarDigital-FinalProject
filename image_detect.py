import easyocr
from yolov5.detect import run
import os

# 번호판 탐지
def detecting(file_path, file_name):
    v5_weights = "yo5s_b32_e10.pt"
    v5_data = "custom.yaml"
    v5_project = "result_save"
    v5_source = file_path

    save_dir, detect_result = run(weights=v5_weights
                                  , source=v5_source
                                  , data=v5_data
                                  , imgsz=(416, 416)
                                  , project=v5_project

                                  , name="res"  # 탐지 결과 폴더를 exp 대신에 지정한 이름으로 폴더 생성
                                  , save_txt=True  # 바운딩박스 클래스, 좌표, mAP를 labels/.txt로 저장
                                  , save_conf=True  # txt파일에 mAP 결과를 저장
                                  , save_crop=True  # 바운딩박스 자르기, crops에 저장
                                  , exist_ok=True  # name 폴더의 번호 자동 증가 안함
                                  , line_thickness=0  # 이미지 바운딩박스 선 굵기
                                  , hide_labels=True  # 이미지 바운딩박스 class를 표시 안함
                                  , hide_conf=True  # 이미지 바운딩박스 mAP 표시 안함
                                  )

    result_split = detect_result[0].split(" ")

    bound_file = "result_save/res/" + file_name

    print(bound_file, result_split[1])

    if float(result_split[1]) > 0.6:
        crop_file_name = file_name.replace(".png", ".jpg")
        crop_file = "/result_save/res/crops/plate/" + crop_file_name
        plate_number = recognize_license_plate(crop_file)
    else:
        plate_number = None

    return bound_file, plate_number

def recognize_license_plate(image_path):
    origin_dir = os.getcwd()  # 현재 작업 디렉토리
    image_path = origin_dir + image_path
    try:
        reader = easyocr.Reader(['ko', 'en'])
        results = reader.readtext(image_path)
        return results[0][1]
    except Exception as e:
        print(f"An error occurred: {e}")
        return None