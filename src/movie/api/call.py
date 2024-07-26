import requests

def gen_url(dt="20120101"):
    base_url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json"
    key = "1465c9786034ed67b7f78c1dcdea48f6"
    url = f"{base_url}?key={key}&targetDt={dt}"
    
    return url

def req():
    print("request")

