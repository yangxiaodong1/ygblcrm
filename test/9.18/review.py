# Author : July  Yang 

# f = open('a.py','rb')
# for line in f:
#     print(line)
#
# f = open('b.txt','wb+')
#
# for i in range(0,9):
#     f.write(i)

# def calc(n):
#     print(n)
#     if int(n / 2) >0:
#         return calc(int( n / 2))
#     print('---',n)
#
# calc(10)
# a = '{"a":1,"b":2}'
# b = eval(a)
# print(b)
# print(type(b))

# import time
# def bar():
#     time.sleep(10)
#     print('pp')
# def test(func):
#     print(func)
#     return func
# Bar=test(bar)
# bar()

# print(i*2 for i in range(3))
#
# a = (i*2 for i in range(3))
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())
#
# def gen():
#     yield 5
#     yield 'Hello'
#     yield 'oo'
#
# for i in gen():
#     print(i)
# 判断是不是可迭代对象
# from collections import Iterable
# print(isinstance('',Iterable))

# 内置函数排序
# a = {'a':1,'b':9,'c':3}
#
# print(sorted(a.items()))
# print(sorted(a.items(),key=lambda x:x[1]))
# zip是拼接方法
import json
# 将字典转化为字符串
a = {'a':1,'b':2}
b = json.dumps(a)
print(type(b))
# 序列化 json.dumps()
#反序列化 json.loads()

# 添加到环境变量去，sys.path.append()BASE_DIR