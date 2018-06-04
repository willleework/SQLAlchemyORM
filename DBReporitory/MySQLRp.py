#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'this is mysql sqlslchemy orm demo'

__author__ = 'will lee'
##########################################
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

'''
class MySQLRp(object):
    def __init__(self, user, password, server, dbname, encoding):
        self.__engine = create_engine('"mysql+mysqlconnector://{0}:{1}@{2}/{3}"'.format(user, password, server, dbname),encoding='utf-8', echo=True)
        self.__base = declarative_base()
    #连接属性
    @property
    def Base(self):
        return self.__base
'''
engine = create_engine("mysql+mysqlconnector://root:ggcjdss2017@localhost/dbtest",encoding='utf-8', echo=True)
Base = declarative_base()

#MySQL数据库辅助类
class MySQLHelper(object):
    def __init__(self, engine):
        self.__engine = engine

    #数据库连接
    @property
    def Session(self):
        Session_class = sessionmaker(bind=engine)  # 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
        return Session_class()  # 生成session实例

