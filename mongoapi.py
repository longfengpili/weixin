#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
sys.path.append('..')
import mysetting

import pymongo

class mongoapi():
    def __init__(self):
        self.host = mysetting.ip
        self.port = mysetting.mongo_port
        self.username = mysetting.mongo_account
        self.pwd = mysetting.mongo_pwd

    def client(self):
        client = pymongo.MongoClient(host=self.host,port=self.port)
        client.admin.authenticate(name=self.username,password=self.pwd)

        return client


