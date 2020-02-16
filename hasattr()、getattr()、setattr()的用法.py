"""
hasattr：可以判断一个对象是否包含某个属性
getattr：可以获取对象中某一个属性的值
setattr：可以设置对象中某一个属性的值

"""

class Person:
    def __init__(self):
        self.name = "wmb"
        self.age = 19
    def show(self):
        print(self.__dict__.items())
        print(vars(self).items())# 同上
        print(" ".join("%s:%s"% item for item in vars(self).items()))


person = Person()

if hasattr(person, "name"):
    print("存在name属性")

setattr(person, "sex", "男")
setattr(person, "name", "wwb")

if hasattr(person, "sex"):
    print("存在sex属性")

person.show()