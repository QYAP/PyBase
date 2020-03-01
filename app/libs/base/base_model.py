# encoding: utf-8
# Author    : AP
# Datetime  : 2019/7/22 14:43
# Project   : RBAC
import time

from bson import ObjectId


def getter(property_name):
	def getter(self):
		return getattr(self, property_name)

	return getter


def setter(property_name):
	def setter(self, property_value):
		setattr(self, property_name, property_value)

	return setter


class BaseModel():
	DAO = None

	@classmethod
	def save(cls, info: dict):
		info.update({"created_timestamp": time.time() * 1000})
		cls.DAO.insert_one(info)

	@classmethod
	def delete(cls, info: dict):
		filter = {'_id': ObjectId(info.pop('_id'))}
		cls.DAO.delete_one(filter)

	@classmethod
	def update(cls, info: dict):
		if 'created_timestamp' in info.keys:
			info.pop('created_timestamp')
		info.update({"lastest_updated_timestamp": time.time() * 1000})
		filter = {'_id': ObjectId(info.pop('_id'))}
		cls.DAO.update_one(filter, {'$set': info})

	@classmethod
	def find_many(cls, page: int = -1, size: int = -1, sort: list = None, filter: dict = None,
	              fuzzy_search: dict = None, iterator_mode=False, *args, **kwargs):
		"""
		todo fuzzy_search filter 两者可能在 or 和 and 冲突
		fuzzy_search intersect
		:param page:
		:param size:
		:param sort:
		:param filter:
		:param fuzzy_search:
		:param iterator_mode:
		:param args:
		:param kwargs:
		:return:
		"""
		# 处理过滤条件
		filter_assembly = {
			"$or": [],
			"$and": []
		}

		# 模糊搜索
		if isinstance(fuzzy_search, dict):
			if fuzzy_search.get("intersect", False):
				fuzzy_search.pop("intersect", None)
				for field_name, search_str in fuzzy_search.items():
					if not (isinstance(search_str, str) and isinstance(field_name, str)):
						continue
					filter_assembly['$and'].append({field_name: {"$regex": "[.]*" + search_str + "[.]*"}})
			else:
				fuzzy_search.pop("intersect", None)
				for field_name, search_str in fuzzy_search.items():
					if not (isinstance(search_str, str) and isinstance(field_name, str)):
						continue
					filter_assembly['$or'].append({field_name: {"$regex": "[.]*" + search_str + "[.]*"}})
		# 收尾处理过滤条件
		if len(filter_assembly['$or']) == 0:
			filter_assembly.pop('$or')
		if len(filter_assembly['$and']) == 0:
			filter_assembly.pop('$and')

		# 限制
		if isinstance(filter, dict):
			filter_assembly.update(filter)

		# 获取记录总数
		num = cls.DAO.find(filter_assembly, *args, **kwargs).count()

		# 分页
		skip = (page - 1) * size

		# 处理不分页
		if page < 0 or size < 0:
			recs = cls.DAO.find(filter_assembly, sort=sort, *args, **kwargs)
		else:
			recs = cls.DAO.find(filter_assembly, sort=sort, skip=skip, limit=size, *args, **kwargs)

		if iterator_mode:
			return num, recs
		else:
			return num, list(recs)

	@classmethod
	def find(cls, filter: dict):
		return cls.DAO.find_one(filter)

	@classmethod
	def find_option(cls, option_key: str, filter: dict):
		pass

	@classmethod
	def json_adjust(cls, rep_data):
		pass

	@classmethod
	def format_legal(cls, req_data):
		pass
