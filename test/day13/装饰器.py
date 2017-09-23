# Author : July  Yang 

import time
def timer(func):
    def deco(*args,**kwargs):
        start_time=time.time()
        a=func(*args,**kwargs)
        stop_time=time.time()
        print("the func runing time is:%s" %(stop_time-start_time))
        return a
    return deco
@timer
def test1():
    time.sleep(1)
    print("in the test1")
@timer
def test2(name,age):
    time.sleep(1)
    print("in the test2",name,age)
test1()
test2("July",20)






