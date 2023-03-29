# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindownYgiml.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt , QDate)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(580, 463)
        MainWindow.setStyleSheet(u"background-color: rgb(26, 26, 26);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(50, 30, 481, 371))
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
        self.ir.setGeometry(QRect(50, 110, 191, 61))
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
        self.gr.setGeometry(QRect(50, 170, 191, 61))
        self.gr.setFont(font1)
        self.gr.setStyleSheet(u"border-bottom-color: rgb(170, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 13pt \"Microsoft Sans Serif\";\n"
"background-color: rgb(58, 58, 58);")
        self.usa = QPushButton(self.tab_2)
        self.usa.setObjectName(u"usa")
        self.usa.setGeometry(QRect(50, 230, 191, 61))
        self.usa.setFont(font1)
        self.usa.setStyleSheet(u"border-bottom-color: rgb(170, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 13pt \"Microsoft Sans Serif\";\n"
"background-color: rgb(58, 58, 58);")
        self.gr_time = QPushButton(self.tab_2)
        self.gr_time.setObjectName(u"gr_time")
        self.gr_time.setGeometry(QRect(240, 170, 191, 61))
        self.gr_time.setFont(font1)
        self.gr_time.setStyleSheet(u"border-bottom-color: rgb(170, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 13pt \"Microsoft Sans Serif\";\n"
"background-color: rgb(58, 58, 58);")
        self.us_time = QPushButton(self.tab_2)
        self.us_time.setObjectName(u"us_time")
        self.us_time.setGeometry(QRect(240, 230, 191, 61))
        self.us_time.setFont(font1)
        self.us_time.setStyleSheet(u"border-bottom-color: rgb(170, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 13pt \"Microsoft Sans Serif\";\n"
"background-color: rgb(58, 58, 58);")
        self.ir_time = QPushButton(self.tab_2)
        self.ir_time.setObjectName(u"ir_time")
        self.ir_time.setGeometry(QRect(240, 110, 191, 61))
        self.ir_time.setFont(font1)
        self.ir_time.setStyleSheet(u"border-bottom-color: rgb(170, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 13pt \"Microsoft Sans Serif\";\n"
"background-color: rgb(58, 58, 58);")
        self.title = QPushButton(self.tab_2)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(130, 40, 221, 31))
        self.title.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"border-radius: 3px ;")
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
        self.gridLayoutWidget = QWidget(self.tab)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(50, 200, 281, 131))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setFamily(u"MV Boli")
        font2.setPointSize(11)
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.52, y1:1, x2:0.531421, y2:0.318, stop:0 rgba(232, 232, 232, 0), stop:1 rgba(255, 255, 255, 0));\n"
"color: rgb(170, 85, 255);")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.tb_new_task_title = QLineEdit(self.gridLayoutWidget)
        self.tb_new_task_title.setObjectName(u"tb_new_task_title")
        self.tb_new_task_title.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tb_new_task_title.sizePolicy().hasHeightForWidth())
        self.tb_new_task_title.setSizePolicy(sizePolicy1)
        self.tb_new_task_title.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"font: 11pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;")

        self.gridLayout.addWidget(self.tb_new_task_title, 1, 0, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setFont(font2)
        self.label_4.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.52, y1:1, x2:0.531421, y2:0.318, stop:0 rgba(232, 232, 232, 0), stop:1 rgba(255, 255, 255, 0));\n"
"color: rgb(170, 85, 255);")

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)

        self.comboBox = QComboBox(self.gridLayoutWidget)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.comboBox, 5, 0, 1, 1)

        self.timeEdit = QTimeEdit(self.gridLayoutWidget)
        self.timeEdit.setObjectName(u"timeEdit")
        font3 = QFont()
        font3.setFamily(u"MS Shell Dlg 2")
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        self.timeEdit.setFont(font3)
        self.timeEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.timeEdit.setMaximumDate(QDate(2000, 1, 1))

        self.gridLayout.addWidget(self.timeEdit, 3, 0, 1, 1)

        self.label_5 = QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setFont(font2)
        self.label_5.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.52, y1:1, x2:0.531421, y2:0.318, stop:0 rgba(232, 232, 232, 0), stop:1 rgba(255, 255, 255, 0));\n"
