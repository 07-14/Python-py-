"""
selenium更多用来测试web页面
但是也可以实现爬虫
利用浏览器本身的功能
需要webdriver


"""
#<div class="mine-text">我的关注</div>
from selenium import webdriver
import time

browser = webdriver.Chrome("./webdriver/chromedriver.exe")
try:
    browser.get("https://www.baidu.com/")
    button = browser.find_element_by_class_name("mine-text")
    button.click()

except Exception as e:
    print(e)
    browser.close()
