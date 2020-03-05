# !/usr/bin/python3
# encoding:utf-8
'''
@File    :   __init__.py
@Time    :   2020/03/02 18:27:18
@Author  :   AP 
@Version :   1.0
@Contact :   1792970452@qq.com
@WebSite :   ***
'''

# Start typing your code from here
# from .color import Color
from ..build_in import singleton
'''
    filter_level: notset 0 debug 10 info 20 warn 30 error 40 critical 50 
    config = {
        "Logger_id": str,
        "level": int,
        "color": {
            "notset": str,
            "debug": str,
            "info": str,
            "warn": str,
            "error": str,
            "fatal": str
        },
        "format": str,
        "buffer_size"：int,
        "handles": [
            {
                "handle_model": ConsoleHandle,
                "handle_id": str,
                "filter_level": int,
                "color_or_not": bool,
                "buffer_size": int
            },
            {
                "handle_model": FileHandle,
                "handle_id": str,
                "filter_level": int,
                "color_or_not": bool,
                "buffer_size": int,
                "auto_clean_cycle": int,    # 单位为天
                "dir_layer": int,   # 0,1,2 分别表示没有文件文件夹，单层文件夹，两层文件夹（年月、日）
                "file_granularity": str,    # day、hour
                "path": str  # 文件夹路径
            }
        ]
    },
    format:
        %(name)s                 
        %(levelname)s       
        %(lineno)d   
        %(thread)d          
        %(threadName)s      
        %(process)d         
        %(message)s    
        %(pathname)s        
        %(filename)s        
        %(module)s 
        %(funcName)s         
    '''


@singleton
class Factory():
    '''
        01,校验config以及不全缺省默认配置
        02,检查或者生成logge 实例id
        03,注册logger实例到登记容器中
        04,生成logger实例并返回
    '''
    def __init__(self):
        super().__init__()

    def _validate(self):
        pass

    def _generate_logger_id(self):
        pass

    def _register_logger(self):
        pass

    def log_out(self):
        pass

    def new(self, config: dict):
        logger_id = config.get("Logger_id")
        color = config.get("color")
        formater = config.get("format")
        global_filter = config.get("level")
        handles = config.get("handles")
        self.validate()
        return Logger(logger_id, color, formater, global_filter, handles)


class Logger():
    '''
        01, 全局过滤器过滤
        02，获取format item属性值
        03，组成recorder
        03, handles-distributer 分发recorder

    '''
    def __init__(self, logger_id: str, color_config: dict, formater: dict, global_filter: int, handle_configs: list):
        self.id = logger_id
        self.color = color_config
        self.formater = formater
        self.handles = []
        for item in handle_configs:
            pass

    def _global_filter(self):
        pass

    def _generate_recorder(self):
        pass

    def _dispatcher(self):
        pass

    def info(self, msg: str):
        pass

    def debug(self, msg: str):
        pass

    def warn(self, msg: str):
        pass

    def error(self, msg: str):
        pass

    def fatal(self, msg: str):
        pass

    def destroy(self):
        pass


class Recorder():
    '''
        args:

    '''
    pass


class BaseHandle():
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