"color: rgb(170, 85, 255);")

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.btn_new_alarm = QPushButton(self.tab)
        self.btn_new_alarm.setObjectName(u"btn_new_alarm")
        self.btn_new_alarm.setGeometry(QRect(370, 230, 71, 71))
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_new_alarm.sizePolicy().hasHeightForWidth())
        self.btn_new_alarm.setSizePolicy(sizePolicy2)
        font4 = QFont()
        font4.setFamily(u"MS Shell Dlg 2")
        font4.setPointSize(22)
        font4.setBold(True)
        self.btn_new_alarm.setFont(font4)
        self.btn_new_alarm.setLayoutDirection(Qt.LeftToRight)
        self.btn_new_alarm.setStyleSheet(u"border-radius: 35px;\n"
"background-color: rgb(170, 85, 255);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.gridLayoutWidget_2 = QWidget(self.tab)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(30, 20, 421, 161))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.label_stopwatch = QLabel(self.tab_3)
        self.label_stopwatch.setObjectName(u"label_stopwatch")
        self.label_stopwatch.setGeometry(QRect(100, 20, 281, 161))
        font5 = QFont()
        font5.setFamily(u"Seven Segment")
        font5.setPointSize(70)
        font5.setBold(False)
        self.label_stopwatch.setFont(font5)
        self.label_stopwatch.setStyleSheet(u"color: rgb(0, 250, 30);")
        self.label_stopwatch.setAlignment(Qt.AlignCenter)
        self.btn_start_stopwatch = QPushButton(self.tab_3)
        self.btn_start_stopwatch.setObjectName(u"btn_start_stopwatch")
        self.btn_start_stopwatch.setGeometry(QRect(100, 210, 81, 81))
        font6 = QFont()
        font6.setPointSize(14)
        self.btn_start_stopwatch.setFont(font6)
        self.btn_start_stopwatch.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(37, 200, 100);\n"
"border-radius: 40px ;")
        self.btn_stop_stopwatch = QPushButton(self.tab_3)
        self.btn_stop_stopwatch.setObjectName(u"btn_stop_stopwatch")
        self.btn_stop_stopwatch.setGeometry(QRect(200, 210, 81, 81))
        font7 = QFont()
        font7.setPointSize(14)
        font7.setBold(False)
        self.btn_stop_stopwatch.setFont(font7)
        self.btn_stop_stopwatch.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-radius: 40px ;\n"
"background-color: rgb(135, 120, 135);")
        self.btn_reset_stopwatch = QPushButton(self.tab_3)
        self.btn_reset_stopwatch.setObjectName(u"btn_reset_stopwatch")
        self.btn_reset_stopwatch.setGeometry(QRect(300, 210, 81, 81))
        self.btn_reset_stopwatch.setFont(font7)
        self.btn_reset_stopwatch.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-radius: 40px ;\n"
