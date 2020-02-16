import pyquery
from pyquery import PyQuery as py
import requests

page = requests.get("https://blog.csdn.net/weixin_36338224/article/details/104287582?request_id=&utm_source=distribute.pc_feed.none-task")
print(page.text)
with open("page_html.txt","w",encoding="utf-8") as f:
    f.write(page.text)

with open("page_html.txt","r",encoding="utf-8") as f:
    data = f.read()
#
# doc = py(url="https://blog.csdn.net/weixin_36338224/article/details/104287582?request_id=&utm_source=distribute.pc_feed.none-task")
#
#
# data1 = doc("li:first-child")
# print("--------------------------------")
# print(data1)
# data2 = doc("li:last-child")
# print("--------------------------------")
# print(data2)
# data3 = doc("li:contains(路飞)")
# print("--------------------------------")
# print(data3)
# data4 = doc(":contains(路飞)")
# print("--------------------------------")
# print(data4)
