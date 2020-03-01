# encoding: utf-8
# Author    : AP
# Datetime  : 2019/8/16 18:04
# Project   : RBAC

import abc

import pymongo

from ..build_in.reflect import reflect_attr
from .helper import LoggerLevel


class ExportIface(metaclass=abc.ABCMeta):
	@abc.abstractmethod
	def init(self, url: str, id: str, level: int, classify: bool, segmentation: bool):
		pass

	@abc.abstractmethod
	def write(self, recs: list) -> bool:
		pass

	@abc.abstractmethod
	def pick_choose(self, recs: list) -> dict:
		pass


class ConsoleExport(ExportIface):
	def __init__(self, *args, **kwargs):
		self.init(*args, **kwargs)

	def init(self, url: str, id: str, level: int, classify: bool, segmentation: bool):
		self.min_level = level

	def write(self, recs: list):
		recs_processed = self.pick_choose(recs)
		for item in recs_processed["list"]:
			print(item.msg)

	def pick_choose(self, recs: list) -> dict:
		# build res dict
		res = {"list": []}

		# filter
		for rec_i in recs:
			if rec_i.level >= self.min_level:
				res["list"].append(rec_i)
		return res


class MongoExport(ExportIface):

	def __init__(self, *args, **kwargs):
		self.init(*args, **kwargs)

	def init(self, url: str, id: str, level: int, classify: bool, segmentation: bool):
		self.db = pymongo.MongoClient(url).get_database(id)

		self.cols = {}
		if classify:
			for log_kind_i in reflect_attr(LoggerLevel).keys():
				self.cols.update({log_kind_i: self.db.get_collection(log_kind_i)})
		self.cols.update({'default': self.db.get_collection('default')})
		self.min_level = level

	def write(self, recs: list):
		recs_processed = self.pick_choose(recs)
		for log_kind, recs_i in recs_processed.items():
			if log_kind in self.cols.keys():
				if len(recs_i) > 0:
					self.cols[log_kind].insert_many(recs_i)
			else:
				self.cols['default'].insert_many(recs_i)

	def pick_choose(self, recs: list) -> dict:
		# build res dict
		res = {}
		for log_kind_i in reflect_attr(LoggerLevel).keys():
			res.update({log_kind_i: []})
		# filter and classify
		for rec_i in recs:
			if rec_i.level >= self.min_level:
				if LoggerLevel(rec_i.level) in res.keys():
					res[LoggerLevel(rec_i.level)].append(rec_i.dump_json())
		return res


class FileExport(ExportIface):
	def __init__(self, *args, **kwargs):
		self.init(*args, **kwargs)

	def init(self, url: str, id: str, level: int, classify: bool, segmentation: bool):
		pass

	def write(self, recs: list):
		pass

	def pick_choose(self, recs: list) -> dict:
		pass
