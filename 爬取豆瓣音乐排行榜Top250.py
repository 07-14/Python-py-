import requests
from bs4 import BeautifulSoup
import re, time, csv

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"
}


def get_url_music(filename, url):
    html = requests.get(url, headers=headers)
    print(html.text)
    soup = BeautifulSoup(html.text, "lxml")
    Tags = soup.find_all("a", attrs={"class": "nbg"})
    if len(Tags) == 0:
        print("0")
    for tag in Tags:
        print(tag["href"])
        get_url_info(filename, tag["href"])


def get_url_info(filename, url):
    html = requests.get(url, headers=headers)
    soup = BeautifulSoup(html.text, "lxml")
    print(soup)
    # 获取专辑名
    name = soup.find(attrs={"id": "wrapper"}).h1.span.text

    # 获取表演者
    author = soup.find(attrs={"id": "info"}).find("a").text

    # 获取流派
    forms = re.findall('<span class="pl">流派:</span>&nbsp;(.*?)<br />', html.text, re.S)
    if len(forms) == 0:
        form = "未知"
    else:
        form = forms[0].strip()

    # 获取发行时间
    times = re.findall('<span class="pl">发行时间:</span>&nbsp;(.*?)<br />', html.text, re.S)
    if len(times) == 0:
        time = "未知"
    else:
        time = times[0].strip()

    info = {
        "name": name,
        "author": author,
        "form": form,
        "time": time
    }

    save_csv(filename, info)


def save_csv(filename, info):
    with open(filename, "a", encoding="utf-8") as f:
        fieldnames = ['name', 'author', 'form', 'time']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerow(info)


if __name__ == "__main__":
    filename = "music.csv"
    urls = ["https://music.douban.com/top250?start={}".format(str(i)) for i in range(0, 250, 25)]
    print(urls)
    with open(filename, "w", encoding="utf-8") as f:
        fieldnames = ['name', 'author', 'form', 'time']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

    for url in urls:
        print(url)
        get_url_music(filename, url)
        # time.sleep(1)
