import requests
import os    # used for get key method to conceal key value, attain key value from server
import pandas as pd

def get_key():
    key = os.getenv('MOVIE_API_KEY')
    return key

def gen_url(dt="20120101"):
    base_url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json"
    key = get_key()   
    url = f"{base_url}?key={key}&targetDt={dt}"
    
    return url

def req(dt="20120101"):
    url = gen_url(dt)
    r = requests.get(url)
    # 200이 오면 정상, 400이 오면 문제 생김
    code = r.status_code
    data = r.json()
    
    return code, data

def req2list(load_dt='20120101') -> list:
    _, data = req(load_dt)
    l = data['boxOfficeResult']['dailyBoxOfficeList']
    
    return l

def list2df(load_dt='20120101'):
    l = req2list(load_dt)
    df = pd.DataFrame(l)

    return df

def save2df(load_dt='20120101'):
    df = list2df(load_dt)
    # df에 load_dt column 추가 (조회 일자 YYYYMMDD 형식으로)
    df['load_dt'] = load_dt #pd.Timestamp.today().strftime('%Y%m%d')
    print(df.head(5))
    # 아래 파일 저장시 load_dt 기본으로 partitioning
    df.to_parquet('~/tmp/test_parquet', partition_cols=['load_dt'])

    return df

def apply_type2df(load_dt="20120101", path="~/tmp/test_parquet"):
    df = pd.read_parquet(f'{path}/load_dt={load_dt}')
    # df['rnum'] = pd.to_numeric(df['rnum'])
    num_cols = ['rnum', 'rank', 'rankInten', 'salesAmt', 'audiCnt', 'audiAcc', 'scrnCnt', 'showCnt', 'salesShare', 'salesInten', 'salesChange', 'audiInten', 'audiChange']

    for c in num_cols:
        df[c] = pd.to_numeric(df[c])   #string => numeric(float), which enables to derive statistics like avg, std ...
        # df[c] = df[c].apply(pd.to_numeric)
    return df

def echo(yaho):
    return yaho
