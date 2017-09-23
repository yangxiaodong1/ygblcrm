# Author : July  Yang 
'''1 使用new'''
class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,"_instance"):
            cls._instance = super(Singleton, cls).__new__(cls,*args,**kwargs)
        return cls._instance

class MyClass(Singleton):
    a=1

one = MyClass()
two = MyClass()

one.a= 5
print(two.a)

'''使用装饰器'''
def single(cls,*args,**kwargs):
    instance = {}
    def _single():
        if cls not in instance:
            instance[cls] = cls(*args,**kwargs)
        return instance[cls]
    return _single
@single
class MyClass2(object):
    a=1






