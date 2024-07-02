from PyQt6 import QtCore
from PyQt6.QtCore import QRunnable
import debugpy
import requests
from datetime import datetime

class WorkerSignals(QtCore.QObject):
    finished = QtCore.pyqtSignal(dict,str)


class PurchaseDataWork(QRunnable):

    def __init__(self,name, cookie,isSelectPurchaseTime,dateStart,dateEnd):
        super().__init__()
        self.signals = WorkerSignals()
        self.name = name
        self.cookie = cookie
        self.isSelectPurchaseTime = isSelectPurchaseTime
        self.dateStart = dateStart
        self.dateEnd = dateEnd

    
    def run(self):
        # debugpy.debug_this_thread()
        # 模拟接口请求数据
        data = self.fetch_data()
        if data == None:
            return
        self.signals.finished.emit(data,self.name)


    def fetch_data(self):
        url = "https://mterp.renyi.club/api/purch/log"

        headers = {
            "accept": "application/json",
            "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "content-type": "application/json; charset=utf-8",
            "cookie": self.cookie,
            "origin": "https://mterp.renyi.club",
            "priority": "u=1, i",
            "referer": "https://mterp.renyi.club/purch/log",
            "sec-ch-ua": '"Chromium";v="124", "Microsoft Edge";v="124", "Not-A.Brand";v="99"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "token": "PjGT5FV+g3AjOdZ4894xMg==",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0"
        }

        field = ""
        if self.isSelectPurchaseTime:
            field = "AddTime"
        else:
            field = "OrderTime"
        data = {
            "items": [
                {
                    "filterId": field,
                    "field":field,
                    "method": 4,
                    "value": self.dateStart
                },
                {
                    "filterId": field,
                    "field": field,
                    "method": 3,
                    "value": self.dateEnd
                }
            ],
            "page": 1,
            "pageSize": 99999,
            "sortOrder": "",
            "sortName": ""
        }
        response = requests.post(url, headers=headers, json=data)
        return response.json()





