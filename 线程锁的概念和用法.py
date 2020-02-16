"""
什么是线程锁？
目的是将一段代码锁住，一旦获得锁权限，除非释放线程锁，否则其他任何代码都无法获得锁权限

为什么需要线程锁

由于多线程同时在完成特定的操作时，由于并不是原子操作，所以在完成操作的过程中可能会被打断，去做其他的操作。

可能会产生脏数据

例如，一个线程读取变量n，n初始值为1，然后n++，最后输出n

当访问n++后，被打断，由另外的线程做同样的工作，这时n被加了两次，所以最后n等于2，而不是1

所以说需要给n++操作加上锁变成原子操作，直到结束再释放线程锁

"""
from threading import Thread, Lock, currentThread
from time import sleep, ctime
import random
from atexit import register
lock = Lock()

def fun():
    # lock.acquire() #加锁
    for i in range(5):
        print("Thread Name = ",currentThread().name, "i =", i)
        sleep(random.randint(1,5))
    # lock.release() #解锁

def myfun():
    for i in range(3):
        Thread(target=fun).start()
@register
def exit():
    print("线程执行结束:",ctime())
myfun()

