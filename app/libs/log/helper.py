# encoding: utf-8
# Author    : AP
# Datetime  : 2019/9/9 17:25
# Project   : RBAC
from .text_proc import Color
from ..build_in.simple_enum import SimpleEnum


class LoggerLevel(SimpleEnum):
	debug = 10
	info = 20
	warn = 30
	error = 40
	critical = 50


class LoggerColor(SimpleEnum):
	debug = Color.BLACK
	info = Color.GREEN
	warn = Color.YELLOW
	error = Color.LIGHT_RED
	critical = Color.LIGHT_PURPLE


class LoggerRecord():

	def __init__(self, original_msg: str, level: int, color: str, timestamp: int, thread_name: str, path: str,
	             lineno: int):
		self.__original_msg = original_msg
		self.__timestamp = timestamp

		self.__level = level
		self.__thread_name = thread_name
		self.__color = color
		self.__path = path
		self.__lineno = lineno

		self.__msg = Color.color(Color.clean(original_msg), self.__color)

	msg = property(lambda self: self.__msg)
	original_msg = property(lambda self: self.__original_msg)
	timestamp = property(lambda self: self.__timestamp)
	level = property(lambda self: self.__level)
	thread_name = property(lambda self: self.__thread_name)
	color = property(lambda self: self.__color)
	path = property(lambda self: self.__path)
	lineno = property(lambda self: self.__lineno)

	def dump_json(self) -> dict:
		res = {
			"message": self.msg,
			"detail": {
				'timestamp': self.timestamp,
				"original_msg": self.original_msg,
				"level": self.level,
				"color": self.color,
				"context": {
					"thread_name": self.thread_name,
					"path": self.path,
					'lineno': self.lineno
				}
			}
		}
		return res

	FORMAT_JSON = {
		"message": str,
		"detail": {
			'timestamp': int,
			"original_msg": str,
			"level": int,
			"color": str,
			"context": {
				"thread_name": str,
				"path": str,
				'lineno': str
			}
		}
	}
