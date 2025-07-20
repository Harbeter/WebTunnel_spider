from datetime import datetime
import time
import requests
from bs4 import BeautifulSoup

def getBridge():
    # 发送 GET 请求
    url = 'https://bridges.torproject.org/bridges?transport=webtunnel'  # 替换为您要请求的网站 URL
    response = requests.get(url)

    # 搜索网桥
    soup = BeautifulSoup(response.text, 'html.parser')
    bridge = soup.find('div', class_='p-4 mb-3', id='bridgelines')

    # 输出该div元素的文本内容
    bridge1 =' '.join(bridge.text.split()[0:5])
    print(bridge1)
    bridge2=' '.join(bridge.text.split()[5:])
    print(bridge2)
    return bridge1,bridge2
if __name__ == '__main__':
    while True:
        t = datetime.now()
        with open('bridge.txt', 'a') as file:
            b1, b2 = getBridge()
            file.write(str(t) + '\n' + b1 + '\n' + b2 + '\n\n')
        time.sleep(86400)
