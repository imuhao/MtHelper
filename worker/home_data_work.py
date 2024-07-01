from PyQt6 import QtCore
from PyQt6.QtCore import QRunnable
import requests
import debugpy
import config.config

class WorkerSignals(QtCore.QObject):
    finished = QtCore.pyqtSignal(dict,str)


class HomeDataWork(QRunnable):

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
        url = "https://yiyao.meituan.com/api/page/bizdata/manageHome/single/b/core"
        params = {
            "businessType": "2",
            "storeType": "1",
            "dateType": "realTime",
            "beginTime": "20240701",
            "endTime": "20240701",
            "compareBeginTime": "20240630",
            "compareEndTime": "20240630",
            "yodaReady": "h5",
            "csecplatform": "4",
            "csecversion": "2.4.0",
            "mtgsig": '{"a1":"1.1","a2":1719833429634,"a3":"5uu6v81uwu7452780uux850xx7u1zw8y81yzy99546y97958xw37x952","a5":"7n3lPf6f+J3GO6b578fHYT67M9r/UlH0","a6":"hs1.4aOG4x69iuIGtADfqn9IKcejgsmOgEUy56HBumI/73CvrYqdskSMRBMU2Z/mu1xaZrmJsogJ7Cx3p5Rt20WnBWA==","x0":4,"d1":"0ffa076f4dfa48b55dba487b42004fd9"}'
        }

        headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "Connection": "keep-alive",
            "Cookie": self.cookie,
            "Referer": "https://yiyao.meituan.com/page/analysis/home/b2c?wmPoiId=20595243&region_id=1000371500&region_version=1709104801",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0",
            "sec-ch-ua": '"Chromium";v="124", "Microsoft Edge";v="124", "Not-A.Brand";v="99"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"'
        }

        response = requests.get(url, params=params, headers=headers)

        return response.json()





