# encoding: utf-8
# Author    : AP
# Datetime  : 2019/7/29 17:05
# Project   : RBAC

from .base_exception import BaseExcp


class DBExcp(BaseExcp):
	pass


class ArgVldExcp(BaseExcp):
	constraint_err = (
		40300,
		'''Decorator arguments error!!!'''
	)
	missing_err = (
		40301,
		'''function args missing error!!!'''
	)
	type_err = (
		40304,
		'''function args type error!!!'''
	)
	range_err = (
		40306,
		'''function args range error!!!'''
	)
	enum_err = (
		40307,
		'''function args enumeration error!!!'''
	)
	default_err = (
		40308,
		'''function args default error!!!arg is not default value.'''
	)
