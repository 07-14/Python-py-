"""
python支持多继承


"""
class Caculator:
    def caculator(self,expression):
        self.value = eval(expression)
        return self.value
    def printResult(self):
        print(f"result:{self.value}")

class MyPrint:
    def print(self,msg):
        print("msg:",msg)
    def printResult(self):
        print(f"结果:{self.value}")

class MyCaculator(Caculator,MyPrint):
    pass
my1 = MyCaculator()
print(my1.caculator("1+3 * 5"))
my1.print("hello")
my1.printResult() #输出result，说明使用的是Caculator中的printResult