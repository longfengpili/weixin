'''
@Author: longfengpili
@Date: 2019-01-26 15:20:50
@LastEditTime: 2019-01-26 17:10:26
@coding: 
#!/usr/bin/env python
# -*- coding:utf-8 -*-
@github: https://github.com/longfengpili
'''

import sys
sys.path.append('..')
import mysetting

from mysetting import ip,mongo_port,mongo_account,mongo_pwd

MONGODB_SETTINGS = {
    'host' : ip,
    'port' : 27017,
    'username' : mongo_account,
    'password' : mongo_pwd,
    'db' : 'weixin'
}

SECRET_KEY = '123456'


