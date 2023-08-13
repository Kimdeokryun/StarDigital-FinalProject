import pymysql

def db_connect():
    db = pymysql.connect(
        host='actionlearning.cv24ixr0qpgh.ap-northeast-2.rds.amazonaws.com',
        user='rlaejrfbs',
        password='jser0211',
        database='project',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

    return db


def make_table():
    db = db_connect()
    try:
        # 테이블 생성 쿼리
        create_table_query = """
            CREATE TABLE IF NOT EXISTS users (
                idx INT AUTO_INCREMENT PRIMARY KEY,
                id VARCHAR(255) NOT NULL,
                pw VARCHAR(255) NOT NULL
            )
        """

        # 데이터베이스와 연결된 커서 생성
        with db.cursor() as cursor:
            # 테이블 생성
            cursor.execute(create_table_query)
            db.commit()

            print("데이터베이스 작업이 완료되었습니다.")

    finally:
        # 데이터베이스 연결 닫기
        db.close()


def insert_user(user_id, user_pw):
    db = db_connect()
    existing = 0


    try:
     # 데이터베이스와 연결된 커서 생성
        with db.cursor() as cursor:
            # 사용자 정보 추가
            select_query = "SELECT id FROM users WHERE id = %s"
            cursor.execute(select_query, (user_id,))
            existing_user = cursor.fetchone()

            if existing_user:
                print("이미 존재하는 아이디입니다.")
                existing = 1
            else:
                insert_query = "INSERT INTO users (id, pw) VALUES (%s, %s)"
                users_to_insert = [(user_id, user_pw)]

                cursor.executemany(insert_query, users_to_insert)
                db.commit()

                print("회원가입 완료")
    finally:
        # 데이터베이스 연결 닫기
        db.close()

    return existing


def check_user(user_id, user_pw):
    db = db_connect()
    success = 0

    try:
        # 데이터베이스와 연결된 커서 생성
        with db.cursor() as cursor:
            # 사용자 정보 추가
            select_query = "SELECT id FROM users WHERE id = %s AND pw = %s"
            cursor.execute(select_query, (user_id,user_pw))
            user_data = cursor.fetchone()

            if user_data:
                print("로그인 완료")
                success = 1
            else:
                print("로그인 실패")
    finally:
        # 데이터베이스 연결 닫기
        db.close()

    return success