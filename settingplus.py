import requests
from fake_useragent import UserAgent
import json
import random
import pymysql
import datetime
import re
import datetime
import logging


# base_path = "/home/video/"
# base_path = "./"

def user_agent():
    """获取UA"""
    u_a = UserAgent().random
    return u_a

def proxies():
    with open("proxys.txt", "r")as f:
        proxy = f.read()

    proxy = re.sub(r'\[', '', proxy)
    proxy = re.sub(r'\]', '', proxy)
    proxy = proxy.split(",")
    l = []
    for i in proxy:
        l.append(re.sub(r'\"|\'', "", i))
    return l

proxy = random.choice(proxies())
agent = {
    "http": proxy
}

timeout = 20
HOST = "39.97.241.144"
PORT = 3306
USER = "lianzhuoxinxi"
PASSWORD = 'LIANzhuoxinxi888?'
DATABASE = "spider"
CHARSET = "utf8"
start_time = datetime.datetime.now().strftime('%Y%m%d%H%M%S')  # 开始时间

def headers():
    # 配置请求头
    header = {
        "User-Agent": "{}".format(user_agent()),
        "x-apple-store-front": "143465-19,29"
    }
    return header

print("程序开始时间:{}".format(start_time))
def connect_mysql():
    # 链接mysql
    db = pymysql.connect(
        host=HOST,
        port=PORT,
        user=USER,
        password=PASSWORD,
        db=DATABASE,
        charset=CHARSET
    )
    return db

db = connect_mysql()




