import pandas as pd
import requests


def data_processing():
    url = 'http://apis.data.go.kr/5690000/sjSmokingAreaLocation/sj_00001180'
    params = {'serviceKey': '',
              'pageIndex': '1', 'pageUnit': '20', 'dataTy': 'json', 'searchCondition': 'nm', 'searchKeyword': '세종'}

    response = requests.get(url, params=params)
    json_data = response.json()

    header = json_data["header"]
    body = json_data["body"]

    totalCount = header["totalCount"]
    items = body["items"]

    if int(totalCount) > 0:
        data = []

        for item in items:
            roadNmAddr = item["roadNmAddr"]
            mngInstNm = item["mngInstNm"]
            la = item["la"]
            lo = item["lo"]
            boolean_len = True if len(roadNmAddr) > 15 else False
            row = [roadNmAddr, mngInstNm, la, lo, boolean_len]
            data.append(row)

        df = pd.DataFrame(data, columns=["도로명주소", "관리기관명칭", "위도", "경도", "주소길이 15이상"])

        # 경도에 따라 데이터프레임을 오름차순으로 정렬합니다.
        # 동쪽에 가까운 순서로.
        df2 = df.sort_values(by="경도", ascending=False)

        return df, df2
    else:
        return None, None










