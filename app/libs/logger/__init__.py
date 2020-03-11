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
from ..build_in.singleton import singleton

from .level import Level
from .recorder import Recorder
from .handle import ConsoleHandle
'''
    filter_level: notset 0 debug 10 info 20 warn 30 error 40 critical 50 
    config = {
        "logger_id": str,
        "level": int,
        "formater": str,
        "color": {
            "NOTSET": str,
            "DEBUG": str,
            "INFO": str,
            "WARN": str,
            "ERROR": str,
            "FATAL": str
        },
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


class LogColor():
    NOTSET = None
    RED = 'RED'  # 红
    GREEN = 'GREEN'  # 绿
    YELLOW = 'YELLOW'  # 黄

    BLUE = 'BLUE'  # 蓝
    PURPLE = 'PURPLE'  # 紫

    GREY = 'GREY'  # 灰
    BLACK = 'BLACK'  # 黑
    WHITE = 'WHITE'  # 白

    LIGHT_RED = 'LIGHT_RED'  # 亮红
    LIGHT_GREEN = 'LIGHT_GREEN'  # 亮绿
    LIGHT_YELLOW = 'LIGHT_YELLOW'  # 亮绿

    LIGHT_BLUE = 'LIGHT_BLUE'  # 亮蓝
    LIGHT_PURPLE = 'LIGHT_PURPLE'  # 亮紫


class Logger():
    '''
        00，检查并标准化handles
        01, 全局过滤器过滤
        02，获取format item属性值
        03，组成recorder
        03, handles-distributer 分发recorder

    '''
    def __init__(self, logger_id: str, level: int, color: dict, formater: dict, handles: list, *args, **kwargs):
        self.id = logger_id
        self.color = color
        self.global_filter = level
        self.formater = formater
        self.handle_container = {}
        for h_config_i in handles:
            self.handle_container[h_config_i["handle_id"]] = h_config_i["handle_model"](**h_config_i)

    def __global_filter(self, level: int):
        if level < self.global_filter:
            return False
        else:
            return True

    def __generate_recorder(self, level: int, msg: str):
        return Recorder(msg, level, self.formater, self.color.get(Level.get_name(level)))

    def __dispatcher(self, recorder: Recorder):
        for h_name in self.handle_container.keys():
            self.handle_container[h_name].work(recorder)

    def __log(self, level: int, msg: str):
        if self.__global_filter(level):
            recorder = self.__generate_recorder(level, msg)
            self.__dispatcher(recorder)

    def info(self, msg: str):
        self.__log(Level.INFO, msg)

    def debug(self, msg: str):
        self.__log(Level.DEBUG, msg)

    def warn(self, msg: str):
        self.__log(Level.WARN, msg)

    def error(self, msg: str):
        self.__log(Level.ERROR, msg)

    def fatal(self, msg: str):
        self.__log(Level.FATAL, msg)

    def destroy(self):
        Factory.log_out(self)


@singleton
class Factory():
    DEFAULT_LEVEL = Level.NOTSET
    DEFAULT_FROMATER = "%(message)s"
    DEFAULT_COLOR = {
        'NOTSET': LogColor.NOTSET,
        'INFO': LogColor.NOTSET,
        'DEBUG': LogColor.BLUE,
        'WARN': LogColor.YELLOW,
        'ERROR': LogColor.RED,
        'FATAL': LogColor.RED,
    }
    DEFAULT_BUFFER_SIZE = None
    DEFAULT_HANDLES = [{"handle_model": ConsoleHandle}]
    DEFAULT_HANDLE_ID = "%s-%s"

    LOGGER_CONTAINER = {}

    LEGAL_CONFIG_FORMAT = {
        "logger_id": str,
        "level": int,
        "format": str,
        "color": {
            "NOTSET": str,
            "DEBUG": str,
            "INFO": str,
            "WARN": str,
            "ERROR": str,
            "FATAL": str
        },
        "buffer_size": int,
        "handles": list
    }
    LEGAL_HANDLE_CONFIG_FORMAT = [{}]
    '''
        01,校验config以及不全缺省默认配置
        02,检查或者生成logge 实例id
        03,注册logger实例到登记容器中
        04,生成logger实例并返回
    '''
    def __init__(self):
        super().__init__()

    def __validate(self, config: dict):
        '''
            01，参数校验
            02，检查id是否重复
        '''
        pass

    def __generate_logger_id(self):
        return "test_id"

    def __standardizing(self, config: dict):
        '''
            1，检查或生成id
            2，检查或设置默认level
            3，检查或设置默认format
            4，检查或设置默认color
            5，检查或设置默认buffer-size
            6，检查或设置默认handle
        '''
        # 检查并生成logger-id
        if config.get("logger_id"):
            if config["logger_id"] in self.CONTAINER.keys():
                raise Exception("logger-config error,logger-id duplicate!")
        else:
            config["logger_id"] = self.__generate_logger_id()

        # 检查或设置默认level
        if config.get("level"):
            if config["level"] > Level.FATAL:
                raise Exception("logger-config error,level > fatal!")
        else:
            config["level"] = self.DEFAULT_LEVEL

        # 检查或设置默认formater
        if not config.get("formater"):
            config["formater"] = self.DEFAULT_FROMATER

        # 检查或设置默认color
        config["color"] = dict(self.DEFAULT_COLOR, **config.get("color", {}))

        # 检查或设置默认buffer-size
        if not config.get("buffer_size"):
            config["buffer_size"] = None

        # 检查或设置默认handle-config
        if config.get("handles") is None or len(config["handles"]) == 0:
            config["handles"] = self.DEFAULT_HANDLES

        handle_ids = set({})
        for i, h_item in enumerate(config["handles"]):
            # 检查或设置handle-config 默认id
            if not h_item.get("handle_id"):
                h_item["handle_id"] = self.DEFAULT_HANDLE_ID % (h_item["handle_model"].NAME, str(i))
            handle_ids.add(h_item["handle_id"])
            # 检查或设置handle-config filter level
            if h_item.get("filter_level"):
                if h_item.get("filter_level") > Level.FATAL:
                    raise Exception("handle-config error,level > fatal!")
            else:
                h_item["filter_level"] = config["level"]

        # 检查handle-id 重复问题
        if len(handle_ids) != len(config["handles"]):
            raise Exception("handle-config error,id duplicate or use reserved naming format(handle-name + num)")

        return config

    def __register_logger(self, logger: Logger):
        self.LOGGER_CONTAINER[logger.id] = logger
        return logger

    def log_out(self, logger: Logger):
        if self.LOGGER_CONTAINER.pop(logger.id, None):
            return True
        else:
            return False

    def new(self, config: dict):
        # 校验config
        self.__validate(config)
        # 补充并规范化config
        stardard_config = self.__standardizing(config)
        # 生成并注册logger
        return self.__register_logger(Logger(**stardard_config))
