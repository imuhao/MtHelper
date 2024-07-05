from PyQt6 import QtCore
from PyQt6.QtCore import QRunnable
import debugpy
import requests
from datetime import datetime,timedelta
from utils import cookie_util
import json

class ViolationWorkerSignals(QtCore.QObject):
    finished = QtCore.pyqtSignal(dict)


class ViolationDataWork(QRunnable):

    def __init__(self, cookie):
        super().__init__()
        self.signals = ViolationWorkerSignals()
        self.cookie = cookie

    
    def run(self):
        # debugpy.debug_this_thread()
        # 模拟接口请求数据
        data = self.fetch_data()
        if data == None:
            return
        self.signals.finished.emit(data)


    def fetch_data(self):


        # 获取当前日期和时间
        now = datetime.now()

        # 今天23:59:59
        end_of_today = datetime.combine(now.date(), datetime.max.time()).replace(hour=23, minute=59, second=59, microsecond=999999)

        # 29天前的日期
        twenty_nine_days_ago_date = now - timedelta(days=29)
        start_of_twenty_nine_days_ago = datetime.combine(twenty_nine_days_ago_date.date(), datetime.min.time()).replace(hour=0, minute=0, second=0, microsecond=0)

        # 转换为时间戳（精确到毫秒）
        end_of_today_timestamp = int(end_of_today.timestamp() * 1000)
        start_of_one_month_ago_timestamp = int(start_of_twenty_nine_days_ago.timestamp() * 1000)

        url = "https://yiyao.meituan.com/manage/mid/platform/business/violation/ticket/query/v2"
        params = {
            "acctId": cookie_util.get_mt_cookie_acctId(self.cookie),
            "wmPoiId": cookie_util.get_mt_cookie_wmPoiId(self.cookie),
            "bsid": cookie_util.get_mt_cookie_bsid(self.cookie),
            "poiId": cookie_util.get_mt_cookie_wmPoiId(self.cookie),
            "appType": "3",
            "createStartTime": start_of_one_month_ago_timestamp,
            "createEndTime": end_of_today_timestamp,
            "appealStatusList": "[1,3]",
            "pageNo": "1",
            "pageSize": "10",
            "tabType": "ALL"
        }

        headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "Connection": "keep-alive",
            "Cookie":self.cookie,
            "M-APPKEY": "fe_com.sankuai.yiyaobb2cpf.merchant",
            "M-TRACEID": "1480250049611170735",
            "Referer": "https://yiyao.meituan.com/page/medicine/e/ruleCenter/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
            "sec-ch-ua": "\"Not)A;Brand\";v=\"99\", \"Microsoft Edge\";v=\"127\", \"Chromium\";v=\"127\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\""
        }
        response = requests.get(url, headers=headers, params=params).json()
        code = response["code"]
        if code!=0:
            return
        
        return response["data"]





class TransactionWorkerSignals(QtCore.QObject):
    finished = QtCore.pyqtSignal(list)


class TransactionDataWork(QRunnable):

    def __init__(self, cookie):
        super().__init__()
        self.signals = TransactionWorkerSignals()
        self.cookie = cookie

    
    def run(self):
        # debugpy.debug_this_thread()
        # 模拟接口请求数据
        data = self.fetch_data()
        if data == None:
            return
        self.signals.finished.emit(data)


    def fetch_data(self):
        url = "https://waimaieapp.meituan.com/growth/supervise/r/list"

        headers = {
            "Accept": "*/*",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "Connection": "keep-alive",
            "Cookie": self.cookie,
            "Origin": "https://waimaieapp.meituan.com",
            "Referer": ("https://waimaieapp.meituan.com/frontweb/ruleCenter?_source=PC&acctId=184561063&appType=3&bsid=zfP5X_PNp2_zwdD8Yl1UR0NkOM-mEKfO3KuCZsSnUAYBOzS977ijmdZWyXBYEuADkY6YTskk8ZOBebiEtxHJKQ&"
                    "from=yy&fromPoiChange=false&region_id=&token=0Ir4y9wzqUSMltnCNNHb_0creknKD-O0W4_MrMVl5ri8%2A&wmPoiId=20595243"),
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
            "content-type": "application/x-www-form-urlencoded",
            "sec-ch-ua": ('"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"'),
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"'
        }

        data = {
            "acctId": cookie_util.get_mt_cookie_acctId(self.cookie),
            "wmPoiId": cookie_util.get_mt_cookie_wmPoiId(self.cookie),
            "token": cookie_util.get_mt_cookie_token(self.cookie),
            "appType": "3",
            "type": "1",
            "pageNum": "1",
            "pageSize": "20",
            "ruleSubType": "-1",
            "appealStatusStr": "-1",
            "noticeTimeStart": "0",
            "noticeTimeEnd": "0"
        }

        response = requests.post(url, headers=headers, data=data)

        if not is_json(response.text):
            return
        
        responseJson = response.json()

        code = responseJson["code"]
        if code != 0:
            return
        data = responseJson["data"]
        violationInfos = data["violationInfos"]

        return violationInfos


def is_json(text):
    try:
        json_object = json.loads(text)
    except ValueError as e:
        return False
    return True