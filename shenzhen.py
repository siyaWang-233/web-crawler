import os
import urllib.request
from io import BytesIO
import re
import csv


def gethtml(url):
    response = urllib.request.urlopen(url)
    html = response.read()
    html = html.decode('utf-8')
    return html

def all_info(html):
    texturls = re.findall(r"from=title.*?>(.*?)&nbsp;</a>.*?<p class='baseinfo'>\s*<span>(\S*)</span>.*?<p class='unit'>(.*?)元/平</p>", html, re.S)
    return texturls

if __name__ == '__main__':
    list = []
    for i in range(70):
        url = 'https://sz.58.com/xiaoqu/' + 'pn_' + str(i+1)
        html = gethtml(url)
        all = all_info(html)
        for a in all:
            list.append(a)
            print(a)
        print("done ",i+1)
    with open('shenzhen.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(list)
















