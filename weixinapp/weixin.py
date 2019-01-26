'''
@Author: longfengpili
@Date: 2019-01-26 15:30:56
@LastEditTime: 2019-01-26 18:10:33
@coding: 
#!/usr/bin/env python
# -*- coding:utf-8 -*-
@github: https://github.com/longfengpili
'''
from flask import Blueprint, render_template, request, flash, redirect, url_for,make_response,send_file
from .models import Friend

weixin = Blueprint('weixin',__name__)

@weixin.route('/')
@weixin.route('/index')
def index():
    user = { 'nickname': 'Miguel' } # fake user
    friend = Friend(name='test',f_nickname='test2')
    print(friend.name)
    return render_template("weixin/index.html",
        title = 'Home',
        user = user)
