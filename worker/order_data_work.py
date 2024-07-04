from PyQt6 import QtCore
from PyQt6.QtCore import QRunnable
import debugpy
import requests
from utils import cookie_util

class WorkerSignals(QtCore.QObject):
    finished = QtCore.pyqtSignal(list)


class OrderDataWork(QRunnable):

    def __init__(self, cookie,dateStart,dateEnd):
        super().__init__()
        self.signals = WorkerSignals()
        self.cookie = cookie
        self.dateStart = dateStart
        self.dateEnd = dateEnd

    
    def run(self):
        # debugpy.debug_this_thread()
        # 模拟接口请求数据
        data = self.fetch_data()
        if data == None:
            return
        self.signals.finished.emit(data)


    def fetch_data(self):
        url = "https://yiyao.meituan.com/health/pc/order/list/query"

        headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "Connection": "keep-alive",
            "Content-Type": "application/json;charset=UTF-8",
            "Cookie": self.cookie,
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
        responseDatas = []
        current_page =1
        cursor = {}
        while True:
            data = {
                "token": cookie_util.get_mt_cookie_token(self.cookie),
                "acctId": cookie_util.get_mt_cookie_acctId(self.cookie),
                "wmPoiId":cookie_util.get_mt_cookie_wmPoiId(self.cookie),
                "bsid": cookie_util.get_mt_cookie_bsid(self.cookie),
                "appType": 3,
                "orderViewIdOrDaySeq": "",
                "itemName": "",
                "upc": "",
                "recipientName": "",
                "recipientPhone": "",
                "orderStartDate": self.dateStart,
                "orderEndDate": self.dateEnd,
                "spPkgNum": "",
                "partPerform": 0,
                "orderTag": "",
                "page": current_page,
                "size": 20,
                "ascOrder": False
            }

            if bool(cursor):
                data["cursor"] = cursor
            response = requests.post(url, headers=headers, json=data).json()


            if response["code"] !=0:
                print(str(response))
                return
            dataJson = response["data"]

            content = dataJson["content"]
            responseDatas.extend(content)

            cursor = dataJson["cursor"]
            totalPage = dataJson["totalPage"]
            print("加载current_page："+str(current_page))
            if totalPage>current_page:
                current_page+=1
            else:
                break

        return responseDatas




