# !/usr/bin/python3
# encoding:utf-8
'''
@File    :   singleton.py
@Time    :   2020/03/01 17:52:25
@Author  :   AP 
@Version :   1.0
@Contact :   1792970452@qq.com
@WebSite :   ***
'''

# Start typing your code from here


# 实现单例模式
def singleton(cls):
    instance = cls()
    cls.__call__ = lambda self: instance
    return instance

