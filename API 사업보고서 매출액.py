import pandas as pd
import requests



df = pd.read_excel('KBS 상장폐지 요건 강화에 따른 영향 시뮬레이션_20250602.xlsx',dtype=str,sheet_name='상장사 목록')
url = '	https://opendart.fss.or.kr/api/fnlttSinglAcnt.json'

# 매출액 저장할 df
res_df = pd.DataFrame(columns=['rcept_no', 'reprt_code', 'bsns_year', 'corp_code', 'stock_code',
       'fs_div', 'fs_nm', 'sj_div', 'sj_nm', 'account_nm', 'thstrm_nm',
       'thstrm_dt', 'thstrm_amount', 'frmtrm_nm', 'frmtrm_dt', 'frmtrm_amount',
       'bfefrmtrm_nm', 'bfefrmtrm_dt', 'bfefrmtrm_amount', 'ord', 'currency'])

# corp_code = "00118965"
nodata_list = []    # 매출액을 불러올 수 없는 고유번호
total = len(df['고유번호'])

# api를 이용해 매출액 호출해줄 loop
for idx, corp_code in enumerate(df['고유번호']):
    print(idx,"/",total," - ", round(100*idx/total,1) ) # 진행상황 출력문

    # 고유번호가 없는 경우에는 건너뛰기
    if corp_code == "-":
        continue

    # api 호출을 위한 매개변수
    params = {"crtfc_key": api_key,
          "corp_code": str(corp_code).replace(" " , ""),
          "bsns_year": "2024",      # 2024년
          "reprt_code": "11011"}    # 사업보고서

    # api 호출(request)
    res = requests.get(url, params=params)
    data = res.json()   # json데이터를 dictionary 변환

    # 불러온 데이터가 없으면 건너뛰기
    if data['message'] == '조회된 데이타가 없습니다.':
        nodata_list.append(corp_code)
        continue

    # dictionary를 df로 변환
    tmp_df = pd.DataFrame(data['list'])
    res_df = pd.concat([res_df, tmp_df])    # df로 변환한 후 결과 df에 추가

res_df.to_excel('상장사 24년 결산 매출액.xlsx',index=False)