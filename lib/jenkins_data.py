# -*- coding: utf-8 -*-
# author:liucong

import sys

def get_config():
    config_info = {

    }
    #Jenkins参数
    if len(sys.argv) > 1:
        config_info['pro'] = sys.argv[1]
        config_info['env'] = sys.argv[2]
        config_info['email'] = sys.argv[3]
        config_info['title'] = sys.argv[4]
    else:
        #本地兼容
        config_info['pro'] = 'xxxx/'
        config_info['env'] = 'staging'
        config_info['email'] = 'xxxx@xxxx.com,xxxx@xxxxx.com'
        config_info['title'] = '本地调试'
    return config_info


config = get_config()