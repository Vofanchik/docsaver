# coding=utf-8
import sys
from PyQt4.QtGui import QApplication
from PyQt4 import QtGui

from Classes.MainWindow import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = MainWindow()
    form.setWindowIcon(QtGui.QIcon(QtGui.QPixmap('Ui_files/thumbnail.png')))
    form.show()
    app.exec_()
