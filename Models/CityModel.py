#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'this is mysql sqlslchemy orm demo'

__author__ = 'will lee'
##########################################
from sqlalchemy import Column, Integer, String
from DBReporitory.MySQLRp import Base

#用户表
class User(Base):
    __tablename__ = 'user' #表名
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    password = Column(String(64))