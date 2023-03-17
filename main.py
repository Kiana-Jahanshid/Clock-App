import sys
import time 
import threading 
from PySide6.QtWidgets import *
from PySide6.QtGui import * 
from PySide6.QtCore import *
from PySide6.QtUiTools import QUiLoader
from mytime import MyTime
from timer import TimerThread
from stopwatch import StopWatchThread



def reset_stopwatch():
    thread_stopwatch.reset()
    window.label_stopwatch.setText("0:0:0")

def stop_stopwatch():
    thread_stopwatch.terminate()  

def start_stopwatch():
    thread_stopwatch.start() 

def show_time_stopwatch(time):  
    window.label_stopwatch.setText(f"{time.hour}:{time.minute}:{time.second}")


def start_timer():
    thread_timer.start()

def show_time_timer(time):
    window.textbox_hour_timer.setText(str(time.hour))
    window.textbox_minute_timer.setText(str(time.minute))
    window.textbox_second_timer.setText(str(time.second))
    if time.hour == 0 and time.minute == 0 and time.second == 0 :
        thread_timer.terminate()
        alarm = QMessageBox()
        alarm.setText(" ⚠⛔⏰ TIME IS OVER ⏰⛔⚠")
        alarm.exec()

def get_text(time):
    global text_hour , text_minute , text_second
    text_hour   = window.textbox_hour_timer.text()
    text_minute = window.textbox_minute_timer.text()                 
    text_second = window.textbox_second_timer.text()
    time.hour = int(text_hour)
    time.minute = int(text_minute)
    time.second = int(text_second)
    show_time_stopwatch(time)
    print(text_hour ,text_minute ,text_second   )
    


if __name__ == "__main__" :
    app = QApplication(sys.argv)
    loader = QUiLoader()
    window = loader.load("mainwindow.ui")
    window.show()
    

    thread_stopwatch = StopWatchThread()
    window.label_stopwatch.setText("0:0:0")
    window.btn_start_stopwatch.clicked.connect(start_stopwatch)
    window.btn_stop_stopwatch.clicked.connect(stop_stopwatch)
    window.btn_reset_stopwatch.clicked.connect(reset_stopwatch)
    thread_stopwatch.signal_send.connect(show_time_stopwatch)  # tooye thread , yek signale sakhtim , ke vaslesh mikonim be slote show_number


    thread_timer = TimerThread()
    window.btn_start_timer.clicked.connect(start_timer)
    thread_timer.signal_send.connect(show_time_timer)

    window.textbox_hour_timer.textChanged.connect(get_text)
    window.textbox_minute_timer.textChanged.connect(get_text)
    window.textbox_second_timer.textChanged.connect(get_text)
    thread_timer.signal_send.connect(get_text)

    app.exec()