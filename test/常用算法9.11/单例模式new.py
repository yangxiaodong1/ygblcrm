# Author : July  Yang 
'''1 使用new'''


class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,'_instance'):
            cls._instance = super(Singleton, self).__new__(cls,*args,**kwargs)
        return cls._instance