# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDateTimeEdit,
    QHBoxLayout, QHeaderView, QLabel, QLayout,
    QMainWindow, QMenuBar, QPushButton, QRadioButton,
    QSizePolicy, QStatusBar, QTabWidget, QTableWidget,
    QTableWidgetItem, QTreeWidget, QTreeWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1001, 585)
        font = QFont()
        font.setPointSize(14)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 10, 1001, 541))
        self.tabWidget.setTabletTracking(False)
        self.tabWidget.setFocusPolicy(Qt.TabFocus)
        self.tabWidget.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.tabWidget.setLayoutDirection(Qt.LeftToRight)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tableWidget = QTableWidget(self.tab)
        if (self.tableWidget.columnCount() < 9):
            self.tableWidget.setColumnCount(9)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(0, 10, 981, 421))
        self.horizontalLayoutWidget = QWidget(self.tab)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(510, 440, 471, 34))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.cbShop = QComboBox(self.horizontalLayoutWidget)
        self.cbShop.addItem("")
        self.cbShop.addItem("")
        self.cbShop.setObjectName(u"cbShop")

        self.horizontalLayout.addWidget(self.cbShop)

        self.btnRefreshData = QPushButton(self.horizontalLayoutWidget)
        self.btnRefreshData.setObjectName(u"btnRefreshData")

        self.horizontalLayout.addWidget(self.btnRefreshData)

        self.amountCount = QLabel(self.horizontalLayoutWidget)
        self.amountCount.setObjectName(u"amountCount")
        self.amountCount.setLayoutDirection(Qt.RightToLeft)
        self.amountCount.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.amountCount)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.purchaseTable = QTableWidget(self.tab_2)
        if (self.purchaseTable.columnCount() < 9):
            self.purchaseTable.setColumnCount(9)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.purchaseTable.setHorizontalHeaderItem(0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.purchaseTable.setHorizontalHeaderItem(1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.purchaseTable.setHorizontalHeaderItem(2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.purchaseTable.setHorizontalHeaderItem(3, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.purchaseTable.setHorizontalHeaderItem(4, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.purchaseTable.setHorizontalHeaderItem(5, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.purchaseTable.setHorizontalHeaderItem(6, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.purchaseTable.setHorizontalHeaderItem(7, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.purchaseTable.setHorizontalHeaderItem(8, __qtablewidgetitem17)
        self.purchaseTable.setObjectName(u"purchaseTable")
        self.purchaseTable.setGeometry(QRect(0, 10, 981, 421))
        self.horizontalLayoutWidget_2 = QWidget(self.tab_2)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(680, 440, 301, 34))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btnRefreshPurchaseData = QPushButton(self.horizontalLayoutWidget_2)
        self.btnRefreshPurchaseData.setObjectName(u"btnRefreshPurchaseData")

        self.horizontalLayout_2.addWidget(self.btnRefreshPurchaseData)

        self.horizontalLayoutWidget_3 = QWidget(self.tab_2)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(10, 440, 206, 31))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.rbPurchase = QRadioButton(self.horizontalLayoutWidget_3)
        self.rbPurchase.setObjectName(u"rbPurchase")
        self.rbPurchase.setChecked(True)

        self.horizontalLayout_3.addWidget(self.rbPurchase)

        self.rbPlace = QRadioButton(self.horizontalLayoutWidget_3)
        self.rbPlace.setObjectName(u"rbPlace")

        self.horizontalLayout_3.addWidget(self.rbPlace)

        self.horizontalLayoutWidget_4 = QWidget(self.tab_2)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(230, 440, 428, 34))
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.horizontalLayoutWidget_4)
        self.label.setObjectName(u"label")
        self.label.setLayoutDirection(Qt.RightToLeft)

        self.horizontalLayout_4.addWidget(self.label)

        self.dateStart = QDateEdit(self.horizontalLayoutWidget_4)
        self.dateStart.setObjectName(u"dateStart")
        self.dateStart.setCalendarPopup(True)

        self.horizontalLayout_4.addWidget(self.dateStart)

        self.label_2 = QLabel(self.horizontalLayoutWidget_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setLayoutDirection(Qt.RightToLeft)

        self.horizontalLayout_4.addWidget(self.label_2)

        self.dateEnd = QDateEdit(self.horizontalLayoutWidget_4)
        self.dateEnd.setObjectName(u"dateEnd")
        self.dateEnd.setCalendarPopup(True)

        self.horizontalLayout_4.addWidget(self.dateEnd)

        self.labelPurchase = QLabel(self.tab_2)
        self.labelPurchase.setObjectName(u"labelPurchase")
        self.labelPurchase.setGeometry(QRect(10, 476, 971, 32))
        self.labelPurchase.setLayoutDirection(Qt.RightToLeft)
        self.labelPurchase.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tableOrder = QTableWidget(self.tab_3)
        if (self.tableOrder.columnCount() < 12):
            self.tableOrder.setColumnCount(12)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableOrder.setHorizontalHeaderItem(0, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableOrder.setHorizontalHeaderItem(1, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableOrder.setHorizontalHeaderItem(2, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableOrder.setHorizontalHeaderItem(3, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableOrder.setHorizontalHeaderItem(4, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableOrder.setHorizontalHeaderItem(5, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableOrder.setHorizontalHeaderItem(6, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableOrder.setHorizontalHeaderItem(7, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableOrder.setHorizontalHeaderItem(8, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tableOrder.setHorizontalHeaderItem(9, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tableOrder.setHorizontalHeaderItem(10, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tableOrder.setHorizontalHeaderItem(11, __qtablewidgetitem29)
        self.tableOrder.setObjectName(u"tableOrder")
        self.tableOrder.setGeometry(QRect(0, 10, 981, 421))
        self.horizontalLayoutWidget_5 = QWidget(self.tab_3)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(0, 440, 981, 34))
        self.horizontalLayout_5 = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setSizeConstraint(QLayout.SetNoConstraint)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.horizontalLayoutWidget_5)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(100, 16777215))
        self.label_3.setBaseSize(QSize(0, 0))
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_3.setWordWrap(False)

        self.horizontalLayout_5.addWidget(self.label_3)

        self.cbOrderShop = QComboBox(self.horizontalLayoutWidget_5)
        self.cbOrderShop.setObjectName(u"cbOrderShop")
        self.cbOrderShop.setMaxVisibleItems(20)

        self.horizontalLayout_5.addWidget(self.cbOrderShop)

        self.label_4 = QLabel(self.horizontalLayoutWidget_5)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(100, 16777215))
        self.label_4.setLayoutDirection(Qt.RightToLeft)
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_4)

        self.dataStartOrder = QDateTimeEdit(self.horizontalLayoutWidget_5)
        self.dataStartOrder.setObjectName(u"dataStartOrder")
        self.dataStartOrder.setCalendarPopup(True)

        self.horizontalLayout_5.addWidget(self.dataStartOrder)

        self.label_5 = QLabel(self.horizontalLayoutWidget_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(100, 16777215))
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_5)

        self.dataEndOrder = QDateTimeEdit(self.horizontalLayoutWidget_5)
        self.dataEndOrder.setObjectName(u"dataEndOrder")
        self.dataEndOrder.setCalendarPopup(True)

        self.horizontalLayout_5.addWidget(self.dataEndOrder)

        self.btnShopOrder = QPushButton(self.horizontalLayoutWidget_5)
        self.btnShopOrder.setObjectName(u"btnShopOrder")
        self.btnShopOrder.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_5.addWidget(self.btnShopOrder)

        self.btnExportOrder = QPushButton(self.horizontalLayoutWidget_5)
        self.btnExportOrder.setObjectName(u"btnExportOrder")

        self.horizontalLayout_5.addWidget(self.btnExportOrder)

        self.horizontalLayout_5.setStretch(6, 1)
        self.horizontalLayout_5.setStretch(7, 1)
        self.labelBottomOrfer = QLabel(self.tab_3)
        self.labelBottomOrfer.setObjectName(u"labelBottomOrfer")
        self.labelBottomOrfer.setGeometry(QRect(0, 476, 981, 20))
        self.labelBottomOrfer.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.treeViolation = QTreeWidget(self.tab_5)
        self.treeViolation.setObjectName(u"treeViolation")
        self.treeViolation.setGeometry(QRect(10, 0, 591, 471))
        self.treeViolation.setTabletTracking(False)
        self.tabWidget.addTab(self.tab_5, "")
        self.btnMini = QPushButton(self.centralwidget)
        self.btnMini.setObjectName(u"btnMini")
        self.btnMini.setGeometry(QRect(940, 5, 24, 24))
        self.btnMini.setAutoFillBackground(False)
        self.btnMini.setStyleSheet(u"background:rgba(0,0,0,0);\n"
"border-image: url(./res/mini_icon.png)\n"
"\n"
"")
        self.btnClose = QPushButton(self.centralwidget)
        self.btnClose.setObjectName(u"btnClose")
        self.btnClose.setGeometry(QRect(970, 5, 24, 24))
        self.btnClose.setAutoFillBackground(False)
        self.btnClose.setStyleSheet(u"background:rgba(0,0,0,0);\n"
"border-image: url(./res/close_icon.png)\n"
"\n"
"")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1001, 30))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u7f8e\u56e2\u8f85\u52a9", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u5e97\u94fa\u540d\u79f0", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u4eca\u65e5\u8425\u4e1a\u989d", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u8425\u4e1a\u989d\u73af\u6bd4", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u8425\u4e1a\u989d\u6392\u540d", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u6210\u4ea4\u5355\u91cf", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u5355\u91cf\u73af\u6bd4", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u8ba2\u5355\u5747\u4ef7", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\u9000\u6b3e\u91d1\u989d", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\u9000\u6b3e\u91d1\u989d\u73af\u6bd4", None));
        self.cbShop.setItemText(0, QCoreApplication.translate("MainWindow", u"\u6211\u7684\u5e97\u94fa", None))
        self.cbShop.setItemText(1, QCoreApplication.translate("MainWindow", u"\u540c\u884c\u5e97\u94fa", None))

        self.btnRefreshData.setText(QCoreApplication.translate("MainWindow", u"\u5237\u65b0\u6570\u636e", None))
        self.amountCount.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u5e97\u94fa\u6570\u636e", None))
        ___qtablewidgetitem9 = self.purchaseTable.horizontalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"\u5e97\u94fa\u540d\u79f0", None));
        ___qtablewidgetitem10 = self.purchaseTable.horizontalHeaderItem(1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"\u8ba2\u5355\u91cf", None));
        ___qtablewidgetitem11 = self.purchaseTable.horizontalHeaderItem(2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"\u91c7\u8d2d\u65f6\u95f4", None));
        ___qtablewidgetitem12 = self.purchaseTable.horizontalHeaderItem(3)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u5355\u65f6\u95f4", None));
        ___qtablewidgetitem13 = self.purchaseTable.horizontalHeaderItem(4)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"\u8ba2\u5355\u91d1\u989d", None));
        ___qtablewidgetitem14 = self.purchaseTable.horizontalHeaderItem(5)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"\u9884\u8ba1\u6536\u5165", None));
        ___qtablewidgetitem15 = self.purchaseTable.horizontalHeaderItem(6)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"\u91c7\u8d2d\u6210\u672c", None));
        ___qtablewidgetitem16 = self.purchaseTable.horizontalHeaderItem(7)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"\u5229\u6da6", None));
        ___qtablewidgetitem17 = self.purchaseTable.horizontalHeaderItem(8)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"\u5229\u6da6\u7387", None));
        self.btnRefreshPurchaseData.setText(QCoreApplication.translate("MainWindow", u"\u5237\u65b0\u6570\u636e", None))
        self.rbPurchase.setText(QCoreApplication.translate("MainWindow", u"\u91c7\u8d2d\u65f6\u95f4", None))
        self.rbPlace.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u5355\u65f6\u95f4", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u65e5\u671f", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u7ed3\u675f\u65e5\u671f", None))
        self.labelPurchase.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u91c7\u8d2d\u6570\u636e", None))
        ___qtablewidgetitem18 = self.tableOrder.horizontalHeaderItem(0)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"\u8ba2\u5355\u53f7", None));
        ___qtablewidgetitem19 = self.tableOrder.horizontalHeaderItem(1)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"\u4ea7\u54c1\u540d", None));
        ___qtablewidgetitem20 = self.tableOrder.horizontalHeaderItem(2)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u5355\u65f6\u95f4", None));
        ___qtablewidgetitem21 = self.tableOrder.horizontalHeaderItem(3)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"\u8ba2\u5355\u72b6\u6001", None));
        ___qtablewidgetitem22 = self.tableOrder.horizontalHeaderItem(4)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"\u8d2d\u4e70\u6570\u91cf", None));
        ___qtablewidgetitem23 = self.tableOrder.horizontalHeaderItem(5)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"\u8d2d\u4e70\u5355\u4ef7", None));
        ___qtablewidgetitem24 = self.tableOrder.horizontalHeaderItem(6)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"\u8ba2\u5355\u91d1\u989d", None));
        ___qtablewidgetitem25 = self.tableOrder.horizontalHeaderItem(7)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"\u6536\u8d27\u4eba", None));
        ___qtablewidgetitem26 = self.tableOrder.horizontalHeaderItem(8)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"\u6536\u8d27\u7535\u8bdd", None));
        ___qtablewidgetitem27 = self.tableOrder.horizontalHeaderItem(9)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"\u6536\u8d27\u5730\u5740", None));
        ___qtablewidgetitem28 = self.tableOrder.horizontalHeaderItem(10)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u5355\u6e20\u9053", None));
        ___qtablewidgetitem29 = self.tableOrder.horizontalHeaderItem(11)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"\u662f\u5426\u5237\u5355", None));
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u5e97\u94fa\uff1a", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u65f6\u95f4\uff1a", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u7ed3\u675f\u65f6\u95f4\uff1a", None))
        self.btnShopOrder.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u8be2", None))
        self.btnExportOrder.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa", None))
        self.labelBottomOrfer.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"\u5e97\u94fa\u8ba2\u5355", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"\u4e3b\u56fe\u66ff\u6362", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"\u8fdd\u89c4\u4fe1\u606f", None))
        self.btnMini.setText("")
        self.btnClose.setText("")
    # retranslateUi

