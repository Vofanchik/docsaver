# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddDocumentDialog.ui'
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(789, 515)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lineEdit_name_document = QtGui.QLineEdit(Form)
        self.lineEdit_name_document.setObjectName(_fromUtf8("lineEdit_name_document"))
        self.gridLayout.addWidget(self.lineEdit_name_document, 0, 2, 1, 2)
        self.comboBox_structure = QtGui.QComboBox(Form)
        self.comboBox_structure.setMinimumSize(QtCore.QSize(400, 0))
        self.comboBox_structure.setObjectName(_fromUtf8("comboBox_structure"))
        self.gridLayout.addWidget(self.comboBox_structure, 2, 2, 1, 1)
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.dateEdit_release = QtGui.QDateEdit(Form)
        self.dateEdit_release.setMaximumSize(QtCore.QSize(200, 16777215))
        self.dateEdit_release.setCalendarPopup(True)
        self.dateEdit_release.setObjectName(_fromUtf8("dateEdit_release"))
        self.gridLayout.addWidget(self.dateEdit_release, 3, 2, 1, 1)
        self.LineEdit_number_document = QtGui.QLineEdit(Form)
        self.LineEdit_number_document.setObjectName(_fromUtf8("LineEdit_number_document"))
        self.gridLayout.addWidget(self.LineEdit_number_document, 1, 2, 1, 1)
        self.comboBox_secret = QtGui.QComboBox(Form)
        self.comboBox_secret.setObjectName(_fromUtf8("comboBox_secret"))
        self.gridLayout.addWidget(self.comboBox_secret, 5, 2, 1, 1)
        self.label = QtGui.QLabel(Form)
        self.label.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.pushButton_add_structure = QtGui.QPushButton(Form)
        self.pushButton_add_structure.setMaximumSize(QtCore.QSize(150, 16777215))
        self.pushButton_add_structure.setObjectName(_fromUtf8("pushButton_add_structure"))
        self.gridLayout.addWidget(self.pushButton_add_structure, 2, 3, 1, 1)
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)
        self.label_8 = QtGui.QLabel(Form)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 6, 0, 1, 1)
        self.checkBox_is_current = QtGui.QCheckBox(Form)
        self.checkBox_is_current.setText(_fromUtf8(""))
        self.checkBox_is_current.setObjectName(_fromUtf8("checkBox_is_current"))
        self.gridLayout.addWidget(self.checkBox_is_current, 6, 2, 1, 1)
        self.label_9 = QtGui.QLabel(Form)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout.addWidget(self.label_9, 7, 0, 1, 1)
        self.label_6 = QtGui.QLabel(Form)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 8, 0, 1, 1)
        self.checkBox_is_favorite = QtGui.QCheckBox(Form)
        self.checkBox_is_favorite.setText(_fromUtf8(""))
        self.checkBox_is_favorite.setObjectName(_fromUtf8("checkBox_is_favorite"))
        self.gridLayout.addWidget(self.checkBox_is_favorite, 7, 2, 1, 1)
        self.label_7 = QtGui.QLabel(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setMaximumSize(QtCore.QSize(700, 16777215))
        self.label_7.setText(_fromUtf8(""))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 8, 2, 1, 1)
        self.pushButton_bind_files = QtGui.QPushButton(Form)
        self.pushButton_bind_files.setObjectName(_fromUtf8("pushButton_bind_files"))
        self.gridLayout.addWidget(self.pushButton_bind_files, 8, 3, 1, 1)
        self.label_10 = QtGui.QLabel(Form)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout.addWidget(self.label_10, 9, 0, 1, 1)
        self.textEdit_annotation = QtGui.QTextEdit(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_annotation.sizePolicy().hasHeightForWidth())
        self.textEdit_annotation.setSizePolicy(sizePolicy)
        self.textEdit_annotation.setObjectName(_fromUtf8("textEdit_annotation"))
        self.gridLayout.addWidget(self.textEdit_annotation, 9, 2, 1, 2)
        self.pushButton_finish_add_document = QtGui.QPushButton(Form)
        self.pushButton_finish_add_document.setObjectName(_fromUtf8("pushButton_finish_add_document"))
        self.gridLayout.addWidget(self.pushButton_finish_add_document, 11, 2, 1, 2)
        self.label_11 = QtGui.QLabel(Form)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout.addWidget(self.label_11, 4, 0, 1, 1)
        self.comboBox_category = QtGui.QComboBox(Form)
        self.comboBox_category.setObjectName(_fromUtf8("comboBox_category"))
        self.gridLayout.addWidget(self.comboBox_category, 4, 2, 1, 1)
        self.pushButton_add_category = QtGui.QPushButton(Form)
        self.pushButton_add_category.setObjectName(_fromUtf8("pushButton_add_category"))
        self.gridLayout.addWidget(self.pushButton_add_category, 4, 3, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Добавление документа", None))
        self.label_2.setText(_translate("Form", "Номер", None))
        self.label.setText(_translate("Form", "Наименование", None))
        self.label_3.setText(_translate("Form", "Вид", None))
        self.pushButton_add_structure.setText(_translate("Form", "Добавить вид", None))
        self.label_4.setText(_translate("Form", "Издан", None))
        self.label_5.setText(_translate("Form", "Секретность", None))
        self.label_8.setText(_translate("Form", "Действующий", None))
        self.label_9.setText(_translate("Form", "Добавить в избранное", None))
        self.label_6.setText(_translate("Form", "Связанные файлы", None))
        self.pushButton_bind_files.setText(_translate("Form", "Добавить файлы", None))
        self.label_10.setText(_translate("Form", "Аннотация документа", None))
        self.pushButton_finish_add_document.setText(_translate("Form", "Готово", None))
        self.label_11.setText(_translate("Form", "Категория", None))
        self.pushButton_add_category.setText(_translate("Form", "Добавить категорию", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

