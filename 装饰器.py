from functools import wraps
def log(label):
    def decorate(func):
        @wraps(func)
        def _warp(*args, **kwargs):
            try:
                func(*args, **kwargs)
                print("name",func.__name__)
            except Exception as e:
                print(e.args)
        return _warp
    return decorate

@log("")
def add(a, b, c):
    print(a+b+c)

add(1,2,3)
def add1(a, b, c):
    print(a+b+c)
add(2,3,4)


"""

@staticmethod和classmethod的用法和区别
都是用来生命静态方法的。类名.方法名


"""
class Myclass:
    bar = 1
    def __init__(self):
        self.number = 20
    def process(self):
        # print(bar)会报错
        print(Myclass.bar)
    @staticmethod
    def staticprocess():
        print("staticprocess:",Myclass.bar)
    @classmethod
    def classprocess(cls):
        print("classmethod:", cls.bar)
        print(cls)
        print(cls().number)
        cls().process()

# Myclass.process()# 会报错
Myclass.staticprocess()
Myclass.classprocess()
Myclass.bar = 2
Myclass.staticprocess()

from types import MethodType,FunctionType
print(type(Myclass().process).__name__ == "method")