from PyQt6 import QtCore
from config import config
from worker.home_data_work import HomeDataWork
from worker.purchase_data_work import PurchaseDataWork
from worker.order_data_work import OrderDataWork
from worker.violation_data_work import TransactionDataWork, ViolationDataWork

class RequestData:

    def __init__(self):
        super().__init__()
        self.threadpool = QtCore.QThreadPool()
        self.threadpool.setMaxThreadCount(20)

        self.threadpool2 = QtCore.QThreadPool()
        self.threadpool2.setMaxThreadCount(20)


    #获取店铺数据
    def request_shop_data(self,optoion,callback):
        shop_list = config.get_shop_list(optoion)
        for shop in shop_list:
            name = shop["name"]
            cookie = shop["cookie"]
            homeDataWork = HomeDataWork(name,cookie)
            homeDataWork.signals.finished.connect(callback)
            self.threadpool.start(homeDataWork)
    
    #获取采购数据
    def request_purchase_data(self,isSelectPurchaseTime,dateStart,dateEnd,callback):
        purchase_list = config.get_purchase_list()
        for purchase in purchase_list:
            name = purchase["name"]
            cookie = purchase["cookie"]
            purchaseDataWork = PurchaseDataWork(name,cookie,isSelectPurchaseTime,dateStart,dateEnd)
            purchaseDataWork.signals.finished.connect(callback)
            self.threadpool.start(purchaseDataWork)

    
    #获取订单数据
    def request_order_data(self,selectShop,orderStart,orderEnd,callback):
        cookie = config.get_shop_cookie(selectShop)
        orderDataWork = OrderDataWork(cookie,orderStart,orderEnd)
        orderDataWork.signals.finished.connect(callback)
        self.threadpool.start(orderDataWork)


    #获取违规信息
    def request_violation_data(self,callback):
        myShopList = config.get_shop_list("我的店铺")
        for shop in myShopList:
            cookie = shop["cookie"]
            violationDataWork = ViolationDataWork(cookie)
            violationDataWork.signals.finished.connect(callback)
            self.threadpool.start(violationDataWork)

    #获取交易风险
    def request_transaction_data(self,callback):
        myShopList = config.get_shop_list("我的店铺")
        for shop in myShopList:
            cookie = shop["cookie"]
            transactionDataWork = TransactionDataWork(cookie)
            transactionDataWork.signals.finished.connect(callback)
            self.threadpool2.start(transactionDataWork)