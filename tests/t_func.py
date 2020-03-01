# encoding: utf-8
# Author    : AP
# Datetime  : 2019/7/23 17:43
# # Project   : RBAC
# def test(a, b, c, d, *args, **kwargs):
# 	print(a, b, c, d)
# 	print(args)
# 	print(kwargs)
#
#
# # test(1,2,3,4,5,q=6)
#
# def f(a=1, b=2, c=3):
# 	print(locals())  # 在函数内获取
# function
#
# f(1, c=3, b=2)
# print(f.__defaults__)
# print(f.__code__.co_varnames)

# #使用inspect模块，简单方便
# #
# # import inspectinspect.getargspec(f)
# #
# # #使用f的内置方法#获取默认值,如果参数名没有默认值则不在其中：
import inspect


# print(inspect.getargspec())
#
# print(f.__defaults__)  # 使用__code__#总参数个数
#
# print(f.__code__.co_argcount)  # 总参数名
#
# print(f.__code__.co_varnames)
#
# f()

# print(locals())

# def decorator(f):
# 	def executor(*args, **kwargs):
# 		print(args, kwargs)
# 		f(*args, **kwargs)
# 	return executor
#
# # @decorator
# # def f(a, b=2, c=3):
# # 	print(locals())  # 在函数内获取
# # # f(1)
# # print(f.__defaults__)  # 使用__code__#总参数个数
# # print(f.__code__.co_argcount)
# # print(f.__code__.co_varnames)
