# !/usr/bin/python3
# encoding:utf-8
'''
@File    :   manager.py
@Time    :   2020/02/26 03:47:04
@Author  :   AP 
@Version :   1.0
@Contact :   1792970452@qq.com
@WebSite :   ***
'''
import logging
# Start typing your code from here
from flask import Flask
# from app.libs.args_validator.flask_plus_in import args_validator
# from app.libs.args_validator.__type import Type, Number
# from app.libs.args_validator import Required, Default
app = Flask(__name__)

# def arg_validator(func):
#     def inner(*args, **kwargs):

#         return func(*args, **kwargs)

#     inner.__name__ = func.__name__
#     return inner

# def arg_validator(func):
#     @wraps(func)
#     def inner(*args,**kwargs):
#         print("***********")
#         ret=func(*args,**kwargs)
#         return ret
#     return inner


@app.route("/hello-world", methods=["GET", "POST"])
# @args_validator(rule={"a": Number, Required("b"): Type(str), "c": int}, redundant_max_num=0)
def hello_world():
    return "Hello World!!!"


@app.route("/test", methods=["GET", "POST"])
# @arg_validator
def test():
    return "Test!!!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
