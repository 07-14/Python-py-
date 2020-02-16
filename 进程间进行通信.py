from multiprocessing import Queue,Process
import time,random
"""
通过队列在进程间进行通信
"""

value = ["java","php","pyhton"]

def write(queue):
    for v in value:
        print(f"正在向队列中传送数据{v}")
        queue.put_nowait(v)
        time.sleep(random.random())

def read(queue):
    while True:
        if not queue.empty():
            v = queue.get_nowait()
            print(f"正在从队列中读取数据{v}")
            time.sleep(random.random())
        else:
            break


queue = Queue()
writeprocess = Process(target=write,args=(queue,))
readprocess = Process(target=read,args=(queue,))
if __name__ == '__main__':
    writeprocess.start()
    writeprocess.join()
    readprocess.start()
    readprocess.join()
    print("ok")
