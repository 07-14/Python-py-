import requests

r = requests.get("http://t.cn/EfgN7gz")
with open("book.png","wb") as f:
    f.write(r.content)
#如果是文本的话，得用r.text
#这里的requests和urllib3中的PoolManager中的request也有区别，后者是PoolManager().request('GET',网址)