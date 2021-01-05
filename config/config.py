# -*- coding: utf-8 -*-
# author:liucong

 # -*- coding:utf-8 -*-
 # author:liucaiyu
import os
import logging
import pymysql


# 邮件配置
sender = ''  # 发送方1
receiver = ''
emailusername = ''  # 登陆邮箱的用户名
emailpassword = ''  # 登陆邮箱的授权码
server = 'smtp.exmail.qq.com'  # smtp服务器2017/6/22

# 数据目录
datapath = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data')


# os.path.abspath(path) #返回绝对路径
# os.path.basename(path) #返回文件名
# os.path.dirname(path) #返回文件路径
# os.path.join(path1[, path2[, ...]])  #把目录和文件                                                                                              名合成一个路径


# 项目配置
basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 日志配置
logpath = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'log')
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%y-%m-%d %H:%M',
                    filename=os.path.join(logpath, 'log.txt'),
                    filemode='a')





