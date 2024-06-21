import schedule
import datetime
import time
from dongpo import manager
from dongpo import config


def print_time():
    print(datetime.datetime.now())


if __name__ == '__main__':
    # 测试
    # 创建一个按3秒间隔执行任务
    # schedule.every(3).seconds.do(print_time)
    # 创建一个按3分钟间隔执行任务
    schedule.every(3).minutes.do(print_time)
    # 指定时间执行测试任务
    # schedule.every().hour.at(':00').do(manager.query_house_info, config.test_config_init())

    # 我的定时任务
    schedule.every().day.at('08:03').do(manager.query_house_info, config.v0_config_init())

    # 通用客户的任务
    schedule.every().friday.at('12:13').do(manager.query_house_info, config.ggd_config_init())
    schedule.every().friday.at('12:23').do(manager.query_house_info, config.gs_config_init())
    schedule.every().friday.at('12:33').do(manager.query_house_info, config.yjw_config_init())

    # 定制化客户的任务
    schedule.every().day.at('09:13').do(manager.query_house_info, config.wenjie_config_init())
    while True:
        schedule.run_pending()
        time.sleep(1)
