import time 
from PySide6.QtGui import * 
from PySide6.QtCore import *
from mytime import MyTime
from plyer import notification
from world_clock import WorldTimeThread
from datetime import datetime 

class Alarm(QThread):
    def __init__(self):
        super().__init__()
        self.alarm_time = []
        self.alarm_date = []
        self.ir_time = datetime.now().strftime('%H:%M:%S')
        self.ir_time.split(":")
        s1=int(self.ir_time[6:8])
        m1=int(self.ir_time[3:5])
        h1=int(self.ir_time[0:2]  )        
        self.time = MyTime(h1,m1,s1)

    def run(self):
        while True:
            self.time.second += 1
            time.sleep(1)
            for t in self.alarm_time:
                if self.time == t:
                    notification.notify(title='Alarm',message= str(t))