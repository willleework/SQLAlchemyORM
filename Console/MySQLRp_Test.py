#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'this is mysql sqlslchemy orm demo'

__author__ = 'will lee'
##########################################
from DBReporitory.MySQLRp import engine, MySQLHelper
from Models.Model import *

#测试数据连接
def MysqlQueryTest():
    mysql = MySQLHelper(engine)
    my_user = mysql.Session.query(User).filter_by(name="alex").first()

    print(my_user.id, my_user.name, my_user.password)

MysqlQueryTest()