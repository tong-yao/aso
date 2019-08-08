# -*- coding=utf-8 -*-
# @Time : 2019/6/26 9:41
# @Author : piller
# @File : ranking_bill_board_spider.py
# @Software: PyCharm
import sys, datetime
from os.path import abspath, join, dirname
import requests
import random
import time
from settingplus import user_agent,proxies,source_url_dict,json_write,timeout

sys.path.insert(0, join(abspath(dirname(__file__)), '../'))


def headers():
    # 配置请求头
    header = {
        "User-Agent": "{}".format(user_agent()),
        "x-apple-store-front": "143465-19,29"
    }
    return header




def get_source_url():
    for key, value in source_url_dict.items():
        yield (key, value)


def su_next(su):
    try:
        key, value = su.__next__()
        return key, value
    except StopIteration:
        pass


starttime = datetime.datetime.now()


def main():
    """流程调转"""
    error_number = 0
    su = get_source_url()
    while 1:

        key, value = su_next(su)

        proxy = random.choice(proxies())
        agent = {
            "http": proxy
        }
        print("目前使用代理为:{}".format(agent))
        print("请求", value)
        response = requests.get(value, headers=headers(), timeout=timeout, proxies=agent)
        print("本次请求为{}页, 该页状态码为{}".format(key, response.status_code))
        bill_board_ranking_json = response.content.decode()
        # base_path = "/home/gogs/spider/billBoardInfo/"
        base_path = "/home/aso/"
        # base_path = "/Users/a1/PycharmProjects/z_lzxx/spider_aso/"
        times = str(int(time.time() * 1000))
        path = base_path + "{}" + "{}".format(times,key) + ".json"
        json_write(path, bill_board_ranking_json,times, key, starttime)
        # insert_ranking_bill_board(source=key, bill_board_ranking_json=path)
        # file(path)
        #     except requests.exceptions.ConnectTimeout:
        #         error_number += 1
        #         print("请求失败, 当前第{}次请求".format(error_number))
        #         if error_number >= 10:
        #             error_number = 0
        #             break
        #         continue
        #     except requests.exceptions.ConnectionError:
        #         error_number += 1
        #         print("请求失败, 当前第{}次请求".format(error_number))
        #         if error_number >= 10:
        #             error_number = 0
        #             break
        #         continue
        #     except requests.exceptions.Timeout:
        #         error_number += 1
        #         print("请求失败, 当前第{}次请求".format(error_number))
        #         if error_number >= 10:
        #             error_number = 0
        #             break
        #         continue
        #     else:
        #         error_number = 0
        #         break






if __name__ == '__main__':
    main()
