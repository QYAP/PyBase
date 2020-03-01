# encoding: utf-8
# Author    : AP
# Datetime  : 2019/8/27 11:03
# Project   : RBAC


from collections import deque

t_d = deque(maxlen=10)
print(t_d.maxlen)
for i in range(10):
	t_d.append(1)
print(t_d)
t_d.append(2)
t_d.append(2)
print(t_d)
t_c = t_d.copy()
print(t_c)
t_d.clear()
print(t_d)
t_c.pop()
print(t_c)
t_c.popleft()
print(t_c)
print(t_c.count())
