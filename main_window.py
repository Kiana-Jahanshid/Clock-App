# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindowMzrweD.ui'
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
        self.ir = QPushButton(self.tab_2)
        self.ir.setObjectName(u"ir")
        self.ir.setGeometry(QRect(50, 100, 191, 61))
        font1 = QFont()
        font1.setFamily(u"Microsoft Sans Serif")
        font1.setPointSize(13)
        font1.setBold(False)
        font1.setItalic(False)
        self.ir.setFont(font1)
        self.ir.setStyleSheet(u"border-bottom-color: rgb(170, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 13pt \"Microsoft Sans Serif\";\n"
"background-color: rgb(58, 58, 58);")
        self.gr = QPushButton(self.tab_2)
        self.gr.setObjectName(u"gr")
        self.gr.setGeometry(QRect(50, 160, 191, 61))
        self.gr.setFont(font1)
        self.gr.setStyleSheet(u"border-bottom-color: rgb(170, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 13pt \"Microsoft Sans Serif\";\n"
"background-color: rgb(58, 58, 58);")
        self.usa = QPushButton(self.tab_2)
        self.usa.setObjectName(u"usa")
        self.usa.setGeometry(QRect(50, 220, 191, 61))
        self.usa.setFont(font1)
        self.usa.setStyleSheet(u"border-bottom-color: rgb(170, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 13pt \"Microsoft Sans Serif\";\n"
"background-color: rgb(58, 58, 58);")
        self.gr_time = QPushButton(self.tab_2)
        self.gr_time.setObjectName(u"gr_time")
        self.gr_time.setGeometry(QRect(240, 160, 191, 61))
        self.gr_time.setFont(font1)
        self.gr_time.setStyleSheet(u"border-bottom-color: rgb(170, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 13pt \"Microsoft Sans Serif\";\n"
"background-color: rgb(58, 58, 58);")
        self.us_time = QPushButton(self.tab_2)
        self.us_time.setObjectName(u"us_time")
        self.us_time.setGeometry(QRect(240, 220, 191, 61))
        self.us_time.setFont(font1)
        self.us_time.setStyleSheet(u"border-bottom-color: rgb(170, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 13pt \"Microsoft Sans Serif\";\n"
"background-color: rgb(58, 58, 58);")
        self.ir_time = QPushButton(self.tab_2)
        self.ir_time.setObjectName(u"ir_time")
        self.ir_time.setGeometry(QRect(240, 100, 191, 61))
        self.ir_time.setFont(font1)
        self.ir_time.setStyleSheet(u"border-bottom-color: rgb(170, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 13pt \"Microsoft Sans Serif\";\n"
"background-color: rgb(58, 58, 58);")
        self.title = QPushButton(self.tab_2)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(130, 30, 221, 31))
        self.title.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.tabWidget.addTab(self.tab_2, "")
        self.ir.raise_()
        self.gr.raise_()
        self.ir_time.raise_()
        self.gr_time.raise_()
        self.usa.raise_()
        self.us_time.raise_()
        self.title.raise_()
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.label_stopwatch = QLabel(self.tab_3)
        self.label_stopwatch.setObjectName(u"label_stopwatch")
        self.label_stopwatch.setGeometry(QRect(100, 20, 281, 161))
        font2 = QFont()
        font2.setFamily(u"Seven Segment")
        font2.setPointSize(70)
        font2.setBold(False)
        self.label_stopwatch.setFont(font2)
        self.label_stopwatch.setStyleSheet(u"color: rgb(0, 250, 30);")
        self.label_stopwatch.setAlignment(Qt.AlignCenter)
        self.btn_start_stopwatch = QPushButton(self.tab_3)
        self.btn_start_stopwatch.setObjectName(u"btn_start_stopwatch")
        self.btn_start_stopwatch.setGeometry(QRect(100, 210, 81, 81))
        font3 = QFont()
        font3.setPointSize(14)
        self.btn_start_stopwatch.setFont(font3)
        self.btn_start_stopwatch.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(37, 200, 100);\n"
"border-radius: 40px ;")
        self.btn_stop_stopwatch = QPushButton(self.tab_3)
        self.btn_stop_stopwatch.setObjectName(u"btn_stop_stopwatch")
        self.btn_stop_stopwatch.setGeometry(QRect(200, 210, 81, 81))
        font4 = QFont()
        font4.setPointSize(14)
        font4.setBold(False)
        self.btn_stop_stopwatch.setFont(font4)
        self.btn_stop_stopwatch.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-radius: 40px ;\n"
