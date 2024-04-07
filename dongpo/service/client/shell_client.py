import re
import requests
from dongpo import config


# 参考文档：https://blog.51cto.com/u_15168725/2708108
# 获取贝壳数据服务
class ShellConfig:
    name = ''
    house_url = ''
    buildArea = 0
    actualArea = 0
    publicShare = 0
    unitPriceLimit = 0
    feishu_url = ''
    black_list_valid = 1

    def __init__(self, name, house_url, buildArea, actualArea, unitPriceLimit, feishu_url, black_list_valid):
        self.name = name
        self.house_url = house_url
        self.actualArea = actualArea
        self.buildArea = buildArea
        self.publicShare = round((buildArea - actualArea) / buildArea, 4)
        self.unitPriceLimit = unitPriceLimit
        self.feishu_url = feishu_url
        self.black_list_valid = black_list_valid


def query_total_price(e):
    return e[3]


def query_house_lists(shellConfig):
    # 01-获取网页原始信息
    rep = requests.get(shellConfig.house_url)
    html = rep.text
    html = re.sub('\\s', '', html)
    htmlListContent = re.findall(r'<ulclass="sellListContent"log-mod="list">(.*?)</ul>', html)[0]
    htmlLists = re.findall(r'<liclass="clear">(.*?)</li>', htmlListContent)

    # 02-将原始信息初始化成列表
    houseList = []
    for html in htmlLists:
        try:
            totalPrice = re.findall(r'<divclass="totalPricetotalPrice2"><i></i><spanclass="">(.*?)</span><i>', html)[0]
            house = [re.findall(r'housedel_id=(\d+)&', html)[0],
                     re.findall(r'<spanclass="houseIcon"></span>(.*?)</div>', html)[0],
                     totalPrice,
                     re.findall(r'<divclass="unitPrice".*<span>(.*?)元/平</span></div></div></div>', html)[0].replace(',', ''),
                     shellConfig.actualArea,
                     int(totalPrice) * 10000 // shellConfig.actualArea,
                     shellConfig.publicShare,
                     re.findall(r'detail"title="(.*?)"data-hreftype', html)[0],
                     re.findall(r'<spanclass="starIcon"></span>(.*?)</div>', html)[0],
                     re.findall(r'"href="(.*?)"target="_blank"', html)[0]]
            houseList.append(house)
        except Exception as e:
            print(e)
            continue

    # 03-排序
    houseList.sort(key=query_total_price)

    # 04-过滤
    for house in houseList.copy():
        if int(house[3]) > shellConfig.unitPriceLimit:
            houseList.remove(house)
            continue
        if house[0] in config.black_list and shellConfig.black_list_valid == 1:
            houseList.remove(house)
            continue

    # 05-返回
    return houseList


def query_house_info():
    # 01-获取网页原始信息
    rep = requests.get('https://wh.ke.com/ershoufang/104112833454.html')
    html = rep.text
    html = re.sub('\\s', '', html)
    print('https://wh.ke.com/ershoufang/104112833454.html')
    print(html)


if __name__ == '__main__':
    query_house_info()
