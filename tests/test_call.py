from movie.api.call import gen_url, req, get_key, req2list, list2df, save2df, echo
import pandas as pd 

def test_get_key():
    key = get_key()
    assert key

def test_gen_url():
    url = gen_url()

    assert "http" in url
    assert "kobis" in url

def test_req():
    code, data = req()
    assert code == 200
    
def test_req2list():
    l = req2list()
    assert len(l) > 0
    v = l[0]
    assert 'rnum' in v.keys()
    #assert type(req2dataframe()) is list
    assert v['rnum'] == '1'

def test_list2df():
    df = list2df()
    print(df)
    print(type(df))
    assert isinstance(df, pd.DataFrame)
    assert 'rnum' in df.columns
    assert 'openDt' in df.columns
    assert 'salesAmt' in df.columns
    assert 'audiCnt' in df.columns

def test_save2df():
    df = save2df()
    print(type(df))
    assert isinstance(df, pd.DataFrame)
    assert 'load_dt' in df.columns
   
def test_echo():
    r = echo("hello")
    assert r == "hello"
