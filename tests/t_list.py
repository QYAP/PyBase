# encoding: utf-8
# Author    : AP
# Datetime  : 2019/7/24 17:42
# Project   : RBAC
t = [1, 2, 3, 4, 5, 6, '1','1']
# print(t.index('18'))
t.clear()
print(t)
t={}
for i in range(10):
	t.update({str(i):[]})
t['1'].append(123)
print(t)