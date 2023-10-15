# coding=utf-8
import sys
from PyQt4.QtGui import QApplication
from Classes.MainWindow import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()
    app.exec_()
