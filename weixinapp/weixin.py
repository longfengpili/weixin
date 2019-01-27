'''
@Author: longfengpili
@Date: 2019-01-27 08:43:40
@LastEditTime: 2019-01-27 14:52:22
@coding: 
#!/usr/bin/env python
# -*- coding:utf-8 -*-
@github: https://github.com/longfengpili
'''
from flask import Blueprint, render_template, request, flash, redirect, url_for,make_response,send_file
from .models import Friend
import itchat

weixin = Blueprint('weixin',__name__)


@weixin.route('/login')
def login():
    qr_path = './weixinapp/static/weixin/QRcode/weixin.png'
    uuid = itchat.get_QRuuid()
    qrStorage = itchat.get_QR(uuid=uuid,enableCmdQR=True)
    with open(qr_path, 'wb') as f:
        f.write(qrStorage.getvalue())
    # print(uuid)
    return render_template('weixin/login.html',uuid=uuid,weixin='weixin',note='请使用微信扫描二维码进行登陆！')
    
@weixin.route('/check_login')
def check_login():
    uuid = request.args.get('uuid',None)
    status = itchat.check_login(uuid)
    if status == '200':
        web_init = itchat.web_init()
        return redirect(url_for('weixin.show'))
    elif status == '201':
        return render_template('weixin/login.html',uuid=uuid,weixin='weixin',note='请在手机上确认登陆！')
    else:
        return render_template('weixin/login.html',uuid=uuid,weixin='weixin',note='请使用微信扫描二维码进行登陆！')

def get_friends():
    friends = itchat.get_friends(True)
    myname = friends[0]['NickName']
    friend = Friend.objects(myname=myname).first()
    if not friend:
        for friend in friends:
            username = friend.get('UserName',None)
            nickname = friend.get('NickName',None)
            remarkname = friend.get('RemarkName',None)
            sex = friend.get('Sex',None)
            signature = friend.get('Signature',None)
            province = friend.get('Province',None)
            city = friend.get('City',None)
            friend = Friend(myname=myname,username=username,nickname=nickname,remarkname=remarkname,
                                sex=sex,signature=signature,province=province,city=city)
            friend.save()
    
    friends = Friend.objects().all()
    return friends

@weixin.route('/show')  
def show(): 
    new_friends = []
    friends = Friend.objects().all()
    return render_template('weixin/show.html',friends=friends)

    




    
