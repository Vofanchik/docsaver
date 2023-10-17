# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SearchDocumentDialog.ui'
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

class Ui_Form_search_dialog(object):
    def setupUi(self, Form_search_dialog):
        Form_search_dialog.setObjectName(_fromUtf8("Form_search_dialog"))
        Form_search_dialog.resize(633, 299)
        self.gridLayout = QtGui.QGridLayout(Form_search_dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.dateEdit_release_to = QtGui.QDateEdit(Form_search_dialog)
        self.dateEdit_release_to.setCalendarPopup(True)
        self.dateEdit_release_to.setObjectName(_fromUtf8("dateEdit_release_to"))
        self.gridLayout.addWidget(self.dateEdit_release_to, 6, 2, 1, 1)
        self.lineEdit_name_document = QtGui.QLineEdit(Form_search_dialog)
        self.lineEdit_name_document.setObjectName(_fromUtf8("lineEdit_name_document"))
        self.gridLayout.addWidget(self.lineEdit_name_document, 0, 2, 1, 1)
        self.label_2 = QtGui.QLabel(Form_search_dialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.comboBox_structure = QtGui.QComboBox(Form_search_dialog)
        self.comboBox_structure.setMinimumSize(QtCore.QSize(400, 0))
        self.comboBox_structure.setObjectName(_fromUtf8("comboBox_structure"))
        self.gridLayout.addWidget(self.comboBox_structure, 2, 2, 1, 1)
        self.dateEdit_release_from = QtGui.QDateEdit(Form_search_dialog)
        self.dateEdit_release_from.setMaximumSize(QtCore.QSize(16777215, 22))
        self.dateEdit_release_from.setCalendarPopup(True)
        self.dateEdit_release_from.setObjectName(_fromUtf8("dateEdit_release_from"))
        self.gridLayout.addWidget(self.dateEdit_release_from, 5, 2, 1, 1)
        self.LineEdit_number_document = QtGui.QLineEdit(Form_search_dialog)
        self.LineEdit_number_document.setObjectName(_fromUtf8("LineEdit_number_document"))
        self.gridLayout.addWidget(self.LineEdit_number_document, 1, 2, 1, 1)
        self.comboBox_secret = QtGui.QComboBox(Form_search_dialog)
        self.comboBox_secret.setObjectName(_fromUtf8("comboBox_secret"))
        self.gridLayout.addWidget(self.comboBox_secret, 8, 2, 1, 1)
        self.label_3 = QtGui.QLabel(Form_search_dialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label = QtGui.QLabel(Form_search_dialog)
        self.label.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_4 = QtGui.QLabel(Form_search_dialog)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 1)
        self.label_5 = QtGui.QLabel(Form_search_dialog)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 8, 0, 1, 1)
        self.label_8 = QtGui.QLabel(Form_search_dialog)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 9, 0, 1, 1)
        self.checkBox_is_current = QtGui.QCheckBox(Form_search_dialog)
        self.checkBox_is_current.setText(_fromUtf8(""))
        self.checkBox_is_current.setObjectName(_fromUtf8("checkBox_is_current"))
        self.gridLayout.addWidget(self.checkBox_is_current, 9, 2, 1, 1)
        self.comboBox_category = QtGui.QComboBox(Form_search_dialog)
        self.comboBox_category.setObjectName(_fromUtf8("comboBox_category"))
        self.gridLayout.addWidget(self.comboBox_category, 7, 2, 1, 1)
        self.label_11 = QtGui.QLabel(Form_search_dialog)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout.addWidget(self.label_11, 7, 0, 1, 1)
        self.label_12 = QtGui.QLabel(Form_search_dialog)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout.addWidget(self.label_12, 6, 0, 1, 1)
        self.pushButton_finish_add_document = QtGui.QPushButton(Form_search_dialog)
        self.pushButton_finish_add_document.setObjectName(_fromUtf8("pushButton_finish_add_document"))
        self.gridLayout.addWidget(self.pushButton_finish_add_document, 11, 0, 1, 3)

        self.retranslateUi(Form_search_dialog)
        QtCore.QMetaObject.connectSlotsByName(Form_search_dialog)

    def retranslateUi(self, Form_search_dialog):
        Form_search_dialog.setWindowTitle(_translate("Form_search_dialog", "Поиск по категориям", None))
        self.label_2.setText(_translate("Form_search_dialog", "Номер", None))
        self.label_3.setText(_translate("Form_search_dialog", "Вид", None))
        self.label.setText(_translate("Form_search_dialog", "Наименование", None))
        self.label_4.setText(_translate("Form_search_dialog", "Издан c ", None))
        self.label_5.setText(_translate("Form_search_dialog", "Секретность", None))
        self.label_8.setText(_translate("Form_search_dialog", "Действующий", None))
        self.label_11.setText(_translate("Form_search_dialog", "Категория", None))
        self.label_12.setText(_translate("Form_search_dialog", "По", None))
        self.pushButton_finish_add_document.setText(_translate("Form_search_dialog", "Готово", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form_search_dialog = QtGui.QWidget()
    ui = Ui_Form_search_dialog()
    ui.setupUi(Form_search_dialog)
    Form_search_dialog.show()
    sys.exit(app.exec_())

