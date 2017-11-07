#2017-11-02
#by Lyy
import httplib
#import json
#import authenticate
import get_ip
#import os
#import sys

def login_account_shut_wifi():
    print 'shut wifi start'
    login_wifi = httplib.HTTPSConnection('www.loocha.com.cn', 8443)
    headers = {"Authorization": "Basic MTc3NjYwODU4MzY6MTAxMDA5MDI=",
               "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 6.0; XT1575 Build/MPHS24.49-18.3)",
               "Connection": "Keep-Alive" }
    login_wifi.request('GET', '/login', '', headers)
    httpres = login_wifi.getresponse()
    print httpres.reason
    if httpres.reason=='OK':
        shutdown_wifi()


def shutdown_wifi():
    print 'begain to shutdown wifi'
    login_wifi = httplib.HTTPSConnection('wifi.loocha.cn', 443)
    headers = {"Authorization": "Basic MTc3NjYwODU4MzY6MTAxMDA5MDI=",
               "Content-Type": " application/x-www-form-urlencoded",
               "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 6.0; XT1575 Build/MPHS24.49-18.3)",
               "Connection": "Keep-Alive", "Accept-Encoding": "gzip", 'Content-Length': '0'}
    ip=get_ip.get_host_ip()
    login_wifi.request('DELETE', '/3849698/wifi/kickoff?wanip='+ip+'&brasip=58.213.239.3', '', headers)
    httpres = login_wifi.getresponse()
    print 'wifi has shuting down'
    print httpres.reason
    #print httpres.read()
