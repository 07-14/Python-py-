from urllib3 import *
from threading import Thread

disable_warnings() # 关闭警告



urlList = []
f = open("url.txt", "r")
while True:
    url = f.readline()
    if url:
        urlList.append(url.strip())
    else:
        break
f.close()
print(urlList)

class DownloadThread(Thread): # 自定义一个线程类，其实直接用Thread也完全可以
    def __init__(self,func,args):
        super().__init__(target = func,args=args)

http = PoolManager()
def download(filename,url):
    response = http.request('GET',url)
    f = open(filename,"wb")
    f.write(response.data)
    f.close()
    print("已下载")

for i in range(len(urlList)):
    thread = DownloadThread(download,(str(i)+".jpg",urlList[i]))
    thread.start()

