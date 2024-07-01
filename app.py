import sys
from PyQt6 import QtWidgets, QtCore
from ui.ui import Ui_MainWindow

from datetime import datetime, timedelta
from PyQt6.QtCore import QDate,QFileSystemWatcher
import urllib3
from data.request_data import RequestData
from data.constant import Contants

class MyApp(QtWidgets.QMainWindow):

    sign_chart = QtCore.pyqtSignal(dict)

    def __init__(self):
        super().__init__()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.threadpool = QtCore.QThreadPool()
        self.threadpool.setMaxThreadCount(3)
        self.apply_stylesheet()
        self.setup_ui()
        self.setup_table_widget()


        requestData = RequestData()
        requestData.request_data(self.data_load_callback)

    def setup_table_widget(self):
        """设置表格控件"""
        header = self.ui.tableWidget.horizontalHeader()
        self.ui.tableWidget.setColumnCount(9)
        self.ui.tableWidget.setRowCount(0)  # 初始行数为0，可以根据需要调整
        self.ui.tableWidget.setColumnWidth(Contants.index_name, 140)
        self.ui.tableWidget.setColumnWidth(Contants.index_deal_amount_value, 80)
        self.ui.tableWidget.setColumnWidth(Contants.index_deal_relative_cycle, 80)
        self.ui.tableWidget.setColumnWidth(Contants.index_deal_ranking_interval, 80)
        self.ui.tableWidget.setColumnWidth(Contants.index_transaction_turnover, 80)
        self.ui.tableWidget.setColumnWidth(Contants.index_transaction_relative_cycle, 80)
        self.ui.tableWidget.setColumnWidth(Contants.index_average_price, 80)
        self.ui.tableWidget.setColumnWidth(Contants.index_refund_amount_value, 80)
        self.ui.tableWidget.setColumnWidth(Contants.index_refund_relative_cycle, 80)

    def data_load_callback(self,data,shopName):
        if data["code"] !=0:
            return
        shopData = data["data"]

        dealAmount = shopData["dealAmount"]
        dealAmountValue = dealAmount["amount"] #今日营业额
        dealRelativeCycle = dealAmount["relativeCycle"] #营业额环比
        dealRankingInterval = dealAmount["rankingInterval"] #成交额排名

        transactionVolume = shopData["transactionVolume"]
        transactionTurnover = transactionVolume["turnover"] #成交单量
        transactionRelativeCycle = transactionVolume["relativeCycle"] #单量环比


        singleAveragePrice = shopData["singleAveragePrice"]
        averagePrice = singleAveragePrice["averagePrice"] #单均价

        refundAmount = shopData["refundAmount"]
        refundAmountValue = refundAmount["amount"] #退款金额
        refundRelativeCycle = refundAmount["relativeCycle"] #退款金额环比

    
        row_position = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(row_position)
        
        #店铺名称
        shopName = QtWidgets.QTableWidgetItem(str(shopName))
        self.ui.tableWidget.setItem(row_position, Contants.index_name, shopName)

        #营业额
        dealAmountValueItem = QtWidgets.QTableWidgetItem(str(dealAmountValue))
        self.ui.tableWidget.setItem(row_position, Contants.index_deal_amount_value, dealAmountValueItem)
        
        #营业额环比
        dealRelativeCycleItem = QtWidgets.QTableWidgetItem(str(dealRelativeCycle))
        self.ui.tableWidget.setItem(row_position, Contants.index_deal_relative_cycle, dealRelativeCycleItem)
        
        #营业额排名
        dealRankingIntervalItem = QtWidgets.QTableWidgetItem(str(dealRankingInterval))
        self.ui.tableWidget.setItem(row_position, Contants.index_deal_ranking_interval, dealRankingIntervalItem)
        
        #成交单量
        transactionTurnoverItem = QtWidgets.QTableWidgetItem(str(transactionTurnover))
        self.ui.tableWidget.setItem(row_position, Contants.index_transaction_turnover, transactionTurnoverItem)
        
        #单量环比
        transactionRelativeCycleItem = QtWidgets.QTableWidgetItem(str(transactionRelativeCycle))
        self.ui.tableWidget.setItem(row_position, Contants.index_transaction_relative_cycle, transactionRelativeCycleItem)
              
        #单均价
        averagePriceItem = QtWidgets.QTableWidgetItem(str(averagePrice))
        self.ui.tableWidget.setItem(row_position, Contants.index_average_price, averagePriceItem)
        

        #退款金额
        refundAmountValueItem = QtWidgets.QTableWidgetItem(str(refundAmountValue))
        self.ui.tableWidget.setItem(row_position, Contants.index_refund_amount_value, refundAmountValueItem)
        

        #退款金额环比
        refundRelativeCycleItem = QtWidgets.QTableWidgetItem(str(refundRelativeCycle))
        self.ui.tableWidget.setItem(row_position, Contants.index_refund_relative_cycle, refundRelativeCycleItem)
        

        self.ui.tableWidget.update()

         # 判断是否所有任务已经完成
        active_threads = self.threadpool.activeThreadCount()
        if active_threads == 0:
            print("已加载完成")

    def apply_stylesheet(self):
        QtWidgets.QApplication.setStyle("Fusion")
        QtWidgets.QApplication.setPalette(QtWidgets.QApplication.style().standardPalette())


    def setup_network(self):
        # 发起请求时忽略证书验证警告
        urllib3.disable_warnings()

    def setup_ui(self):
        pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MyApp()
    mainWindow.show()
    sys.exit(app.exec())