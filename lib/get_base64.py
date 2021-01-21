# -*- coding: utf-8 -*-
# author:liucong


from lib.log import logger
import base64
import os

##获取文件的base64
def get_file_base64(basedir,fileName):

    path = basedir + fileName
    with open(path, 'rb') as f:
        base64_data = base64.b64encode(f.read())
        s = base64_data.decode()
        logger.info('data:image/jpeg;base64,%s'%s)
    return s

if __name__ == '__main__':
    basedir = os.path.abspath(os.path.dirname(os.getcwd())) + "/data/"
    get_file_base64(basedir,"XXX.jpg")
