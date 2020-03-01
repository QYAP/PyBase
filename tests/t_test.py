class FinalClassProperty(type):
	"""
	通过元类继承，赋予类属性不可修改特性
	"""

	def __init__(self, *args, **kwargs):
		super(FinalClassProperty, self).__init__(*args, **kwargs)

	def __setattr__(self, name, value):
		if name in self.__dict__ or name in dir(self):
			pass
		else:
			super().__setattr__(name, value)


class FinalProperty(metaclass=FinalClassProperty):
	"""
	通过继承，赋予类和实例属性不可修改特性
	"""

	def __init__(self, *args, **kwargs):
		super(FinalProperty, self).__init__(*args, **kwargs)

	def __setattr__(self, name, value):
		if name in self.__dict__ or name in dir(self):
			pass
		else:
			super().__setattr__(name, value)


class BaseExcp(Exception):
	DEFAULT_COLOR = True
	ERROR_CODE = 123
	MSG = "456"

	@property
	def msg(self):
		return self.MSG

	@msg.setter
	def msg(self, msg: str):
		self.MSG = msg

	@property
	def code(self):
		return self.ERROR_CODE

	@code.setter
	def code(self, error_code: int):
		self.ERROR_CODE = error_code

	def __str__(self):
		exce_info = sys.exc_info()
		e_type = exce_info[0]
		e_traceback = exce_info[2]
		msg_base = '[CODE:%d]%s' % (self.code, type(self)) + \
		           ('' if self.msg is None else ',%s' % self.msg) + '\n'
		msg_traceback = '|-%s\tLine:%d [FuncName:%s]\n' % \
		                (
			                e_traceback.tb_frame.f_code.co_filename,
			                e_traceback.tb_lineno,
			                e_traceback.tb_frame.f_code.co_name
		                )
		t_countor = 0
		while e_traceback.tb_next:
			t_countor += 1
			e_traceback = e_traceback.tb_next
			msg_traceback += '\t' * t_countor
			msg_traceback += '|-%s\tLine:%d [FuncName:%s]\n' % \
			                 (
				                 e_traceback.tb_frame.f_code.co_filename,
				                 e_traceback.tb_lineno,
				                 e_traceback.tb_frame.f_code.co_name
			                 )
		if self.DEFAULT_COLOR:
			assembly_msg = '\033[1;31m' + msg_base + '\033[1;33m' + msg_traceback + '\033[0m'
		else:
			assembly_msg = msg_base + msg_traceback
		return assembly_msg

	@classmethod
	def new_excp(cls, name_code_msg: tuple):
		return type(name_code_msg[0], (cls,),
		            {"ERROR_CODE": name_code_msg[1], "MSG": name_code_msg[2]})


class ArgVldExcp(FinalProperty, BaseExcp):
	missing_error = BaseExcp.new_excp(("miss", 40301, '''function args missing error!!!'''))
	a = 1

	@classmethod
	def test(cls):
		print(super(cls))

	def __getattribute__(self, item):
		return type("123", (BaseExcp,), {"ERROR_CODE": 1, "MSG": 1})

# try:
# 	raise ArgVldExcp.missing_error
# except Exception as e:
# 	print(e)
# # ArgVldExcp.a=2
# # print(ArgVldExcp.a)
# # ArgVldExcp.b=2
# # print(ArgVldExcp.b)
# # print(id(ArgVldExcp().a))
# # print(id(ArgVldExcp().a))
# # print(id(ArgVldExcp().a))
# # print(id(BaseExcp))
# # print(id(BaseExcp))
