# encoding: utf-8
# Author    : AP
# Datetime  : 2019/8/27 18:21
# Project   : RBAC
from collections import deque

t_d = deque(maxlen=10)
for i in range(10):
	t_d.append(i)
print(t_d)

t_d.pop()
t_d.append(10)
print(t_d)

t_c = t_d.copy()
print(t_c)

t_d.popleft()
print(t_d)
print(t_c)

print("********************")
t_c2 = list(t_d.copy())
t_d.clear()
print(t_d)
print(t_c2)


print(t_d.maxlen)
print(len(t_d))