source_url_dict = {
    "总榜": "https://itunes.apple.com/WebObjects/MZStore.woa/wa/viewTop?cc=cn&genreId=36&popId=30",  # 总榜
    "游戏总榜" : "https://itunes.apple.com/WebObjects/MZStore.woa/wa/viewTop?cc=cn&genreId=6014&popId=30&pageOnly=true",
    "休闲游戏" : "https://itunes.apple.com/WebObjects/MZStore.woa/wa/viewTop?cc=cn&genreId=7003&popId=30&pageOnly=true",
    "体育（游戏）" : "https://itunes.apple.com/WebObjects/MZStore.woa/wa/viewTop?cc=cn&genreId=7016&popId=30&pageOnly=true",
    "冒险游戏" : "https://itunes.apple.com/WebObjects/MZStore.woa/wa/viewTop?cc=cn&genreId=7002&popId=30&pageOnly=true",
    "动作游戏" : "https://itunes.apple.com/WebObjects/MZStore.woa/wa/viewTop?cc=cn&genreId=7001&popId=30&pageOnly=true",
    "卡牌游戏" : "https://itunes.apple.com/WebObjects/MZStore.woa/wa/viewTop?cc=cn&genreId=7005&popId=30&pageOnly=true",
    "娱乐场游戏" : "https://itunes.apple.com/WebObjects/MZStore.woa/wa/viewTop?cc=cn&genreId=7006&popId=30&pageOnly=true",
    "文字游戏" : "https://itunes.apple.com/WebObjects/MZStore.woa/wa/viewTop?cc=cn&genreId=7019&popId=30&pageOnly=true",
    "桌面游戏" : "https://itunes.apple.com/WebObjects/MZStore.woa/wa/viewTop?cc=cn&genreId=7004&popId=30&pageOnly=true",
    "模拟游戏" : "https://itunes.apple.com/WebObjects/MZStore.woa/wa/viewTop?cc=cn&genreId=7015&popId=30&pageOnly=true",
    "益智游戏" : "https://itunes.apple.com/WebObjects/MZStore.woa/wa/viewTop?cc=cn&genreId=7012&popId=30&pageOnly=true",
    "竞速游戏" : "https://itunes.apple.com/WebObjects/MZStore.woa/wa/viewTop?cc=cn&genreId=7013&popId=30&pageOnly=true",
    "策略游戏" :  "https://itunes.apple.com/WebObjects/MZStore.woa/wa/viewTop?cc=cn&genreId=7017&popId=30&pageOnly=true",
    "聚会游戏" : "https://itunes.apple.com/WebObjects/MZStore.woa/wa/viewTop?cc=cn&genreId=7009&popId=30&pageOnly=true",
    "角色扮演游戏" : "https://itunes.apple.com/WebObjects/MZStore.woa/wa/viewTop?cc=cn&genreId=7014&popId=30&pageOnly=true",
    "问答游戏" : "https://itunes.apple.com/WebObjects/MZStore.woa/wa/viewTop?cc=cn&genreId=7018&popId=30&pageOnly=true",
    "音乐（游戏）" : "https://itunes.apple.com/WebObjects/MZStore.woa/wa/viewTop?cc=cn&genreId=7011&popId=30&pageOnly=true",
    "儿童": "https://itunes.apple.com/WebObjects/MZStore.woa/wa/viewTop?ageBandId=0&cc=cn&genreId=36&pageOnly=true",  # 儿童
    "教育": "https://itunes.apple.com/WebObjects/MZStore.woa/wa/viewTop?cc=cn&genreId=6017&popId=30&pageOnly=true",  # 教育
    "购物": "https://itunes.apple.com/WebObjects/MZStore.woa/wa/viewTop?cc=cn&genreId=6024&popId=30&pageOnly=true",  # 购物
    "摄影与录像": "https://itunes.apple.com/WebObjects/MZStore.woa/wa/viewTop?cc=cn&genreId=6008&popId=30&pageOnly=true",  # 摄影与录像
    "效率": "https://itunes.apple.com/WebObjects/MZStore.woa/wa/viewTop?cc=cn&genreId=6007&popId=30&pageOnly=true",
    "美食佳饮": "https://itunes.apple.com/WebObjects/MZStore.woa/wa/viewTop?cc=cn&genreId=6023&popId=30&pageOnly=true",
    "生活": "https://itunes.apple.com/WebObjects/MZStore.woa/wa/viewTop?cc=cn&genreId=6012&popId=30&pageOnly=true",
    "健康健美": "https://itunes.apple.com/WebObjects/MZStore.woa/wa/viewTop?cc=cn&genreId=6013&popId=30&pageOnly=true",
    "旅游": "https://itunes.apple.com/WebObjects/MZStore.woa/wa/viewTop?cc=cn&genreId=6003&popId=30&pageOnly=true",
    "音乐": "https://itunes.apple.com/WebObjects/MZStore.woa/wa/viewTop?cc=cn&genreId=6011&popId=30&pageOnly=true",
    "体育": "https://itunes.apple.com/WebObjects/MZStore.woa/wa/viewTop?cc=cn&genreId=6004&popId=30&pageOnly=true",
    "商务": "https://itunes.apple.com/WebObjects/MZStore.woa/wa/viewTop?cc=cn&genreId=6000&popId=30&pageOnly=true",
    "新闻": "https://itunes.apple.com/WebObjects/MZStore.woa/wa/viewTop?cc=cn&genreId=6009&popId=30&pageOnly=true",
    "工具": "https://itunes.apple.com/WebObjects/MZStore.woa/wa/viewTop?cc=cn&genreId=6002&popId=30&pageOnly=true",
    "娱乐": "https://itunes.apple.com/WebObjects/MZStore.woa/wa/viewTop?cc=cn&genreId=6016&popId=30&pageOnly=true",
    "社交": "https://itunes.apple.com/WebObjects/MZStore.woa/wa/viewTop?cc=cn&genreId=6005&popId=30&pageOnly=true",
    "报刊杂志": "https://itunes.apple.com/WebObjects/MZStore.woa/wa/viewTop?cc=cn&genreId=6021&popId=30&pageOnly=true",
    "财务": "https://itunes.apple.com/WebObjects/MZStore.woa/wa/viewTop?cc=cn&genreId=6015&popId=30&pageOnly=true",
    "参考": "https://itunes.apple.com/WebObjects/MZStore.woa/wa/viewTop?cc=cn&genreId=6006&popId=30&pageOnly=true",
    "导航": "https://itunes.apple.com/WebObjects/MZStore.woa/wa/viewTop?cc=cn&genreId=6010&popId=30&pageOnly=true",
    "医疗": "https://itunes.apple.com/WebObjects/MZStore.woa/wa/viewTop?cc=cn&genreId=6020&popId=30&pageOnly=true",
    "图书": "https://itunes.apple.com/WebObjects/MZStore.woa/wa/viewTop?cc=cn&genreId=6018&popId=30&pageOnly=true",
    "天气": "https://itunes.apple.com/WebObjects/MZStore.woa/wa/viewTop?cc=cn&genreId=6001&popId=30&pageOnly=true",
}

