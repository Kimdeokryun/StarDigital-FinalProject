from flask import Flask, request, render_template, Response, send_file, session
from werkzeug.utils import secure_filename
from image_detect import detecting
from datetime import datetime
from flask_cors import CORS
from dbmodule import insert_user, check_user
from check_api import data_processing
from urllib.parse import quote
import pandas as pd

import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # 보안을 위한 시크릿 키 설정
app.config['PERMANENT_SESSION_LIFETIME'] = 600 # 세션 유지 시간 설정
CORS(app)

def get_now():
    now = datetime.now()
    print(now)
    return now


@app.route('/')
@app.route('/index')
def index():
    return render_template("home.html")


@app.route('/auth')
def auth_page():
    return render_template('auth.html')


@app.route('/login', methods=['GET',"POST"])
def login():
    id = request.form.get("username")
    pw = request.form.get("password")
    if check_user(id, pw) == 1:
        session.permanent = True
        session['user_id'] = id  # 세션에 사용자 아이디 저장
        return render_template('home.html')
    else:
        return render_template('auth.html', error="login_error")


@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return render_template('home.html')


@app.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == "POST":
        id = request.form.get("username")
        pw = request.form.get("password")
        if insert_user(id, pw) == 0:
            session.permanent = True  # 세션 유지 설정
            session['user_id'] = id  # 세션에 사용자 아이디 저장
            return render_template('home.html')
        else:
            return render_template('signup.html', error="signup_error")
    else:
        return render_template('signup.html')


# -------------------------------------------------
# 이미지 파일 업로드
# -------------------------------------------------
@app.route('/file_upload', methods=["GET", "POST"])
def file_upload():
    return render_template("file_upload.html")


@app.route('/result', methods=['POST'])
def show_result():
    if 'user_id' not in session:
        return render_template("file_upload.html", error="session")

    if 'file' in request.files:
        f = request.files['file']

        # 파일 이름 변경
        now = get_now()
        file_name = str(now.strftime('%Y%m%d_%H%M%S'))
        file_name += "_" + secure_filename(f.filename)

        # 파일 저장 경로
        file_dir = "upload_files"
        file_path = os.path.join(file_dir, file_name)

        # 파일 저장
        f.save(file_path)

        # 번호판 탐지 후, class 번호와 mAP 값을 출력
        label_file, plate_number = detecting(file_path, file_name)

        dic_data = {"image_path": label_file, "detect_result": plate_number}

        print(dic_data)

        return render_template('result_page.html', json_data=dic_data)


@app.route('/get_image', methods=['POST'])
def get_image():
    image_path = request.json.get('image_path')
    return send_file(image_path, mimetype='image/png')



# -------------------------------------------------
# 세종시 흡연구역 위치 수집 및 저장
# -------------------------------------------------

@app.route('/data_request')
def data_request():
    return render_template("data_request.html")


@app.route('/data_process', methods=['POST'])
def data_process():
    df, df2 = data_processing()

    print(df)

    if df is None or df2 is None:
        return render_template("data_request.html", error="dferror")
    else:
        return render_template("data_process.html", df=df, df2=df2)


@app.route('/data_download', methods=['POST'])
def data_download():
    print("다운로드 요청")
    df, df2 = data_processing()

    if df is None or df2 is None:
        return render_template("data_request.html", error="dferror")

    today = str(get_now().strftime('%Y%m%d'))
    file_name = "result_save/세종시흡연위치_" + today + ".csv"

    df2.to_csv(file_name, index=False, encoding="utf-8-sig")

    return send_file(file_name, mimetype='text/csv', as_attachment=True)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)