# !/usr/bin/python3
# encoding:utf-8
'''
@File    :   __init__.py
@Time    :   2020/03/12 20:41:55
@Author  :   AP 
@Version :   1.0
@Contact :   1792970452@qq.com
@WebSite :   ***
'''
# Start typing your code from here

from inspect import getmro

from ...build_in.reflect import reflect_attr


class BaseError(Exception):
    CODE = 0

    def __init__(self, msg: str = "", *args, **kwargs):
        self.msg = msg
        super().__init__(*args, **kwargs)

    def __str__(self):
        formater = "[CODE:%(code)d]%(error_info)s%(msg)s"
        data = {"code": self.CODE, "error_info": "", "msg": " >>> %s" % self.msg if self.msg else self.msg}
        # 获取继承树并获取拼接所有字符串属性值
        for item in reversed(getmro(type(self))[0:-1]):
            attributes = reflect_attr(item)
            for k, v in attributes.items():
                if isinstance(v, str):
                    data["error_info"] += " >>> " + v
        return formater % data
