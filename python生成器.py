"""
Python生成器（迭代）

yield

"""

def myGenerator():
    list = [1,2,3,4,5,6,7,8]
    for num in list:
        yield num

for num in myGenerator():
    print(num, end=" ")
print()

nestedList = [[1,2],[2,3],[3,4]]

def Gen(nestedList): # 二维变为一维
    for sublist in nestedList:
        for element in sublist:
            yield element

for num in Gen(nestedList):
    print(num, end=" ")
print()
# 迭代将多维转为一维列表
def enumList(nestedList):
    try:
        for sublist in nestedList:
            for element in enumList(sublist):
                yield element
    except TypeError:
        yield nestedList

listn = [1,[2,[3,4],[5,6,7],[8,[8,8,[8,8]]]],[9,10]]

listn2 = list(enumList(listn))
print(listn2)
print(" ".join(map(str,listn2)))