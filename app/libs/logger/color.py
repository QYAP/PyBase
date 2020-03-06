# encoding: utf-8
# Author    : AP
# Datetime  : 2019/7/22 16:06
# Project   : RBAC

import re

# from ..build_in import singleton


# @singleton
class Color():
    NOTSET = None
    RED = '0;31m'  # 红（用于error）
    GREEN = '0;32m'  # 绿（用于info）
    YELLOW = '0;33m'  # 黄（用于warn）

    BLUE = '0;34m'  # 蓝
    PURPLE = '0;35m'  # 紫

    GREY = '0;37m'  # 灰
    BLACK = '0;30m'  # 黑
    WHITE = '1;37m'  # 白

    LIGHT_RED = '1;31m'  # 亮红
    LIGHT_GREEN = '1;32m'  # 亮绿
    LIGHT_YELLOW = '1;33m'  # 亮绿

    LIGHT_BLUE = '1;34m'  # 亮蓝
    LIGHT_PURPLE = '1;35m'  # 亮紫

    # console颜色显示格式前后缀
    COLOR_START = '\033['
    COLOR_EDN = '\033[0m'

    @classmethod
    def dye(cls, target_str: str, color_type: str) -> str:
        if color_type is None:
            return target_str
        else:
            return '%s%s%s%s' % (cls.COLOR_START, color_type, target_str, cls.COLOR_EDN)

    @staticmethod
    def clean(target_str: str) -> str:
        return re.sub('\\033\[[\s\S]*?m{1}', '', target_str)

    @classmethod
    def get_name_by_color(cls, color_name: str):
        color_to_name = {
            cls.NOTSET: "NOTSET",
            cls.RED: 'RED',
            cls.GREEN: 'GREEN',
            cls.YELLOW: 'YELLOW',
            cls.BLUE: 'BLUE',
            cls.PURPLE: 'PURPLE',
            cls.GREY: 'GREY',
            cls.BLACK: 'BLACK',
            cls.WHITE: 'WHITE',
            cls.LIGHT_RED: 'LIGHT_RED',
            cls.LIGHT_GREEN: 'LIGHT_GREEN',
            cls.LIGHT_YELLOW: 'LIGHT_YELLOW',
            cls.LIGHT_BLUE: 'LIGHT_BLUE',
            cls.LIGHT_PURPLE: 'LIGHT_PURPLE'
        }
        return color_to_name.get(color_name)

    @classmethod
    def get_color_by_name(cls, color_name: str):
        name_to_color = {
            "NOTSET": cls.NOTSET,
            'RED': cls.RED,
            'GREEN': cls.GREEN,
            'YELLOW': cls.YELLOW,
            'BLUE': cls.BLUE,
            'PURPLE': cls.PURPLE,
            'GREY': cls.GREY,
            'BLACK': cls.BLACK,
            'WHITE': cls.WHITE,
            'LIGHT_RED': cls.LIGHT_RED,
            'LIGHT_GREEN': cls.LIGHT_GREEN,
            'LIGHT_YELLOW': cls.LIGHT_YELLOW,
            'LIGHT_BLUE': cls.LIGHT_BLUE,
            'LIGHT_PURPLE': cls.LIGHT_PURPLE
        }
        return name_to_color.get(color_name)


print(Color.dye("test", Color.BLUE))
