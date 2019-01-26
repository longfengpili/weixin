'''
@Author: longfengpili
@Date: 2019-01-26 15:20:30
@LastEditTime: 2019-01-26 16:22:24
@coding: 
#!/usr/bin/env python
# -*- coding:utf-8 -*-
@github: https://github.com/longfengpili
'''
#!/usr/bin/env python3
#-*- coding:utf-8 -*-

from flask import Blueprint, render_template, request, flash, redirect, url_for,make_response,send_file


admin = Blueprint('admin',__name__)

