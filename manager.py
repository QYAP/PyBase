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
# Start typing your code from here
from flask import Flask

from app.libs.logger import Factory

from app.libs.args_validator.flask_plus_in import args_validator
from app.libs.args_validator.__type import Type, Number
from app.libs.args_validator import Required, Default
app = Flask(__name__)

config = {}
logger = Factory().new({})


@app.route("/hello-world", methods=["GET", "POST"])
@args_validator(rule={"a": Number, Required("b"): Type(str), Default("c"): int}, redundant_max_num=0)
def hello_world():
    logger.debug("Hello World!!!")
    logger.error("error")
    return "Hello World!!!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
