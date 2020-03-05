# !/usr/bin/python3
# encoding:utf-8
'''
@File    :   handle.py
@Time    :   2020/03/05 21:32:45
@Author  :   AP 
@Version :   1.0
@Contact :   1792970452@qq.com
@WebSite :   ***
'''
# Start typing your code from here


class BaseHandle():
    Name = "BaseHandle"
    '''
        01，handle 过滤器
        02，handle 格式化
        03，handle 染色
        04，进入buffer队列
        05，输出到终端
    '''
    def _filter(self):
        pass

    def _format(self):
        pass

    def _color(self):
        pass

    def _buffer(self):
        pass

    def _export(self):
        pass

    def work(self):
        pass


class ConsoleHandle(BaseHandle):
    NAME = "ConsoleHandle"
