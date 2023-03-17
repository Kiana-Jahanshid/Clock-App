import sys
import time 
import threading 
from PySide6.QtWidgets import *
from PySide6.QtGui import * 
from PySide6.QtCore import *
from PySide6.QtUiTools import QUiLoader
from functools import partial
from mytime import MyTime
from ui_mainwindow import Ui_MainWindow

class TimerThread(QThread):
    signal_send = Signal(MyTime)
    def __init__(self):
        super().__init__()        
        #self.time = MyTime("" , "" , "")    

    def run(self):
        while True :
            self.time.minus()
            self.signal_send.emit(self.time)  
            time.sleep(1)

