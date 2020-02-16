"""
copy：只复制深层对象的引用
deepcopy：复制深层对象的本身

"""

import copy
a = [1,2,["a", "b"]]

c = copy.copy(a) # 浅拷贝
d = copy.deepcopy(a) #深拷贝

print(c)
print(d)

a.append(5)
print("---------")
print(a)
print(c)
print(d)

a[2][1] = "x"
print("---------")
print(a)
print(c)
print(d)