#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
sys.path.append('..')
import mysetting

import pymongo
import warnings

class mongoapi():
    def __init__(self,dbname,tablename):
        self.host = mysetting.ip
        self.port = mysetting.mongo_port
        self.username = mysetting.mongo_account
        self.pwd = mysetting.mongo_pwd
        self.dbname = dbname
        self.tablename = tablename

    def __client(self):
        client = pymongo.MongoClient(host=self.host,port=self.port)
        client.admin.authenticate(name=self.username,password=self.pwd)

        return client

    def select(self,post,limit=1):
        client = self.__client()
        collection = client[self.dbname][self.tablename]
        result = collection.find(post)
        result = list(result)
        row = len(result)
        
        return row,result[:limit]

    def insert_one(self,post):
        client = self.__client()
        collection = client[self.dbname][self.tablename]
        row,_ = self.select(post)
        if row > 0:
            warnings.warn(f'already exists , not insert!【{post}】')
        else:
            collection.insert_one(post)

    def update_one(self,post,newvalues):
        client = self.__client()
        collection = client[self.dbname][self.tablename]
        row,_ = self.select(post)
        newvalues = {"$set":newvalues}
        if row > 1:
            warnings.warn(f'【{row}】 may update ，please check you post')
        else:
            collection.update_one(post,newvalues)

    def delete_one(self,post,many=False):
        client = self.__client()
        collection = client[self.dbname][self.tablename]
        row,_ = self.select(post)
        if row > 1:
            warnings.warn(f'【{row}】 may delete ，please check you post')
        else:
            collection.delete_one(post)
