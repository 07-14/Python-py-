"""
threading.local #可以保存全局变量，但是只针对当前线程

"""
import threading,time

a = threading.local()
def working():
    a.x = 0
    for x in range(20):
        time.sleep(0.01)
        a.x += 1
    print(threading.current_thread(),a.x)

for i in range(10):
    threading.Thread(target = working).start()