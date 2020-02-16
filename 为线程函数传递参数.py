import threading

def func1(s,fun):
    print("正在运行线程函数func1")
    fun(s)

def ff(s):
    print(f"ff输出了{s}")

thread = threading.Thread(target=func1, args=("hello world",ff))
thread.start()
