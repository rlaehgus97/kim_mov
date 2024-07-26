import requests
import os    # used for get key method to conceal key value, attain key value from server
#import pandas as pd

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
    
    #print(data)
    return code, data

def req2dataframe():
    _, data = req()
    l = data['boxOfficeResult']['dailyBoxOfficeList']
    return l

print(req2dataframe())
