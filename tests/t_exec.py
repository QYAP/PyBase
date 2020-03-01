import sys


class MetaExcp(type):
	def __init__(self, *args, **kwargs):
		super(MetaExcp, self).__init__(*args, **kwargs)

	def __setattr__(self, name, value):
		if name in self.__dict__ or name in dir(self):
			pass
		else:
			super().__setattr__(name, value)

	def __getattribute__(self, item):

		cls_name = super().__name__
		var_name = item
		var_value = super().__getattribute__(item)
		try:
			err_instance = self(var_value[0], var_value[1], cls_name, var_name)
		except:
			raise RootExcp
		return err_instance


class BaseExcp(Exception, metaclass=MetaExcp):
	DEFAULT_COLOR = True

	def __init__(self, err_code: int, msg: str, first_err_name: str = None, second_err_name: str = None, *args,
	             **kwargs):
		super(BaseExcp, self).__init__(*args, **kwargs)
		self.__code = err_code
		self.__msg = msg
		self.__first_err_name = first_err_name
		self.__second_err_name = second_err_name

	@property
	def code(self):
		return self.__code

	@code.setter
	def code(self, error_code: int):
		self.__code = error_code

	@property
	def msg(self):
		return self.__msg

	@msg.setter
	def msg(self, msg: str):
		self.__msg = msg

	@property
	def first_err_name(self):
		return self.__first_err_name

	@first_err_name.setter
	def first_err_name(self, first_err_name: str):
		self.__first_err_name = first_err_name

	@property
	def second_err_name(self):
		return self.__second_err_name

	@second_err_name.setter
	def second_err_name(self, second_err_name: str):
		self.__second_err_name = second_err_name

	def assemble(self, *args):
		super().__setattr__("_BaseExcp__msg", self.msg % tuple(args))
		return self

	def __setattr__(self, name, value):
		if name in self.__dict__ or name in dir(self):
			pass
		else:
			super().__setattr__(name, value)

	def __str__(self):
		exce_info = sys.exc_info()
		# e_type = exce_info[0]
		e_traceback = exce_info[2]
		err_name = ("" if self.first_err_name is None else self.first_err_name + " # ") + self.second_err_name
		msg_base = '[CODE:%d] %s' % (self.code, err_name) + ('' if self.msg is None else ' : %s' % self.msg) + '\n'
		msg_traceback = '#|-%s\tLine:%d [FuncName:%s]\n' % \
		                (
			                e_traceback.tb_frame.f_code.co_filename,
			                e_traceback.tb_lineno,
			                e_traceback.tb_frame.f_code.co_name
		                )
		t_countor = 1
		while e_traceback.tb_next:
			t_countor += 1
			e_traceback = e_traceback.tb_next
			msg_traceback += '#' * t_countor
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


class RootExcp(Exception):
	def __str__(self):
		return '\033[1;31m' + \
		       "Self-defined-exception's arg is formal error,it must be tuple!(e,g (10001,'notice  msg'))" + \
		       '\033[0m'


#####


class DBExcp(BaseExcp):
	unique_err = (1001, "the primary key is %s")


def test():
	raise DBExcp.unique_err.assemble("123")


try:
	test()
except Exception as e:
	print(e)
a = DBExcp(1, "11")
a.b = 1
print(a.b)
a.b = 2
print(a.b)
