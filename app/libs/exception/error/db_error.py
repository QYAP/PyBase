# !/usr/bin/python3
# encoding:utf-8
'''
@File    :   db_error.py
@Time    :   2020/03/12 20:40:36
@Author  :   AP 
@Version :   1.0
@Contact :   1792970452@qq.com
@WebSite :   ***
'''
# Start typing your code from here

from . import BaseError


class DBError(BaseError):
    CODE = 10000
    DESP = "DB ERROR"


class DuplicateError(DBError):
    CODE = 10001
    DESP = "ID duplicate!!!"
