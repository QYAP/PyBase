# !/usr/bin/python3
# encoding:utf-8
'''
@File    :   recorder.py
@Time    :   2020/03/05 22:03:36
@Author  :   AP 
@Version :   1.0
@Contact :   1792970452@qq.com
@WebSite :   ***
'''
import os
import threading


# Start typing your code from here
class Recorder():
    '''
        args:
            message:日志信息
            level_name:日志登记名
            format:格式
            color:颜色

            lineno:代码行
            func_name:方法名
            module:模块名
            file_name:文件名
            path:文件路径
            
            thread_id:线程id
            thread_name:线程名
            process_id:进程id

    '''
    def __init__(self, msg: str, level: str, format: str, color: str):

        self.message = msg
        self.level = level
        self.level_name = level
        self.format = str
        self.color_name = color

        # 获取代码位置信息
        code_location = self.get_code_location
        self.line_no = code_location.get("line_no")
        self.func_name = code_location.get("func_name")
        self.module = code_location.get("module")
        self.file_name = code_location.get("file_name")
        self.path = code_location.get("path")

        # 获取进程线程信息
        t = threading.currentThread()
        self.thread_id = t.ident
        self.thread_name = t.getName()
        self.process_id = os.getpid()

        self.format_msg = "test_format_msg"

    def get_code_location(self):
        return {
            "line_no": 1,
            "func_name": "test_func_name",
            "module": "test_module",
            "file_name": "test_file_name",
            "path": "test_path"
        }

    def json(self):
        return {}