"background-color: rgb(0, 118, 102);")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.textbox_hour_timer = QLineEdit(self.tab_4)
        self.textbox_hour_timer.setObjectName(u"textbox_hour_timer")
        self.textbox_hour_timer.setGeometry(QRect(80, 60, 101, 91))
        font8 = QFont()
        font8.setFamily(u"Seven Segment")
        font8.setPointSize(50)
        self.textbox_hour_timer.setFont(font8)
        self.textbox_hour_timer.setStyleSheet(u"color: rgb(242, 98, 0);")
        self.textbox_hour_timer.setAlignment(Qt.AlignCenter)
        self.textbox_minute_timer = QLineEdit(self.tab_4)
        self.textbox_minute_timer.setObjectName(u"textbox_minute_timer")
        self.textbox_minute_timer.setGeometry(QRect(190, 60, 101, 91))
        self.textbox_minute_timer.setFont(font8)
        self.textbox_minute_timer.setStyleSheet(u"color: rgb(242, 98, 0);")
        self.textbox_minute_timer.setAlignment(Qt.AlignCenter)
        self.textbox_second_timer = QLineEdit(self.tab_4)
        self.textbox_second_timer.setObjectName(u"textbox_second_timer")
        self.textbox_second_timer.setGeometry(QRect(300, 60, 101, 91))
        self.textbox_second_timer.setFont(font8)
        self.textbox_second_timer.setStyleSheet(u"color: rgb(242, 98, 0);")
        self.textbox_second_timer.setAlignment(Qt.AlignCenter)
        self.btn_start_timer = QPushButton(self.tab_4)
        self.btn_start_timer.setObjectName(u"btn_start_timer")
        self.btn_start_timer.setGeometry(QRect(100, 210, 81, 81))
        font9 = QFont()
        font9.setPointSize(13)
        self.btn_start_timer.setFont(font9)
        self.btn_start_timer.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-radius: 40px ;\n"
"background-color: rgb(242, 0, 0);")
        self.btn_stop_timer = QPushButton(self.tab_4)
        self.btn_stop_timer.setObjectName(u"btn_stop_timer")
        self.btn_stop_timer.setGeometry(QRect(200, 210, 81, 81))
        font10 = QFont()
        font10.setPointSize(13)
        font10.setBold(False)
        self.btn_stop_timer.setFont(font10)
        self.btn_stop_timer.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-radius: 40px ;\n"
"background-color: rgb(242, 110, 0);")
        self.btn_reset_timer = QPushButton(self.tab_4)
        self.btn_reset_timer.setObjectName(u"btn_reset_timer")
        self.btn_reset_timer.setGeometry(QRect(300, 210, 81, 81))
        self.btn_reset_timer.setFont(font7)
        self.btn_reset_timer.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-radius: 40px ;\n"
"background-color: rgb(234, 179, 103);")
        self.pushButton = QPushButton(self.tab_4)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(80, 30, 101, 28))
        self.pushButton.setStyleSheet(u"border-radius: 2px;\n"
"color: rgb(255, 255, 255);")
        self.pushButton_2 = QPushButton(self.tab_4)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(190, 30, 101, 28))
        self.pushButton_2.setStyleSheet(u"border-radius: 2px;\n"
"color: rgb(255, 255, 255);")
        self.pushButton_3 = QPushButton(self.tab_4)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(300, 30, 101, 28))
        self.pushButton_3.setStyleSheet(u"border-radius: 2px;\n"
"color: rgb(255, 255, 255);")
        self.tabWidget.addTab(self.tab_4, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 580, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.ir.setText(QCoreApplication.translate("MainWindow", u"IRAN", None))
        self.gr.setText(QCoreApplication.translate("MainWindow", u"GERMANY(Berlin)", None))
        self.usa.setText(QCoreApplication.translate("MainWindow", u"USA(Arizona)", None))
        self.gr_time.setText("")
        self.us_time.setText("")
        self.ir_time.setText("")
        self.title.setText(QCoreApplication.translate("MainWindow", u"W🌍rld Cl🕜ck", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"World Clock", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Time :", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Alarm Title :", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Date :", None))
#if QT_CONFIG(tooltip)
        self.btn_new_alarm.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>press to add new task</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_new_alarm.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Alarm", None))
        self.label_stopwatch.setText(QCoreApplication.translate("MainWindow", u"0:0:0", None))
        self.btn_start_stopwatch.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.btn_stop_stopwatch.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.btn_reset_stopwatch.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"StopWatch", None))
        self.textbox_hour_timer.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.textbox_minute_timer.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.textbox_second_timer.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_start_timer.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.btn_stop_timer.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.btn_reset_timer.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Hour", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Minute", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Second", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Timer", None))
    # retranslateUi

