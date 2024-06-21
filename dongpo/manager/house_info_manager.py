import datetime
import time
from prettytable import PrettyTable
from dongpo import config
from dongpo.service import client


# 构建飞书标题
def build_house_title(shellConfig):
    return str(datetime.date.today()) + ' ' + shellConfig.name


# 构建飞书消息体
def build_house_info(house, num, lastLine):
    return [
        {'tag': 'text',
         'text': '第' + str(num) + '套-' + house[0]
                 + '\n详情：' + house[1]
                 + '\n总价（万）：' + str(house[2])
                 + '\n均价（元）：' + str(house[3])
                 + '\n链接：'
         },
        {'tag': 'a',
         'text': house[7],
         'href': house[9]
         },
        {'tag': 'text',
         'text': lastLine
         }
    ]


# 查询满足条件的房子信息
def query_house_info(shellConfigs):
    # 01-获取房屋列表
    for shellConfig in shellConfigs:
        houseList = client.query_house_lists(shellConfig)
        if houseList == []:
            continue

        # 02-本地打印
        table = PrettyTable(
            ['编号', '详情', '总价（万）', '均价（元）', '预估实际面积（平方米）', '预估实际均价（元）', '预估公摊率', '描述',
             '关注人数', '链接'])
        for house in houseList:
            table.add_row(house)
        print(shellConfig.name)
        print(table)

        # 03-发消息
        content = []
        num = 1
        for house in houseList:
            lastLine = '\n '
            if num == len(houseList):
                lastLine = ''
            content.append(build_house_info(house, num, lastLine))
            num += 1
        client.send_msg(shellConfig.feishu_url,
                        client.get_post_data(build_house_title(shellConfig), content))
        time.sleep(10)


if __name__ == '__main__':
    query_house_info(config.test_config_init())
