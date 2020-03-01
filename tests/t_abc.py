# encoding: utf-8
# Author    : AP
# Datetime  : 2019/8/16 17:53
# Project   : RBAC

import abc
from collections import deque


class CacheIface(metaclass=abc.ABCMeta):
	DEFAULT_SIZE = 1000
	handle = None

	@abc.abstractmethod
	def config(cls, size: int = None): pass

	@abc.abstractmethod
	def get_size(cls): pass

	@abc.abstractmethod
	def full(cls) -> bool: pass

	@abc.abstractmethod
	def auto_push(cls, obj) -> list or None: pass

	@abc.abstractmethod
	def copy(cls): pass

	@abc.abstractmethod
	def clear(cls): pass

	@abc.abstractmethod
	def dump(cls) -> list: pass

	@abc.abstractmethod
	def push(cls, value) -> bool: pass


# class RedisCache(CacheIface):
# 	pass


def singleton(cls):
	instance = cls()
	instance.call = lambda: instance
	return instance


class LocalCache(CacheIface):
	DEFAULT_SIZE = 1000
	handle = None

	@classmethod
	def config(cls, size: int = None):
		if isinstance(size, int) and size > 0:
			cls.handle = deque(maxlen=size)
		else:
			cls.handle = deque(maxlen=cls.DEFAULT_SIZE)

	@classmethod
	def get_size(cls):
		return len(cls.handle)

	@classmethod
	def full(cls) -> bool:
		if len(cls.handle) == cls.handle.maxlen:
			return True
		else:
			return False

	@classmethod
	def auto_push(cls, obj) -> list or None:
		if cls.full():
			res = cls.dump()
			cls.push(obj)
			return res
		else:
			cls.push(obj)
			return None

	@classmethod
	def copy(cls):
		return list(cls.handle.copy())

	@classmethod
	def clear(cls):
		cls.handle.clear()
		return True

	@classmethod
	def dump(cls) -> list:
		res = cls.copy()
		cls.clear()
		return res

	@classmethod
	def push(cls, value) -> bool:
		cls.handle.append(value)
		return True

LocalCache.config(3)
for i in range(4):
	if LocalCache.auto_push(i) is None:
		print("***Normal push")
		print(LocalCache.handle)
	else:
		print("##############")
		print(LocalCache.handle)