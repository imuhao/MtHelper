
import json


# 读取./config.ini文件
import configparser
config = configparser.ConfigParser(interpolation=configparser.ExtendedInterpolation())

def get_shop_list(optoion):
    config.read('./config/config.ini',encoding='utf-8')
    # optoion_name = "我的店铺"
    shop_list = []
    for option in config.options(optoion):
        shop_info = {"name":option,"cookie":config.get(optoion, option)}
        shop_list.append(shop_info)
    return shop_list



def get_purchase_list():
    config.read('./config/config.ini',encoding='utf-8')
    # 获取"阿芬迪采购"下的数据
    optoion_name = "阿芬迪采购"
    
    purchase_list = []
    for option in config.options(optoion_name):
        shop_info = {"name":option,"cookie":config.get(optoion_name, option)}
        purchase_list.append(shop_info)

    return purchase_list