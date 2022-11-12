from PyQt5.QtCore import QTimer,QTime
from PyQt5 import QtCore, QtGui, QtWidgets,uic
from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel, QApplication, QLCDNumber,QWidget,QStackedWidget,QSizePolicy,QTextBrowser,QTextEdit,QPlainTextEdit
import sys
import datetime


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        uic.loadUi("stopwatch.ui", self)

        self.time_display = self.findChild(QLCDNumber, "lcdNumber")
        self.start_button = self.findChild(QPushButton, "start")
        self.pause_button = self.findChild(QPushButton, "pause")
        self.reset_button = self.findChild(QPushButton, "reset")
        self.lap_button = self.findChild(QPushButton, "lap")
        self.view_lap_button = self.findChild(QPushButton, "viewlap")
        
        self.start_button.clicked.connect(self.startTimer)
        self.pause_button.clicked.connect(self.pauseTimer)
        self.reset_button.clicked.connect(self.resetTimer)
        self.lap_button.clicked.connect(self.writeLap)
        self.view_lap_button.clicked.connect(self.lap_window)
        self.view_lap_button.clicked.connect(UI_Laptimes.print_worked)

    

        self.setFixedHeight(340)
        self.setFixedWidth(518)

        self.lap = 0
        self.clear_laps = False
        
        self.isreset = True
        self.timecount = 0
        self.timer = QtCore.QTimer(self)
        self.timecount = 0
        self.timer.timeout.connect(self.run_time)
        self.timer.start(1000)
        self.timer.setInterval(1)
       
        self.showLCD()

    def lap_window(self):
        
        
        
        widget.setCurrentIndex(widget.currentIndex()+1)
        

        

    def showLCD(self):
        current_time = str(datetime.timedelta(milliseconds=self.timecount))[:-3] #[:-3] means all elements of sezuence but the last three
        self.time_display.setDigitCount(11)
        if not self.isreset:
            self.time_display.display(current_time)
        else:
            self.time_display.display("0:00:00:000")


    def run_time(self):
        self.timecount += 1 #adds one second
        self.showLCD()     #updates display

    
        
    def startTimer(self):
        self.timer.start()
        self.isreset = False
        self.reset_button.setDisabled(True)
        self.start_button.setDisabled(True)
        self.pause_button.setDisabled(False)

    def pauseTimer(self):
        self.timer.stop()
        self.reset_button.setDisabled(False)
        self.start_button.setDisabled(False)
        self.pause_button.setDisabled(True)



    def resetTimer(self):
        self.timer.stop()
        self.timecount = 0
        self.isreset = True
        self.showLCD()
        
        self.reset_button.setDisabled(True)
        self.start_button.setDisabled(False)
        self.pause_button.setDisabled(True)
       

    def writeLap(self):
            
            self.lap += 1
            self.f = open("laptimes.txt", "a")
            self.f.write("Lap # " + str(self.lap) + " : " + str(self.timecount / 1000) + "\n")
            self.f.close()

class UI_Laptimes(QMainWindow):
    def __init__(self):
        super(UI_Laptimes, self).__init__()

        uic.loadUi("laptimes.ui", self)

        self.lap_display = self.findChild(QTextEdit, "textEdit")
        self.clear_laps = self.findChild(QPushButton, "clearlaps")
        self.back_button = self.findChild(QPushButton, "back")
        self.clear_laps.clicked.connect(self.clear_all)
        self.back_button.clicked.connect(self.back_watch)
        self.text = open("laptimes.txt").read()
        self.lap_display.setText(self.text)
        
        
        
        
        

        self.height = 427
        self.width = 391
        self.setFixedHeight(self.height)
        self.setFixedWidth(self.width)


    
    def print_worked(self):
        print("it worked")
        
        
       
        
        
        
         
         
        
        
        
    def clear_all(self):
        self.clear_laps = open("laptimes.txt", "w")
        self.clear_laps.write("")
        self.lap_display.setText(self.text)
        self.clear_laps.close()

        self.lap_display.clear()
        

    def back_watch(self):
        
        widget.setCurrentIndex(widget.currentIndex()-1)
        
        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    w = UI()
    l = UI_Laptimes()
    widget.addWidget(UI())
    widget.addWidget(UI_Laptimes())
  
    
    widget.show()
    
    sys.exit(app.exec_())    




        

#