def json_write(path, info,times,key,starttime):
    with open(path, 'w') as f:
        f.write(info)
        f.close()
    with open(path, 'r') as f:
        a = f.read()
        a = json.loads(a)
        if path == "/home/aso/{}总榜.json".format(times):
            a_data = a["pageData"]["segmentedControl"]["segments"][0]["pageData"]["categoryList"]
            if "parentCategoryLabel" in a_data:
                name = a_data["parentCategoryLabel"]
                with db.cursor() as cursor:
                    try:
                        sql = "insert into listname (namelist,starttime) values ('%s','%s')" % (
                            name,starttime)
                        cursor.execute(sql)
                    except Exception as e:
                        print(sql)
                        print("e,第一个listname", e)
                db.commit()
            loop = a_data["children"]
            for i in loop:
                name = i["name"]
                with db.cursor() as cursor:
                    try:
                        sql = "insert into listname (namelist,starttime) values ('%s','%s')" % (
                            name,starttime)
                        cursor.execute(sql)
                    except Exception as e:
                        print(sql)
                        print("ee,第二个listname", e)
                    db.commit()
                if "children" in i:
                    children_name = []
                    for b in i["children"]:
                        name = i["name"]
                        children_name.append(b["name"])
                    with db.cursor() as cursor:
                        try:
                            sql = "UPDATE listname SET children = '{}' WHERE namelist = '{}' and starttime = '{}'".format(pymysql.escape_string(str(children_name)),name,starttime)
                            cursor.execute(sql)
                        except Exception as e:
                            print(sql)
                            print("eee,第三次更新listname", e)
                        db.commit()

            free = a["pageData"]["segmentedControl"]["segments"][0]["pageData"]["topCharts"][0]["adamIds"]  # 付费
            best = 0
            save(key, free,best,starttime)
            toll = a["pageData"]["segmentedControl"]["segments"][0]["pageData"]["topCharts"][1]["adamIds"]  # 免费
            best = 0
            save(key, toll,best,starttime)
            bestseller = a["pageData"]["segmentedControl"]["segments"][0]["pageData"]["topCharts"][2]["adamIds"]
            best = 1
            save(key, bestseller, best, starttime)


        else:
            free = a["pageData"]["topCharts"][0]["adamIds"]
            best = 0
            save(key, free, best, starttime)
            toll = a["pageData"]["topCharts"][1]["adamIds"]
            best = 0
            save(key, toll, best, starttime)
            bestseller = a["pageData"]["topCharts"][2]["adamIds"]
            best = 1
            save(key, bestseller, best, starttime)



