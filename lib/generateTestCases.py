# -*- coding: utf-8 -*-
# author:liucong

import os
from lib import readexceldata
from lib.log import logger

datapath = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data')

# 类的实例、被测试的接口名称、测试数据文件名、测试数据表单名称
def __generateTestCases(instanse, inerfaceName, tesDataName, sheetName):
    file = os.path.join(datapath, tesDataName)
    data_list = readexceldata.excel_to_list(file, sheetName)
    for i in range(len(data_list)):
        setattr(instanse, 'test_' + inerfaceName + '_%s' % (str(data_list[i]["tc_num"])),
            instanse.getTestFunc(data_list[i]))
        func_name = 'test_' + inerfaceName + '_%s' % (str(data_list[i]["tc_num"]))
        func_attr = getattr(instanse, func_name)
        func_attr.__doc__ = str(data_list[i]["tc_name"])
