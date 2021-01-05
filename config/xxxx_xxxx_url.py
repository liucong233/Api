# -*- coding: utf-8 -*

import requests
import json
from lib.log import logger
from lib.jenkins_data import config

# 环境判断
def get_ZHRS_base_url(case):
    env = config['env']
    if env == "beta":
        base_url = ""
    if env == "staging":
        base_url = ""
    return base_url


manulife_login = ""


def get_xxx_token(username, password, case, deviceNum):
    # params="login="+phone+"&"+"password="+password
    params = {"username": username, "password": password, "deviceNum": deviceNum}
    logger.info(params)
    headers = {"Content-Type": "application/json"}
    requests.packages.urllib3.disable_warnings()
    res = requests.post(url=get_ZHRS_base_url(case) + manulife_login, json=params, headers=headers, verify=False)
    # logger.info(res.text)
    # bs = BeautifulSoup(res.text, "lxml")  # 将请求结果传递给bs构造对象
    # res1= bs.script.text[21:][:-6]##对象中获取script的字符串，并进行截取
    res2 = json.loads(res.text)  ##转化为json
    result = res2['result']['token']
    logger.info(result)
    return result


if __name__ == '__main__':
    phone = "13700000000"
    # password="123456"
    # params="login="+phone+"&"+"password="+password
    # res = requests.post(url="", params=params)
    # result=res.json()
    # print(result['access_token'])
    # register("phone")
    # token=get_hmsc_token("15816816809","123456","azure")
    # token=get_hmsc_admin_token("root","root","azure")
    # print(token)
    # get_situ_token("010","01010101","beta","00010")
