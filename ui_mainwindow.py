# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindowhFqrlk.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(579, 462)
        MainWindow.setStyleSheet(u"background-color: rgb(26, 26, 26);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(50, 30, 481, 361))
        font = QFont()
        font.setPointSize(8)
        self.tabWidget.setFont(font)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.pushButton = QPushButton(self.tab_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(110, 200, 93, 28))
        self.pushButton_2 = QPushButton(self.tab_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(290, 200, 93, 28))
        self.label = QLabel(self.tab_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(220, 50, 211, 61))
        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.label_stopwatch = QLabel(self.tab_3)
        self.label_stopwatch.setObjectName(u"label_stopwatch")
        self.label_stopwatch.setGeometry(QRect(100, 20, 281, 161))
        font1 = QFont()
        font1.setFamily(u"Seven Segment")
        font1.setPointSize(70)
        font1.setBold(False)
        self.label_stopwatch.setFont(font1)
        self.label_stopwatch.setStyleSheet(u"color: rgb(0, 250, 30);")
        self.label_stopwatch.setAlignment(Qt.AlignCenter)
        self.btn_start_stopwatch = QPushButton(self.tab_3)
        self.btn_start_stopwatch.setObjectName(u"btn_start_stopwatch")
        self.btn_start_stopwatch.setGeometry(QRect(100, 210, 81, 81))
        font2 = QFont()
        font2.setPointSize(14)
        self.btn_start_stopwatch.setFont(font2)
        self.btn_start_stopwatch.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(37, 200, 100);\n"
"border-radius: 40px ;")
        self.btn_stop_stopwatch = QPushButton(self.tab_3)
        self.btn_stop_stopwatch.setObjectName(u"btn_stop_stopwatch")
        self.btn_stop_stopwatch.setGeometry(QRect(200, 210, 81, 81))
        font3 = QFont()
        font3.setPointSize(14)
        font3.setBold(False)
        self.btn_stop_stopwatch.setFont(font3)
        self.btn_stop_stopwatch.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-radius: 40px ;\n"
"background-color: rgb(135, 120, 135);")
        self.btn_reset_stopwatch = QPushButton(self.tab_3)
        self.btn_reset_stopwatch.setObjectName(u"btn_reset_stopwatch")
        self.btn_reset_stopwatch.setGeometry(QRect(300, 210, 81, 81))
        self.btn_reset_stopwatch.setFont(font3)
        self.btn_reset_stopwatch.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-radius: 40px ;\n"
"background-color: rgb(0, 118, 102);")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.textbox_hour_timer = QLineEdit(self.tab_4)
        self.textbox_hour_timer.setObjectName(u"textbox_hour_timer")
        self.textbox_hour_timer.setGeometry(QRect(80, 60, 101, 91))
        font4 = QFont()
        font4.setFamily(u"Seven Segment")
        font4.setPointSize(50)
        self.textbox_hour_timer.setFont(font4)
        self.textbox_hour_timer.setStyleSheet(u"color: rgb(242, 98, 0);")
        self.textbox_hour_timer.setAlignment(Qt.AlignCenter)
        self.textbox_minute_timer = QLineEdit(self.tab_4)
        self.textbox_minute_timer.setObjectName(u"textbox_minute_timer")
        self.textbox_minute_timer.setGeometry(QRect(190, 60, 101, 91))
        self.textbox_minute_timer.setFont(font4)
        self.textbox_minute_timer.setStyleSheet(u"color: rgb(242, 98, 0);")
        self.textbox_minute_timer.setAlignment(Qt.AlignCenter)
        self.textbox_second_timer = QLineEdit(self.tab_4)
        self.textbox_second_timer.setObjectName(u"textbox_second_timer")
        self.textbox_second_timer.setGeometry(QRect(300, 60, 101, 91))
        self.textbox_second_timer.setFont(font4)
        self.textbox_second_timer.setStyleSheet(u"color: rgb(242, 98, 0);")
        self.textbox_second_timer.setAlignment(Qt.AlignCenter)
        self.btn_start_timer = QPushButton(self.tab_4)
        self.btn_start_timer.setObjectName(u"btn_start_timer")
        self.btn_start_timer.setGeometry(QRect(100, 210, 81, 81))
        font5 = QFont()
        font5.setPointSize(13)
        self.btn_start_timer.setFont(font5)
        self.btn_start_timer.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-radius: 40px ;\n"
"background-color: rgb(242, 0, 0);")
        self.btn_stop_timer = QPushButton(self.tab_4)
        self.btn_stop_timer.setObjectName(u"btn_stop_timer")
        self.btn_stop_timer.setGeometry(QRect(200, 210, 81, 81))
        font6 = QFont()
        font6.setPointSize(13)
        font6.setBold(False)
        self.btn_stop_timer.setFont(font6)
        self.btn_stop_timer.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-radius: 40px ;\n"
"background-color: rgb(242, 110, 0);")
        self.btn_reset_timer = QPushButton(self.tab_4)
        self.btn_reset_timer.setObjectName(u"btn_reset_timer")
        self.btn_reset_timer.setGeometry(QRect(300, 210, 81, 81))
        self.btn_reset_timer.setFont(font3)
        self.btn_reset_timer.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-radius: 40px ;\n"
"background-color: rgb(234, 179, 103);")
        self.tabWidget.addTab(self.tab_4, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 579, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"World Clock", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Alarm", None))
        self.label_stopwatch.setText(QCoreApplication.translate("MainWindow", u"0:0:0", None))
        self.btn_start_stopwatch.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.btn_stop_stopwatch.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.btn_reset_stopwatch.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"StopWatch", None))
        self.textbox_hour_timer.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.textbox_minute_timer.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.textbox_second_timer.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_start_timer.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.btn_stop_timer.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.btn_reset_timer.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Timer", None))
    # retranslateUi

