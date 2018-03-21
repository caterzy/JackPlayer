# This Python file uses the following encoding: utf-8
__author__ = 'JackRao'


import functools

def log(text1,text2):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text1,func.__name__))
            func(*args,**kw)
            print('%s %s():' % (text2,func.__name__))
        return wrapper
    return decorator

@log("begin","end")
def now():
    print("2016-8-5");

now();