from PyQt6 import QtCore
from config import config
from worker.home_data_work import HomeDataWork

class RequestData:

    def __init__(self):
        super().__init__()
        self.threadpool = QtCore.QThreadPool()
        self.threadpool.setMaxThreadCount(3)



    def request_data(self,callback):


        shop_list = config.get_shop_list()
        for shop in shop_list:
            name = shop["name"]
            cookie = shop["cookie"]
            homeDataWork = HomeDataWork(name,cookie)
            homeDataWork.signals.finished.connect(callback)
            self.threadpool.start(homeDataWork)