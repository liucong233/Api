# -*- coding: utf-8 -*-
# author:liucong

import time,random
from datetime import datetime

#随机生成cookies
def cookies():
    character = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    first_cookie = []
    for i in range(33):
        first_cookie.append(random.choice(character))
    first_cookie = ''.join(first_cookie)

    timeArray = int(time.time())
    last_cookie = str(timeArray)

    cookie = 'SERVERID=' + first_cookie + '|' + last_cookie + '|' + last_cookie
    return cookie

#时间戳
def timeStamp_10():
    timeArray = int(time.time())
    return str(timeArray)

def timeStamp_13():
    timeArray = int(time.time()*1000)
    return str(timeArray)

def timeTime():
    dt = datetime.now()
    times = dt.strftime("%Y-%m-%d %H:%M:%S")
    print(times)
    return times

if __name__ == '__main__':
    timeTime()