import time 
from PySide6.QtWidgets import *
from PySide6.QtGui import * 
from PySide6.QtCore import *
from PySide6.QtUiTools import QUiLoader
from mytime import MyTime


class StopWatchThread(QThread):
    signal_send = Signal(MyTime) 
    def __init__(self ):
        super().__init__()
        
        self.time = MyTime( 0 , 0 , 0)

    def run(self):
        while True :
            self.time.plus()
            self.signal_send.emit(self.time) #emit  ==> send second 
            time.sleep(1)

    def reset(self):
        self.time.hour = 0
        self.time.minute = 0
        self.time.second = 0
