from PyQt6 import QtCore
from PyQt6.QtCore import QRunnable
import debugpy
import requests
from datetime import datetime

class WorkerSignals(QtCore.QObject):
    finished = QtCore.pyqtSignal(dict,str)


class OrderDataWork(QRunnable):

    def __init__(self,name, cookie):
        super().__init__()
        self.signals = WorkerSignals()
        self.name = name
        self.cookie = cookie

    
    def run(self):
        # debugpy.debug_this_thread()
        # 模拟接口请求数据
        data = self.fetch_data()
        if data == None:
            return
        self.signals.finished.emit(data,self.name)


    def fetch_data(self):
        url = "https://yiyao.meituan.com/health/pc/order/list/query"

        headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "Connection": "keep-alive",
            "Content-Type": "application/json;charset=UTF-8",
            "Cookie": 'WEBDFPID=5uu6v81uwu7452780uux850xx7u1zw8y81yzy99546y97958xw37x952-2014740998953-1699380998234KMQCQEUfd79fef3d01d5e9aadc18ccd4d0c95072134; uuid_update=true; pushToken=0IHuCXFALTQQJsqUeAwg2zbEZEMjO7m2MpBfL4pCtRHE*; iuuid=BE7F292D754439183A5AD35C1A98AB626C89D76602B827A2DF8589636ED23F24; ci=44; cityname=%E7%A6%8F%E5%B7%9E; __utma=74597006.657253308.1701349088.1701349088.1701349088.1; _lxsdk=BE7F292D754439183A5AD35C1A98AB626C89D76602B827A2DF8589636ED23F24; userId=305341949; u=305341949; Hm_lvt_cc86211b89ef384b7a1651ab62391e0e=1709127989; _ga=GA1.1.1096046427.1709719432; _ga_95GX0SH5GM=GS1.1.1709719431.1.1.1709719516.0.0.0; Hm_lvt_157affb1807b7f0daed4e6f0d9529e56=1709529978,1709979159,1710051507,1710065750; device_uuid=!76ccb42b-7280-4ad9-b3cd-0f5630df23c6; acctId=184561063; token=0Ir4y9wzqUSMltnCNNHb_0creknKD-O0W4_MrMVl5ri8*; brandId=-1; wmPoiId=20595243; isOfflineSelfOpen=2; city_id=0; isChain=0; existBrandPoi=true; ignore_set_router_proxy=false; region_version=0; newCategory=true; bsid=zfP5X_PNp2_zwdD8Yl1UR0NkOM-mEKfO3KuCZsSnUAYBOzS977ijmdZWyXBYEuADkY6YTskk8ZOBebiEtxHJKQ; cityId=330100; provinceId=310000; city_location_id=371500; location_id=371502; account_businesstype=2; single_poi_businesstype=2; accountAllPoiBusinessType=2; acct_id=184561063; acct_name=mt104374v; poi_id=20595243; account_second_type=310; poi_first_category_id=22; poi_second_category_id=179; pharmacistAccount=0; __51vcke__3HVlmB9e1VFRstol=2f1e4b94-6752-56db-ae91-7daca495137b; __51vuft__3HVlmB9e1VFRstol=1708349182359; __51uvsct__3HVlmB9e1VFRstol=1343; set_info={"wmPoiId":20595243,"region_id":"1000371500","region_version":1709104801}; _lxsdk_cuid=1883ebb3bbbc8-027fc313ab691f-26031a51-306000-1883ebb3bbbc8; igateApp=igate; _lx_utm=utm_source%3Dgoogle%26utm_medium%3Dorganic; uuid=37f91127c50a2cf1007b.1719645241.1.0.0; cacheTimeMark=2024-07-01; _gw_ab_call_37616_37=TRUE; _gw_ab_37616_37=62; wpush_server_url=wss://wpush.meituan.com; Hm_lvt_ed0a6497a1fdcdb3cdca291a7692408d=1719832238,1719832440,1719832932,1719833397; Hm_lvt_5d9f09afca5675c534c22d2c685e1128=1719832238,1719832440,1719832932,1719833397; Hm_lvt_7afe580efa9cda86356bdea8077a83e7=1719832238,1719832440,1719832932,1719833397; terminal=bizCenter; Hm_lpvt_ed0a6497a1fdcdb3cdca291a7692408d=1719833427; Hm_lpvt_5d9f09afca5675c534c22d2c685e1128=1719833427; Hm_lpvt_7afe580efa9cda86356bdea8077a83e7=1719833427; shopCategory=medicine; _lxsdk_s=1906e5dd732-591-f9c-07e%7C%7C10',
            "M-APPKEY": "fe_com.sankuai.yiyaobb2cpf.merchant",
            "M-TRACEID": "-7490703048493255716",
            "Origin": "https://yiyao.meituan.com",
            "Referer": "https://yiyao.meituan.com/page/medicine/e/b2cOrder",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
            "sec-ch-ua": "\"Not)A;Brand\";v=\"99\", \"Microsoft Edge\";v=\"127\", \"Chromium\";v=\"127\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\""
        }

        data = {
            "token": "0Ir4y9wzqUSMltnCNNHb_0creknKD-O0W4_MrMVl5ri8*",
            "acctId": "184561063",
            "wmPoiId": "20595243",
            "bsid": "zfP5X_PNp2_zwdD8Yl1UR0NkOM-mEKfO3KuCZsSnUAYBOzS977ijmdZWyXBYEuADkY6YTskk8ZOBebiEtxHJKQ",
            "appType": 3,
            "orderViewIdOrDaySeq": "",
            "itemName": "",
            "upc": "",
            "recipientName": "",
            "recipientPhone": "",
            "orderStartDate": "2024-07-03 00:00:00",
            "orderEndDate": "2024-07-03 23:59:59",
            "spPkgNum": "",
            "partPerform": 0,
            "orderTag": "",
            "page": 1,
            "size": 20,
            "ascOrder": False
        }
        response = requests.post(url, headers=headers, json=data)
        
        return response.json()



