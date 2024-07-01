import sys
from PyQt6 import QtWidgets, QtCore
from ui.ui import Ui_MainWindow

from datetime import datetime, timedelta
from PyQt6.QtCore import QDate,QFileSystemWatcher
import urllib3
from data.request_data import RequestData

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
        self.ui.tableWidget.setColumnCount(3)
        self.ui.tableWidget.setRowCount(0)  # 初始行数为0，可以根据需要调整

    def data_load_callback(self,data):
        if data["code"] !=0:
            return
        shopData = data["data"]

        dealAmount = shopData["dealAmount"]
        dealAmountValue = dealAmount["amount"] #今日营业额
        dealRelativeCycle = dealAmount["relativeCycle"] #营业额环比
        dealRankingInterval = dealAmount["rankingInterval"] #排名

        transactionVolume = shopData["transactionVolume"]
        transactionTurnover = transactionVolume["turnover"] #成交单量
        transactionRelativeCycle = transactionVolume["relativeCycle"] #单量环比


        singleAveragePrice = shopData["singleAveragePrice"]
        averagePrice = singleAveragePrice["averagePrice"] #单均价

        refundAmount = shopData["refundAmount"]
        refundAmountValue = refundAmount["amount"] #退款金额
        refundRelativeCycle = refundAmount["relativeCycle"] #退款金额环比

        dealAmountValueItem = QtWidgets.QTableWidgetItem(str(dealAmountValue))

        row_position = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(row_position)

        self.ui.tableWidget.setItem(row_position, 0, dealAmountValueItem)
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