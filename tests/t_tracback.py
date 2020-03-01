# encoding: utf-8
# Author    : AP
# Datetime  : 2019/8/22 18:07
# Project   : RBAC
import traceback
import sys
import datetime


def get_head_info():
	try:
		raise Exception
	except:
		f = sys.exc_info()[2].tb_frame.f_back
	return '%s, %s, %s, %s, ' % (str(datetime.now()), f.f_code.co_filename, f.f_code.co_name, str(f.f_lineno))
