from PyQt5.QtCore import QTimer,QTime
from PyQt5 import QtCore, QtGui, QtWidgets,uic
from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel, QApplication, QLCDNumber,QWidget,QStackedWidget,QSizePolicy,QTextBrowser,QTextEdit,QPlainTextEdit
import sys
import datetime
from threading import Timer


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        uic.loadUi("stopwatch.ui", self)

        self.time_display = self.findChild(QLCDNumber, "lcdNumber")
        self.start_button = self.findChild(QPushButton, "start")
        self.pause_button = self.findChild(QPushButton, "pause")
        self.reset_button = self.findChild(QPushButton, "reset")
        self.lap_button = self.findChild(QPushButton, "lap")
        self.clear_button = self.findChild(QPushButton, "clearlaps")
        self.lap_display = self.findChild(QTextEdit, "textEdit")
        
        self.start_button.clicked.connect(self.startTimer)
        self.pause_button.clicked.connect(self.pauseTimer)
        self.reset_button.clicked.connect(self.resetTimer)
        self.lap_button.clicked.connect(self.writeLap)
        self.clear_button.clicked.connect(self.clear_all)
       
        
      
        
        

        # NEED TO MAKE/CONNECT TO FUNCTION THAT WILL OPEN LAPTIMES.TXT AND UPDATE QTEXTEDIT BOX UPON CLICKING VIEW LAPS

    

        

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
            self.f = open("laptimes.txt", "r")
            self.f = self.f.read()
            self.lap_display.setText(str(self.f))


    def clear_all(self):
        self.lap = 0
        self.f = open("laptimes.txt", "w")
        self.f.write("")
        self.f.close()
        self.f = open("laptimes.txt", "r")
        self.f = self.f.read()
        self.lap_display.clear()
        
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    w = UI()
   
    w.show()
    sys.exit(app.exec_())    
