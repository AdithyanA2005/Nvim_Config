import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5.QtCore import QDate
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QTime
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QMovie

from alpha.alpha import Alpha
from alpha.gui import Ui_alphaWindow
from alpha.tasks import Tasks

skill = Tasks()

class MainThread(QThread):

    def __init__(self):
        super(MainThread, self).__init__()
        
    def run(self): 
        skill.wish_me()
        Alpha()

startExecution = MainThread()

class Main(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_alphaWindow()
        self.ui.setupUi(self)
        self.ui.onButton.clicked.connect(self.start_alpha_app)
        self.show()

    def start_alpha_app(self):
        self.ui.movie = QtGui.QMovie("alpha/lib/GuiLib/rotator.gif")
        self.ui.mainRotatorLabel.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("alpha/lib/GuiLib/ironman.gif")
        self.ui.ironmanLabel.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("alpha/lib/GuiLib/rotator2.gif")
        self.ui.greenSpinnerLabel.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("alpha/lib/GuiLib/earth.gif")
        self.ui.earthLabel.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        current_day = QDate.currentDate()
        time_Label = current_time.toString('hh:mm:ss')
        date_Label = current_date.toString('dd-MMMM ')
        day_label = current_day.toString('ddd')
        self.ui.dayMonthLabel.setText(date_Label)
        self.ui.timeLabel.setText(time_Label)
        self.ui.dayLabel.setText(day_label)

    
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    alpha = Main()
    alpha.show()
    sys.exit(app.exec_())
