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
from world_clock import WorldTimeThread
from main_window import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self ):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self )


        def reset_stopwatch():
            self.thread_stopwatch.reset()
            self.ui.label_stopwatch.setText("0:0:0")
        def stop_stopwatch():
            self.thread_stopwatch.terminate()  
        def start_stopwatch():
            self.thread_stopwatch.start() 
        def show_time_stopwatch(time):  
            self.ui.label_stopwatch.setText(f"{time.hour}:{time.minute}:{time.second}")


        def start_timer():
            self.thread_timer.start()
        def show_time_timer(time):
            self.textbox_hour_timer.setText(str(time.hour))
            self.textbox_minute_timer.setText(str(time.minute))
            self.textbox_second_timer.setText(str(time.second))
            if time.hour == 0 and time.minute == 0 and time.second == 0 :
                self.thread_timer.terminate()
                alarm = QMessageBox()
                alarm.setText(" ⚠⛔⏰ TIME IS OVER ⏰⛔⚠")
                alarm.exec()

        def get_text(time):
            global text_hour , text_minute , text_second
            text_hour   = self.textbox_hour_timer.text()
            text_minute = self.textbox_minute_timer.text()                 
            text_second = self.textbox_second_timer.text()
            time.hour = int(text_hour)
            time.minute = int(text_minute)
            time.second = int(text_second)
            show_time_stopwatch(time)
            print(text_hour ,text_minute ,text_second   )
                

        
        self.thread_stopwatch = StopWatchThread()
        self.ui.label_stopwatch.setText("0:0:0")
        self.ui.btn_start_stopwatch.clicked.connect(start_stopwatch)
        self.ui.btn_stop_stopwatch.clicked.connect(stop_stopwatch)
        self.ui.btn_reset_stopwatch.clicked.connect(reset_stopwatch)
        self.thread_stopwatch.signal_send.connect(show_time_stopwatch)  # tooye thread , yek signale sakhtim , ke vaslesh mikonim be slote show_number


        self.thread_timer = TimerThread()
        self.ui.btn_start_timer.clicked.connect(start_timer)
        self.thread_timer.signal_send.connect(show_time_timer)

        self.ui.textbox_hour_timer.textChanged.connect(get_text)
        self.ui.textbox_minute_timer.textChanged.connect(get_text)
        self.ui.textbox_second_timer.textChanged.connect(get_text)
        self.thread_timer.signal_send.connect(get_text)



        self.ir_time_thread = WorldTimeThread()
        self.gr_time_thread = WorldTimeThread()
        self.us_time_thread = WorldTimeThread()

        def start_Wclock():
            self.ir_time_thread.start() 
            self.gr_time_thread.start()
            self.us_time_thread.start()

        def show_time_Wclock2( time2 ):  
            self.ui.gr_time.setText(f"{time2.hour}:{time2.minute}:{time2.second}")

        def show_time_Wclock1( time1 ):  
            self.ui.ir_time.setText(f"{time1.hour}:{time1.minute}:{time1.second}")

        def show_time_Wclock3( time3 ):  
            self.ui.us_time.setText(f"{time3.hour}:{time3.minute}:{time3.second}")
                   
        start_Wclock()
        self.ir_time_thread.signal_send_i.connect(show_time_Wclock1)
        self.gr_time_thread.signal_send_g.connect(show_time_Wclock2)
        self.us_time_thread.signal_send_u.connect(show_time_Wclock3)



if __name__ == "__main__" :
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
