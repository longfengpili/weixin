'''
@Author: longfengpili
@Date: 2019-01-26 15:20:30
@LastEditTime: 2019-01-28 08:26:12
@coding: 
#!/usr/bin/env python
# -*- coding:utf-8 -*-
@github: https://github.com/longfengpili
'''

__all__ = ['db', 'login_manager']

from flask import Flask, url_for, request, redirect, render_template
from flask_mongoengine import MongoEngine
from datetime import timedelta
app = Flask(__name__)
app.config.from_object('config')
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)
db = MongoEngine()
db.init_app(app)

from flask_login import LoginManager,login_required, logout_user, login_user, current_user

#用户认证
login_manager = LoginManager()

#配置用户认证信息
login_manager.init_app(app)
#认证加密程度
login_manager.session_protection = 'strong'
#登陆认证的处理视图
login_manager.login_view = 'admin.login'
#登陆提示信息
login_manager.login_message = u'请登录'
login_manager.login_message_category = 'info'


from weixinapp import models
from weixinapp import views
