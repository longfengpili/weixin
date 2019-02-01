'''
@Author: longfengpili
@Date: 2019-01-26 15:20:30
@LastEditTime: 2019-02-01 09:00:23
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
    notenum = db.IntField(default=0)
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
        'ordering': 'nickname'
    }
    myname = db.StringField(required=True)
    username = db.StringField(required=True)
    nickname = db.StringField()
    remarkname = db.StringField()
    sex = db.IntField()
    signature = db.StringField()
    province = db.StringField()
    city = db.StringField()
    notenum = db.IntField(default=0)
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


class Message(db.Document):
    meta = {
        'collection': 'Message',
    }
    message = db.StringField(required=True)
    create_at = db.DateTimeField(default=datetime.now)
    update_at = db.DateTimeField(default=datetime.now)

    def __str__(self):
        return f'<Msg:{self.message[:10]}>'
    
    def __repr__(self):
        return f'<Msg:{self.message[:10]}>'


