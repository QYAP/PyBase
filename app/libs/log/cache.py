# encoding: utf-8
# Author    : AP
# Datetime  : 2019/8/16 17:53
# Project   : RBAC

import abc
from collections import deque

from ..build_in.singleton import singleton


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


@singleton
class LocalCache(CacheIface):
	DEFAULT_SIZE = 1000
	EFFECT = True
	handle = None

	@classmethod
	def config(cls, size: int = None):
		if isinstance(size, int) and size >= 0:
			cls.handle = deque(maxlen=size)
		else:
			cls.handle = deque(maxlen=cls.DEFAULT_SIZE)

		if isinstance(size, int) and size <= 0:
			cls.EFFECT = False
		else:
			cls.EFFECT = True

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
	def auto_push(cls, rec) -> list or None:
		if not cls.EFFECT:
			return [rec]
		else:
			if cls.full():

				res = cls.dump()
				cls.push(rec)
				return res
			else:
				cls.push(rec)
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
#

# class RedisCache(CacheIface):
# 	pass