def save(key, lis,best,starttime):
    top = 0
    for i in lis:
        top += 1
        response = requests.get("https://apps.apple.com/cn/app/this-war-of-mine/id{}".format(i), headers=headers(),timeout=timeout, proxies=agent)
        data = response.content.decode()
        data = json.loads(data)

        if i not in data["storePlatformData"]["product-dv"]["results"]:
            commodity_names = data["pageData"]["metricsBase"]["pageDetails"]
            deposittime = datetime.datetime.now()
            with db.cursor() as cursor:
                try:
                    sql = "insert into new_aso (top,appid,source,commodity_names,starttime,deposittime) values ('%s','%s','%s','%s','%s','%s')" % (
                        top, i, key, commodity_names, starttime, deposittime)
                    cursor.execute(sql)
                except Exception as e:
                    print(sql)
                    print("eeee,第一次总榜写入new_aso", e)
                db.commit()
            continue
        loop_vaule = data["storePlatformData"]["product-dv"]["results"][i]

        if "children" in loop_vaule:
            children = loop_vaule["children"]
            namesortvalue = loop_vaule["nameSortValue"]
            artistname = loop_vaule['artistName']
            price = loop_vaule["offers"][0]['price']
            deposittime = datetime.datetime.now()

            with db.cursor() as cursor:
                try:
                    sql = "insert into new_aso (top,appid,source,commodity_names,artistname,price,types,package,starttime,deposittime) values ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (
                        top, i, key, namesortvalue,  artistname, price, types, 1, starttime, deposittime)
                    cursor.execute(sql)
                except Exception as e:
                    print(sql)
                    print("eeeee,第一次写入包应用", e)
                db.commit()

            for j in children:
                source = "{}中第{}个".format(key,top)
                name = loop_vaule["children"][j]['name']
                releasedate = loop_vaule["children"][j]['releaseDate']
                price = loop_vaule["children"][j]["offers"][0]["price"]
                display = loop_vaule["children"][j]["offers"][0]["version"]["display"]
                deposittime = datetime.datetime.now()

                if best:
                    types = "畅销"
                else:
                    types = loop_vaule["offers"][0]["type"]

                with db.cursor() as cursor:
                    try:
                        sql = "insert into aso_package (appid, source, sourceid,commodity_names,releasedate,price,display,starttime,deposittime) values ('%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(
                            j,source,i,name,releasedate,price,display,starttime,deposittime)
                        cursor.execute(sql)
                    except Exception as e:
                        print(sql)
                        print("eeeeee，第一次存入包应用表aso_package",e)
                    db.commit()
            continue
        contentratingsbysystem = loop_vaule["contentRatingsBySystem"]["appsApple"]["name"]

        releasedate = loop_vaule["releaseDate"]

        commodity_names = loop_vaule["name"]

        if "minimumOSVersion"  in loop_vaule:
            minimumosversion = loop_vaule["minimumOSVersion"]
        else:
            minimumOSVersion = "没有要求"

        artistname = loop_vaule["artistName"]

        if "subtitle" in loop_vaule:
            subtitle = loop_vaule["subtitle"]
        else:
            subtitle = "没有副标题"

        fenshu = loop_vaule["userRating"]["value"]

        ratingcount = loop_vaule["userRating"]["ratingCount"]

        price = loop_vaule["offers"][0]["price"]

        if best:
            types = "畅销"
        else:
            types = loop_vaule["offers"][0]["type"]

        versionstring = data["pageData"]["versionHistory"][0]["versionString"]

        new_releasedate = data["pageData"]["versionHistory"][0]["releaseDate"]

        deposittime = datetime.datetime.now()

        with db.cursor() as cursor:
            try:
                sql = "insert into new_aso (top,appid,source,contentratingsbysystem,releasedate,commodity_names,minimumosversion,artistname,subtitle,fenshu,ratingcount,price,types,versionstring,new_releasedate,package, starttime,deposittime) values ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (
                    top, i, key, contentratingsbysystem, releasedate, pymysql.escape_string(commodity_names), minimumosversion, artistname, subtitle,
                    fenshu, ratingcount, price, types, versionstring, new_releasedate,0, starttime,deposittime)
                cursor.execute(sql)
            except Exception as e:
                print(sql)
                print("eeeeeee，正常其他榜单写入应用", e)
            db.commit()

