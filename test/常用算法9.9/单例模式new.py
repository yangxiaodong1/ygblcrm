# Author : July  Yang 
'''1 使用new'''


class Singleton(object):
    def __new__(cls, *args, **kwargs):
        # if hasattr(cls,'_instance'):
        #     cls._instance = super(Singleton,cls).__new__(cls,*args,**kwargs)
        # return cls._instance
        if hasattr(cls,'_instance'):
            cls._instance = super(Singleton, cls).__new__(cls,*args,**kwargs)

        return cls._instance