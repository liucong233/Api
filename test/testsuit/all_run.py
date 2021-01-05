# -*- coding: utf-8 -*-
# author:liucong

import unittest
import os.path
import sys
from unittestreport import TestRunner
from lib.jenkins_data import config

basedir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(basedir)

# 执行的项目文件目录
pro = config['pro']
email_data = config['email']
email = str(email_data).split(',')
if len(email) > 1:
    email = list(email)
title = config['title']

# 执行文件地址
suite_case = unittest.defaultTestLoader.discover(basedir + '/test/testcase/XXXX/' + pro, pattern='*.py')

'''BeautifulReport风格将templates改为2即可'''
runner = TestRunner(suite_case,
                    filename="report.html",
                    report_dir='../../report',
                    title=title,
                    tester='测试组',
                    desc='接口自动化测试报告',
                    templates=1
                    )
runner.run()
runner.send_email(host="smtp.exmail.qq.com",
                  port=465,
                  user="XXXX@XXXX.com",
                  password="XXXX",
                  to_addrs=email)
