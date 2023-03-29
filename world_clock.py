import time 
from PySide6.QtWidgets import *
from PySide6.QtGui import * 
from PySide6.QtCore import *
from PySide6.QtUiTools import QUiLoader
from mytime import MyTime
from datetime import datetime 
import pytz

class WorldTimeThread(QThread):
    signal_send_i = Signal(MyTime)
    signal_send_g = Signal(MyTime)
    signal_send_u = Signal(MyTime)
    def __init__(self):
        super().__init__()

        self.ir_time = datetime.now().strftime('%H:%M:%S')
        self.ir_time.split(":")
        s1=self.ir_time[6:8]
        m1=self.ir_time[3:5]
        h1=self.ir_time[0:2]        
        #print("iran time :" + self.ir_time)


        usa = datetime.now(pytz.utc)
        us_time = usa.astimezone(pytz.timezone('US/Arizona'))
        fmt = '%H:%M:%S'
        self.us_time = us_time.strftime(fmt)
        self.us_time.split(":")
        s3=self.us_time[6:8]
        m3=self.us_time[3:5]
        h3=self.us_time[0:2]        
        #print("usa time : " + self.us_time)

        Gr = datetime.now(pytz.utc)
        gr_time = Gr.astimezone(pytz.timezone("Europe/Berlin"))
        fmt = '%H:%M:%S'
        self.gr_time = gr_time.strftime(fmt)
        self.gr_time.split(":")
        s=self.gr_time[6:8]
        m=self.gr_time[3:5]
        h=self.gr_time[0:2]
        #print("germany time : " + self.gr_time)

        self.time_iran = MyTime(int(h1) , int(m1) , int(s1))
        self.time_ger  = MyTime(int(h)  , int(m)  , int(s) )
        self.time_usa  = MyTime(int(h3) , int(m3) , int(s3))

    def run(self):
        while True :
            self.time_iran.plus()
            self.time_ger.plus()
            self.time_usa.plus()
            self.signal_send_i.emit(self.time_iran) #emit  ==> send second 
            self.signal_send_g.emit(self.time_ger)  
            self.signal_send_u.emit(self.time_usa)  
            time.sleep(1)
