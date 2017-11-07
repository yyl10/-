
#2017-11-02
#by Lyy

import httplib
import json
import get_ip
def login_accounts():
    print 'get login'
    login_wifi = httplib.HTTPSConnection('www.loocha.com.cn', 8443)
    headers = {"Authorization": "Basic ",
               "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 6.0; XT1575 Build/MPHS24.49-18.3)",
               "Connection": "Keep-Alive","Accept-Encoding": "gzip" }
    login_wifi.request('GET', '/login', '', headers)
    httpres = login_wifi.getresponse()
    if httpres.reason=='OK':
        return get_status()
    else:
        return 0


def get_status():
    print 'get status'
    login_wifi = httplib.HTTPSConnection('wifi.loocha.cn', 443)
    headers = {"Authorization": "Basic ",
               "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 6.0; XT1575 Build/MPHS24.49-18.3)",
               "Connection": "Keep-Alive", "Accept-Encoding": "gzip"}
    login_wifi.request('GET', '/3849698/wifi/status', '', headers)
    httpres = login_wifi.getresponse()
    if httpres.reason=='OK':
        return get_id()
    else:
        return 0

def get_id():
    print 'get id'
    login_wifi = httplib.HTTPSConnection('wifi.loocha.cn', 443)
    headers = {"User-Agent": "Dalvik/2.1.0 (Linux; U; Android 6.0; XT1575 Build/MPHS24.49-18.3)",
               "Connection": "Keep-Alive"}
    ip = get_ip.get_host_ip()
    login_wifi.request('GET', '/0/wifi/qrcode?brasip=58.213.239.3&ulanip='+ip+'&wlanip='+ip, '', headers)
    httpres = login_wifi.getresponse()
    if httpres.reason=="OK":
        data=httpres.read()
        j=json.loads(data)
        HIWF=j['telecomWifiRes']['password']
        password=get_password()
        if password==0:
            return 0
        return wifi_authenticate(HIWF,password)

def get_password():
    print 'get password'
    login_wifi = httplib.HTTPSConnection('wifi.loocha.cn', 443)
    headers = {"Authorization": "Basic ",
               "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 6.0; XT1575 Build/MPHS24.49-18.3)",
               "Connection": "Keep-Alive"}
    login_wifi.request('GET', '/3849698/wifi?server_did=541a0cc7-221d-45d1-bd7d-e74f96df9a72', '', headers)
    httpres = login_wifi.getresponse()
    if httpres.reason!='OK':
        return 0
    data=httpres.read()
    j=json.loads(data)
    password=j['telecomWifiRes']['password']
    return password

def wifi_authenticate(HIWF,password):
    print 'geting authenticate'
    login_wifi = httplib.HTTPSConnection('wifi.loocha.cn', 443)
    headers = {"Authorization": "Basic ",
               "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 6.0; XT1575 Build/MPHS24.49-18.3)",
               "Connection": "Keep-Alive",
               "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6",
               "Content - Type": "application/x-www-form-urlencoded","Content-Length": "0"}
    login_wifi.request('POST', '/3849698/wifi/enable?qrcode='+HIWF+'&code='+password, '', headers)
    httpres = login_wifi.getresponse()
    print httpres.read()
    if httpres.reason!='OK':
        return 0
    else:
        return 1
