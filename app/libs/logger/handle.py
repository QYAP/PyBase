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

from collections import deque


from ..utils.console_color import ConsoleColor

from .recorder import Recorder


class BaseHandle():
    Name = "BaseHandle"
    DEFAULT_BUFFER = 0
    '''
        01，handle 过滤器
        02，handle 格式化
        03，handle 染色
        04，进入buffer队列
        05，输出到终端
    '''
    def __init__(self, handle_id: str, filter_level: int, buffer_size: int, *args, **kwargs):
        self.handle_id = handle_id
        self.filter_level = filter_level
        self.buffer_size = buffer_size
        if buffer_size >= 0:
            self.buffer = deque(maxlen=self.buffer_size)
        else:
            self.buffer = deque(maxlen=self.DEFAULT_BUFFER)

    def _filter(self, recorder: Recorder):
        if recorder.level >= self.filter_level:
            return True
        else:
            return False

    def _color(self):
        pass

    def _copy(self):
        return list(self.buffer.copy())

    def _clear(self):
        self.buffer.clear()
        return True

    def _dump(self):
        res = self._copy()
        self._clear()
        return res

    def _push(self, value):
        self.buffer.append(value)

    def _full(self):
        if len(self.buffer) == self.buffer.maxlen:
            return True
        else:
            return False

    def _auto_push(self, rec: Recorder):
        if self.buffer.maxlen > 0:
            if self.buffer._full():
                recs = self.buffer._dump()
                self.buffer._push(rec)
                return recs
            else:
                self.buffer._push(rec)
                return []
        else:
            return [rec]

    def _export(self, recs: list, color_func: object = None):
        pass

    def work(self, recorder: Recorder):
        if self._filter(recorder):
            self._export(self._auto_push(recorder), self._color)


class ConsoleHandle(BaseHandle):
    NAME = "ConsoleHandle"
    DEFAULT_BUFFER = 0

    def __init__(self, handle_id: str, filter_level: str, buffer_size: int = None, color_or_not: bool = True, *args, **kwargs):
        if buffer_size is None:
            buffer_size = self.DEFAULT_BUFFER
        self.color_or_not = color_or_not
        super().__init__(handle_id, filter_level, buffer_size, *args, **kwargs)

    def _color(self, recs: list):
        if self.color_or_not:
            for item in recs:
                item.format_msg = ConsoleColor.dye(item.format_msg, ConsoleColor.get_color(item.color))

    def _export(self, recs: list, color_func: object = None):
        if color_func:
            color_func(recs)
        for item in recs:
            print(item.format_msg)
