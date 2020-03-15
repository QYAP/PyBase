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
from flask import Flask, jsonify

from app.libs.logger import Factory
from app.libs.exception.error.db_error import DBError, DuplicateError

# from app.libs.args_validator.flask_plus_in import args_validator
# from app.libs.args_validator.__type import Type, Number
# from app.libs.args_validator import Required, Default
app = Flask(__name__)


class InvalidUsage(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv


@app.errorhandler(Exception)
def handle_invalid_usage(error):
    print(DBError())
    print(DuplicateError("Mongodb"))
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


config = {"formater": "message:%(message)s,path:%(path)s,lineno:%(line_no)d"}
logger = Factory.new(config)


@app.route("/hello-world", methods=["GET", "POST"])
# @args_validator(rule={"a": Number, Required("b"): Type(str), Default("c"): int}, redundant_max_num=0)
def hello_world():
    # logger.debug("Hello World!!!")
    # logger.error("error")
    raise InvalidUsage('This view is gone', status_code=410)
    return 'Hello World!'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
