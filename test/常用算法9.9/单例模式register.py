# Author : July  Yang 
'''1 使用new'''


def singlento(cls,*args,**kwargs):
    instance = {}
    def _single():
        if cls not in instance:
            instance[cls] = cls(*args,**kwargs)
        return instance[cls]
    return _single()

@singlento
class As(object):
    a = 2


