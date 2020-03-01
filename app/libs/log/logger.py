# encoding: utf-8
# Author    : AP
# Datetime  : 2019/7/22 15:26
# Project   : RBAC

# 日志记录等级
# 日志输出流（文件、数据库）
# 日志分割功能
# 错误通知
# flask插件
# config_defined:notice,color,format

import time
import threading

from flask import Flask

from ..build_in.singleton import singleton
from .cache import LocalCache
from .export import MongoExport, ConsoleExport

# 可配置项
# 日志是否分类、分割（分割单位 周，天，日，小时）存储
# 日志缓存方式（loacal，redis）
# 日志持久化方式（mongodb、mysql、text-file）
# 持久化资源定位符
# 控制台日志输出等级
# 日志格式化配置

# 顔色对应 致命-紫 错误-红 警告-黄 告知-绿 调试-黑
from .helper import LoggerLevel, LoggerColor, LoggerRecord


@singleton
class Logger():
	color = LoggerColor
	level = LoggerLevel

	cache_handle = None
	export_handles = []

	def __init__(self):
		self.__init(self.DEFAULT_CONFIG)

	def __init(self, config: dict):

		# 初始化缓存句柄
		if config["cache_type"] == 0:
			self.cache_handle = LocalCache
			self.cache_handle.config(config["cache_size"])

		# 初始化输出句柄
		self.export_handles.clear()
		for exp_i in config["exports"]:
			this_handle = None
			if exp_i['type'] == 0:
				this_handle = \
					ConsoleExport(exp_i['url'], exp_i['id'], exp_i['log_level'], exp_i['classify'], exp_i['segment'])
			elif exp_i['type'] == 1:
				pass
			elif exp_i['type'] == 2:
				this_handle = \
					MongoExport(exp_i['url'], exp_i['id'], exp_i['log_level'], exp_i['classify'], exp_i['segment'])
			elif exp_i['type'] == 3:
				pass
			self.export_handles.append(this_handle)

	def config(self, cache_type: int = None, cache_size: int = None, exports: list = None):
		config = {}
		if cache_type is None:
			config["cache_type"] = self.DEFAULT_CONFIG.get("cache_type")
		if cache_size is None:
			config["cache_size"] = self.DEFAULT_CONFIG.get("cache_size")
		if exports is None:
			config["exports"] = self.DEFAULT_CONFIG.get("exports")
		self.__init(config)

	def config_from_flask(self, flask_app: Flask):
		self.__init(flask_app.config)

	def log(self, msg, color, level):
		# msg + level + color + timestamp + thread
		timestamp = int(time.time() * 1000)
		thread_name = str(threading.currentThread().ident)
		path = ''
		lineno = 0
		rec = LoggerRecord(msg, level, color, timestamp, thread_name, path, lineno)

		# 报警
		if level > 30:
			self.police(rec)

		# 记录
		cache_res = self.cache_handle.auto_push(rec)
		if cache_res is not None:
			for handle_i in self.export_handles:
				handle_i.write(cache_res)

	def police(self, msg):
		pass

	# 日志分类
	def info(self, msg):
		self.log(msg, self.color.info, self.level.info)

	def debug(self, msg):
		self.log(msg, self.color.debug, self.level.debug)

	def warn(self, msg):
		self.log(msg, self.color.warn, self.level.warn)

	def error(self, msg):
		self.log(msg, self.color.error, self.level.error)

	def critical(self, msg):
		self.log(msg, self.color.critical, self.level.critical)
		# self.police()

	def auto(self, msg):
		self.log(msg, self.color.debug, self.level.debug)

	DEFAULT_CONFIG = {
		"cache_type": 0,  # 0 is local,1 is redis
		"cache_size": -1,
		"exports": [
			{
				# terminal of output,0 is console,1 is file,2 is mongodb,3 is mysql
				'type': 0,
				# equal or greater than log_leve will be outputed(debug 10 info 20 warn 30 error 40 critical 50)
				'log_level': 0,
				"classify": False,
				"segment": None,  # none,month,day,hourse,minute
				"url": "",
				"id": ""
			},
			{
				# terminal of output,0 is console,1 is file,2 is mongodb,3 is mysql
				'type': 2,
				# equal or greater than log_leve will be outputed(debug 10 info 20 warn 30 error 40 critical 50)
				'log_level': 0,
				"classify": True,
				"segment": None,  # none,month,day,hourse,minute
				"url": "mongodb://192.168.0.199:27017",
				"id": "RBAC_log"
			}
		]
	}
