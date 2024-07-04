import json

def get_mt_cookie_token(cookie):
    try:
        return from_cookie_get_data(cookie,"token=")
    except :
        return ""
    
def get_mt_cookie_acctId(cookie):
    try:
        return from_cookie_get_data(cookie,"acctId=")
    except :
        return ""


def get_mt_cookie_bsid(cookie):
    try:
        return from_cookie_get_data(cookie,"bsid=")
    except:
        return ""
    

def get_mt_cookie_wmPoiId(cookie):
    try:
        info = from_cookie_get_data(cookie,"set_info=")
        infoJson = json.loads(info)
        return str(infoJson["wmPoiId"])
    except :
        return ""
    


def from_cookie_get_data(cookie,name):
    pairs = cookie.split(";")
    for pair in pairs:
        if name in pair:
            value = pair.split("=")[1]
            return str(value)
    return ""

