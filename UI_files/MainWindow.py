# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(869, 623)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.button_add_document = QtGui.QPushButton(self.centralwidget)
        self.button_add_document.setObjectName(_fromUtf8("button_add_document"))
        self.gridLayout.addWidget(self.button_add_document, 3, 0, 1, 1)
        self.lineEdit_search = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_search.setObjectName(_fromUtf8("lineEdit_search"))
        self.gridLayout.addWidget(self.lineEdit_search, 0, 0, 1, 2)
        self.button_search_by_categories = QtGui.QPushButton(self.centralwidget)
        self.button_search_by_categories.setObjectName(_fromUtf8("button_search_by_categories"))
        self.gridLayout.addWidget(self.button_search_by_categories, 3, 1, 1, 1)
        self.table_search = QtGui.QTableWidget(self.centralwidget)
        self.table_search.setObjectName(_fromUtf8("table_search"))
        self.table_search.setColumnCount(0)
        self.table_search.setRowCount(0)
        self.gridLayout.addWidget(self.table_search, 2, 0, 1, 1)
        self.table_favorites = QtGui.QTableWidget(self.centralwidget)
        self.table_favorites.setMaximumSize(QtCore.QSize(300, 16777215))
        self.table_favorites.setObjectName(_fromUtf8("table_favorites"))
        self.table_favorites.setColumnCount(0)
        self.table_favorites.setRowCount(0)
        self.gridLayout.addWidget(self.table_favorites, 2, 1, 1, 1)
        self.label_favorites = QtGui.QLabel(self.centralwidget)
        self.label_favorites.setObjectName(_fromUtf8("label_favorites"))
        self.gridLayout.addWidget(self.label_favorites, 1, 1, 1, 1)
        self.label_searched = QtGui.QLabel(self.centralwidget)
        self.label_searched.setObjectName(_fromUtf8("label_searched"))
        self.gridLayout.addWidget(self.label_searched, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 869, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "База документов", None))
        self.button_add_document.setText(_translate("MainWindow", "Добавить новый документ", None))
        self.button_search_by_categories.setText(_translate("MainWindow", "Поиск по категориям", None))
        self.label_favorites.setText(_translate("MainWindow", "Избранное", None))
        self.label_searched.setText(_translate("MainWindow", "Найденные", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

