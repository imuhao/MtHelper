
import json


# 读取./config.ini文件
import configparser
config = configparser.ConfigParser(interpolation=configparser.ExtendedInterpolation())

#获取店铺数据
def get_shop_list(optoion):
    config.read('./config/config.ini',encoding='utf-8')
    # optoion_name = "我的店铺"
    shop_list = []
    for option in config.options(optoion):
        shop_info = {"name":option,"cookie":config.get(optoion, option)}
        shop_list.append(shop_info)
    return shop_list

#获取店铺名称
def get_shop_name(optoion):
    shop_list = get_shop_list(optoion)
    shop_name_list = []
    for shop in shop_list:
        shop_name_list.append(shop["name"])
    return shop_name_list

#根据店铺名称获取cookie
def get_shop_cookie(name):
    myShopList = get_shop_list("我的店铺")

    for shop in myShopList:
        if shop["name"] == name:
            return shop["cookie"]

    otherShopList = get_shop_list("同行店铺")

    for shop in otherShopList:
        if shop["name"] == name:
            return shop["cookie"]
    return ""

def get_purchase_list():
    config.read('./config/config.ini',encoding='utf-8')
    # 获取"阿芬迪采购"下的数据
    optoion_name = "阿芬迪采购"
    
    purchase_list = []
    for option in config.options(optoion_name):
        shop_info = {"name":option,"cookie":config.get(optoion_name, option)}
        purchase_list.append(shop_info)

    return purchase_list