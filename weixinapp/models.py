'''
@Author: longfengpili
@Date: 2019-01-26 15:20:30
@LastEditTime: 2019-01-27 13:42:06
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
    myname = db.StringField(required=True)
    username = db.StringField(required=True)
    nickname = db.StringField()
    remarkname = db.StringField()
    sex = db.IntField()
    signature = db.StringField()
    province = db.StringField()
    city = db.StringField()
    create_at = db.DateTimeField(default=datetime.now)
    update_at = db.DateTimeField(default=datetime.now)

    def __str__(self):
        if self.remarkname == '':
            self.remarkname = self.nickname
        return f'<【{self.myname}】Friend:{self.remarkname}>'
    
    def __repr__(self):
        if self.remarkname == '':
            self.remarkname = self.nickname
        return f'<【{self.myname}】Friend:{self.remarkname}>'

class User(db.Document):
    meta = {
        'collection': 'user',
    }
    myname = db.StringField(required=True)
    username = db.StringField(required=True)
    nickname = db.StringField()
    remarkname = db.StringField()
    sex = db.IntField()
    signature = db.StringField()
    province = db.StringField()
    city = db.StringField()
    create_at = db.DateTimeField(default=datetime.now)
    update_at = db.DateTimeField(default=datetime.now)

    def __str__(self):
        if self.remarkname == '':
            self.remarkname = self.nickname
        return f'<【{self.myname}】user:{self.remarkname}>'
    
    def __repr__(self):
        if self.remarkname == '':
            self.remarkname = self.nickname
        return f'<【{self.myname}】user:{self.remarkname}>'



