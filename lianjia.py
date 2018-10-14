#_*_ coding:utf-8 _*_
import requests
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        return r.text
    except Exception as ec:
        return '产生异常'


def get_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    infos = soup.find('ul', {'class': 'sellListContent'}).find_all('li')
    with open(r'/users/1111/lianjia.csv', 'a') as f:
        for info in infos:
            name = info.find('div', {'class': 'title'}).find('a').get_text()
            price = info.find('div', {'class': 'priceInfo'}).find('div', {'class', 'totalPrice'}).find(
                'span').get_text()
            houseinfor = info.find('div', {'class': 'houseInfo'}).find('a').get_text()
            f.write("{},{},{}\n".format(name, price, houseinfor))


def main():
    start_url = 'https://su.lianjia.com/ershoufang/'
    for i in range(100):
        url = start_url + "pg"+str(i)
        html = getHTMLText(url)
        get_data(html)

main()