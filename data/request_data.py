from PyQt6 import QtCore
from config import config
from worker.home_data_work import HomeDataWork
from worker.purchase_data_work import PurchaseDataWork

class RequestData:

    def __init__(self):
        super().__init__()
        self.threadpool = QtCore.QThreadPool()
        self.threadpool.setMaxThreadCount(20)



    def request_data(self,callback):

        shop_list = config.get_shop_list()
        for shop in shop_list:
            name = shop["name"]
            cookie = shop["cookie"]
            homeDataWork = HomeDataWork(name,cookie)
            homeDataWork.signals.finished.connect(callback)
            self.threadpool.start(homeDataWork)
    

    def request_purchase_data(self,isSelectPurchaseTime,dateStart,dateEnd,callback):
        purchase_list = config.get_purchase_list()
        for purchase in purchase_list:
            name = purchase["name"]
            cookie = purchase["cookie"]
            purchaseDataWork = PurchaseDataWork(name,cookie,isSelectPurchaseTime,dateStart,dateEnd)
            purchaseDataWork.signals.finished.connect(callback)
            self.threadpool.start(purchaseDataWork)