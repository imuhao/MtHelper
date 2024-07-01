
import json


# 读取./config.ini文件
import configparser
config = configparser.ConfigParser(interpolation=configparser.ExtendedInterpolation())

def get_shop_list():
    config.read('./config/config.ini',encoding='utf-8')
    # 获取"美团大药房店铺"下的数据
    optoion_name = "美团大药房店铺"
    
    shop_list = []
    for option in config.options(optoion_name):
        shop_info = {"name":option,"cookie":config.get(optoion_name, option)}
        # shop_info[option] = config.get(shop_name, option)
        shop_list.append(shop_info)

    return shop_list



def add_shop(shopName,shopClloke):
    config.read('./config/config.ini',encoding='utf-8')
    # sessions =  self.config.add_section("美团大药房店铺")
    config.set("美团大药房店铺",shopName,shopClloke)

    # 保存修改
    with open('./config/config.ini', 'w',encoding='utf-8') as configfile:
        config.write(configfile)