'''
@Author: longfengpili
@Date: 2019-01-26 15:20:30
@LastEditTime: 2019-01-26 18:11:11
@coding: 
#!/usr/bin/env python
# -*- coding:utf-8 -*-
@github: https://github.com/longfengpili
'''

from weixinapp import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

class Friend(db.Document):
    meta = {
        'collection': 'friend',
    }
    name = db.StringField(required=True)
    f_username = db.StringField(required=True)
    f_nickname = db.StringField()
    f_remarkname = db.StringField()
    f_sex = db.StringField()
    f_signature = db.StringField()
    f_province = db.StringField()
    f_city = db.StringField()
    create_at = db.DateTimeField(default=datetime.now)

    def __repr__(self):
        return f'<【{self.name}】Friend[{self.f_remarkname}]>'



