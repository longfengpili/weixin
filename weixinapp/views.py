'''
@Author: longfengpili
@Date: 2019-01-26 15:20:30
@LastEditTime: 2019-01-26 15:42:15
@coding: 
#!/usr/bin/env python
# -*- coding:utf-8 -*-
@github: https://github.com/longfengpili
'''

from weixinapp import app
from .admin import admin
from .user import user
from .weixin import weixin


app.register_blueprint(admin,url_prefix='/admin')
app.register_blueprint(user,url_prefix='/user')
app.register_blueprint(weixin,url_prefix='/weixin')