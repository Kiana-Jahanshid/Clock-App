import time 
from PySide6.QtWidgets import *
from PySide6.QtGui import * 
from PySide6.QtCore import *
from mytime import MyTime

class TimerThread(QThread):
    signal_send = Signal(MyTime)
    def __init__(self ):
        super().__init__()        
        self.time = MyTime(0 ,1 , 15)    

    def run(self):
        while True :
            self.time.minus()
            self.signal_send.emit(self.time)  
            time.sleep(1)

    def reset(self):
        self.time.hour = 0
        self.time.minute = 1
        self.time.second = 1

    def get(self , h , m , s):
        self.time.second = s
        self.time.minute = m 
        self.time.hour = h
