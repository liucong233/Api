# -*- coding: utf-8 -*-
# author:liucong

import unittest
import requests
from lib.generateTestCases import __generateTestCases
from lib.log import logger
from config import situ_ZHRS_url


##中宏APP-业务员端发送短信验证码
class ApiManulifeAccountActivate(unittest.TestCase):
    def setUp(self):
        logger.info("*" * 80)

    def getTest(self,data):
        logger.info("***************网关请求中XXXX账号激活开始****************")
        case = data['case']
        num=data['tc_num']
        name=data['tc_name']
        code=int(data['code'])
        username = data['username']
        phoneNum = data['phoneNum']
        validateCode = data['validateCode']
        password=data['password']
        logger.info(num + "_" + name + "_" + case)
        headers={"Content-Type":"application/json","X-Device":"Xiaomi/MI 9/10"}
        params = {"username":username,"phoneNum":phoneNum,"validateCode":validateCode,"password":password}
        logger.info(params)
        requests.packages.urllib3.disable_warnings()
        res = requests.post(url=situ_ZHRS_url.get_ZHRS_base_url(case)+situ_ZHRS_url.manulife_account_activate,headers=headers, json=params,verify=False)
        logger.info(situ_ZHRS_url.get_ZHRS_base_url(case)+situ_ZHRS_url.manulife_account_activate)
        logger.info(res.text)
        result = res.json()
        logger.info("*******返回数据： " + str(result))
        self.assertEqual(result['code'],code)
        logger.info("****************网关请求中宏APP-业务员端账号激活结束****************")

    @staticmethod
    def getTestFunc(arg1):
        def func(self):
            self.getTest(arg1)
        return func

    def tearDown(self):
        logger.info("*" * 80)

__generateTestCases(ApiManulifeAccountActivate, "manulife_account_activate",  "api_XXXX.xlsx", "账号激活")