"background-color: rgb(135, 120, 135);")
        self.btn_reset_stopwatch = QPushButton(self.tab_3)
        self.btn_reset_stopwatch.setObjectName(u"btn_reset_stopwatch")
        self.btn_reset_stopwatch.setGeometry(QRect(300, 210, 81, 81))
        self.btn_reset_stopwatch.setFont(font4)
        self.btn_reset_stopwatch.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-radius: 40px ;\n"
"background-color: rgb(0, 118, 102);")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.textbox_hour_timer = QLineEdit(self.tab_4)
        self.textbox_hour_timer.setObjectName(u"textbox_hour_timer")
        self.textbox_hour_timer.setGeometry(QRect(80, 60, 101, 91))
        font5 = QFont()
        font5.setFamily(u"Seven Segment")
        font5.setPointSize(50)
        self.textbox_hour_timer.setFont(font5)
        self.textbox_hour_timer.setStyleSheet(u"color: rgb(242, 98, 0);")
        self.textbox_hour_timer.setAlignment(Qt.AlignCenter)
        self.textbox_minute_timer = QLineEdit(self.tab_4)
        self.textbox_minute_timer.setObjectName(u"textbox_minute_timer")
        self.textbox_minute_timer.setGeometry(QRect(190, 60, 101, 91))
        self.textbox_minute_timer.setFont(font5)
        self.textbox_minute_timer.setStyleSheet(u"color: rgb(242, 98, 0);")
        self.textbox_minute_timer.setAlignment(Qt.AlignCenter)
        self.textbox_second_timer = QLineEdit(self.tab_4)
        self.textbox_second_timer.setObjectName(u"textbox_second_timer")
        self.textbox_second_timer.setGeometry(QRect(300, 60, 101, 91))
        self.textbox_second_timer.setFont(font5)
        self.textbox_second_timer.setStyleSheet(u"color: rgb(242, 98, 0);")
        self.textbox_second_timer.setAlignment(Qt.AlignCenter)
        self.btn_start_timer = QPushButton(self.tab_4)
        self.btn_start_timer.setObjectName(u"btn_start_timer")
        self.btn_start_timer.setGeometry(QRect(100, 210, 81, 81))
        font6 = QFont()
        font6.setPointSize(13)
        self.btn_start_timer.setFont(font6)
        self.btn_start_timer.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-radius: 40px ;\n"
"background-color: rgb(242, 0, 0);")
        self.btn_stop_timer = QPushButton(self.tab_4)
        self.btn_stop_timer.setObjectName(u"btn_stop_timer")
        self.btn_stop_timer.setGeometry(QRect(200, 210, 81, 81))
        font7 = QFont()
        font7.setPointSize(13)
        font7.setBold(False)
        self.btn_stop_timer.setFont(font7)
        self.btn_stop_timer.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-radius: 40px ;\n"
"background-color: rgb(242, 110, 0);")
        self.btn_reset_timer = QPushButton(self.tab_4)
        self.btn_reset_timer.setObjectName(u"btn_reset_timer")
        self.btn_reset_timer.setGeometry(QRect(300, 210, 81, 81))
        self.btn_reset_timer.setFont(font4)
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

        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.ir.setText(QCoreApplication.translate("MainWindow", u"IRAN", None))
        self.gr.setText(QCoreApplication.translate("MainWindow", u"GERMANY", None))
        self.usa.setText(QCoreApplication.translate("MainWindow", u"USA", None))
        self.gr_time.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.us_time.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.ir_time.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"W🌎rld Cl🕜ck", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"World Clock", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Alarm", None))
        self.label_stopwatch.setText(QCoreApplication.translate("MainWindow", u"0:0:0", None))
        self.btn_start_stopwatch.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.btn_stop_stopwatch.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.btn_reset_stopwatch.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"StopWatch", None))
        self.textbox_hour_timer.setText("")
        self.textbox_minute_timer.setText("")
        self.textbox_second_timer.setText("")
        self.btn_start_timer.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.btn_stop_timer.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.btn_reset_timer.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Timer", None))
    # retranslateUi

