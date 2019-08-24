import binascii
import requests
import json
import time
import hashlib

server = "133.130.124.62/xaxby37yp"
def login(user, passwd):
    ts = int(time.time())
    data = passwd + str(ts)
    m = hashlib.sha1()
    m.update(data.encode())
    s =  m.hexdigest()
    params={
        "name":user,
        "ts": ts,
        "key": s
	}
    url="http://%s/login"%(server)
    resp = requests.post(url, data=params)
    print(resp.text)
    r = resp.json()
    if r["r"] is True:
        return r["token"]
    else:
        return None

def xorgon_sign(username, token, os):
    url="https://gecko.snssdk.com/gecko/server/package/106906/stats?a=1&b=2&c=3";
    body="325444632D16899C25aF7f4fC5D25269";
    cookies="install_id=61111111117; qh[360]=1";
    sessionid=""
    ts = 1554966927
    request_url="http://%s/dysign"%(server)
    requests_body={
        "user":username,
        "token":token,
        "os":os,
        "version":750,
        "ts":ts,
        "url":url,
        "X-SS-STUB":body,
        "cookies":cookies,
        "sessionid":sessionid
    }
    body_data = json.dumps(requests_body)
    print(body_data)
    resp = requests.post(request_url, data=body_data.encode("utf-8"))
    print(resp.text)

if __name__=="__main__":
    username = "xxx"
    passwd = "xxxx"

    token = login(username,passwd)
    print(token)
    xorgon_sign(username, token, "android")
