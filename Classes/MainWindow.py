# encoding=utf8
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from PyQt4.QtGui import QMainWindow, QDialog, QGridLayout, QLineEdit, QDialogButtonBox, QFileDialog, \
    QTableWidgetItem, QCompleter, QWidget, QAction
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import QDate, QTimer, Qt, QDir
from Classes.DataBase import DataBase
from UI_files.MainWindow import Ui_MainWindow
from UI_files.AddDocumentDialog import Ui_Form
from UI_files.SearchDocumentDialog import Ui_Form_search_dialog


def get_keys_from_value(d, val):
    return [k for k, v in d.items() if v == val]

class AddSearchDialog(QDialog):
    def __init__(self, parent=None):
        super(AddSearchDialog, self).__init__(parent)
        self.setWindowIcon(QtGui.QIcon(QtGui.QPixmap('Ui_files/thumbnail.png')))
        self.ui = Ui_Form_search_dialog()
        self.ui.setupUi(self)
        self.ui.pushButton_finish_add_document.clicked.connect(lambda: self.accept())

class AddDocumentDialog(QDialog):
    def __init__(self, parent=None):
        super(AddDocumentDialog, self).__init__(parent)
        self.setWindowIcon(QtGui.QIcon(QtGui.QPixmap('Ui_files/thumbnail.png')))
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton_finish_add_document.clicked.connect(lambda: self.accept())


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.cell_addAction = None
        self.dict_categories = None
        self.chosen_document_id_in_search_table = None
        self.chosen_document_name_in_search_table = None
        self.dict_of_all_documents = {}
        self.path_to_file_list = []
        self.add_files_dialog = None
        self.dict_structures = {}
        self.add_document_dialog = None

        self.secret_dict = {1: u"Обычный", 2: u"дсп", 3: u"Секретно", 4: u"Совершенно серкетно", 5: u"Особой важности"}
        self.db = DataBase()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.button_add_document.clicked.connect(lambda: self.add_document())
        self.ui.button_search_by_categories.clicked.connect(lambda: self.run_search_dialog())
        self.reload_table_favorites()
        self.show_last_ten_documents()
        self.set_main_completer()

        self.ui.table_search.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.ui.table_favorites.setContextMenuPolicy(Qt.ActionsContextMenu)

        self.createActions()
        self.ui.table_search.addAction(self.save_searched_dicumentAction)
        self.ui.table_search.addAction(self.delete_document_and_linked_filesAction)
        self.ui.table_search.addAction(self.add_to_favoriteAction)
        self.ui.table_favorites.addAction(self.delete_from_favoritesAction)

    def createActions(self):
        self.save_searched_dicumentAction = QAction(u"Сохранить связанные файлы", self)
        self.save_searched_dicumentAction.triggered.connect(self.save_searched_document_from_table)
        self.delete_document_and_linked_filesAction = QAction(u'Удалить запись', self)
        self.delete_document_and_linked_filesAction.triggered.connect(self.delete_document_and_linked_files)
        self.add_to_favoriteAction = QAction(u"Добавить в избранное", self)
        self.add_to_favoriteAction.triggered.connect(self.add_to_favorite)
        self.delete_from_favoritesAction = QAction(u"Убрать из избранного", self)
        self.delete_from_favoritesAction.triggered.connect(self.delete_from_favorites)

    def add_to_favorite(self):
        current = self.ui.table_search.currentRow()
        if current != -1:
            id_document = str(self.ui.table_search.item(current, 0).text())
            self.db.add_to_favorites(id_document)
            self.reload_table_favorites()

    def delete_from_favorites(self):
        current = self.ui.table_favorites.currentRow()
        print current
        if current != -1:
            id_document = str(self.ui.table_favorites.item(current, 0).text())
            print id_document
            self.db.delete_from_favorites(id_document)
            self.reload_table_favorites()


    def save_searched_document_from_table(self):
        current = self.ui.table_search.currentRow()
        if current != -1:
            id_document = str(self.ui.table_search.item(current, 0).text())
            destination = str(QFileDialog.getExistingDirectory(self, 'Folder'))
            destination = destination.decode('utf-8').encode(sys.getfilesystemencoding())
            self.db.save_data(id_document, destination)

    def delete_document_and_linked_files(self):
        current = self.ui.table_search.currentRow()
        if current != -1:
            id_document = str(self.ui.table_search.item(current, 0).text())
            self.db.delete_document_and_linked_files(id_document)
            self.ui.table_search.setRowCount(0)
            self.reload_table_favorites()
            self.show_last_ten_documents()
            self.ui.statusbar.showMessage(u"Документ удален", 5000)

    def set_main_completer(self):
        self.dict_of_all_documents = {i[0]: QtCore.QString.fromUtf8(i[1]) for i in self.db.show_id_name_all_documents()}
        list_of_all_documents = [i for i in self.dict_of_all_documents.values()]
        completer = QCompleter(list_of_all_documents)
        completer.setCaseSensitivity(False)
        completer.activated.connect(self.on_activated_completer)
        self.ui.lineEdit_search.setCompleter(completer)

    def on_activated_completer(self):
        self.chosen_document_name_in_search_table = unicode(self.ui.lineEdit_search.text())
        QTimer.singleShot(0, self.ui.lineEdit_search.clear)
        self.chosen_document_id_in_search_table = get_keys_from_value(self.dict_of_all_documents,
                                                                      self.chosen_document_name_in_search_table)[0]
        self.update_search_table_by_completer()

    def update_search_table_by_completer(self):
        if self.chosen_document_id_in_search_table:
            tuple_of_document = self.db.show_document_by_id(self.chosen_document_id_in_search_table)
            self.ui.table_search.clear()
            headers = ["id", u"Вид",u"Наименование", u"Номер", u"Дата", u"Секретность", u"Избранное", u"Действующий"]
            self.ui.table_search.setColumnCount(len(headers))
            self.ui.table_search.setHorizontalHeaderLabels(headers)
            self.ui.table_search.setColumnHidden(0, True)
            self.ui.table_search.setRowCount(1)
            self.ui.table_search.setItem(0, 0, QTableWidgetItem(str(tuple_of_document[0])))
            self.ui.table_search.setItem(0, 1, QTableWidgetItem(QtCore.QString.fromUtf8(tuple_of_document[1])))
            self.ui.table_search.setItem(0, 2, QTableWidgetItem(QtCore.QString.fromUtf8(tuple_of_document[2])))
            self.ui.table_search.setItem(0, 3, QTableWidgetItem(QtCore.QString.fromUtf8(tuple_of_document[3])))
            self.ui.table_search.setItem(0, 4, QTableWidgetItem(QDate.fromString(tuple_of_document[4], "yyyy-MM-dd")
                                                                                            .toString("dd.MM.yyyy")))
            self.ui.table_search.setItem(0, 5, QTableWidgetItem(self.secret_dict[tuple_of_document[5]]))
            self.ui.table_search.setItem(0, 6, QTableWidgetItem('+' if tuple_of_document[6] else ''))
            self.ui.table_search.setItem(0, 7, QTableWidgetItem('+' if tuple_of_document[6] else ''))

        self.chosen_document_id_in_search_table = None

    def update_search_table(self, searched_list):
        self.ui.table_search.clear()
        headers = ["id", u"Вид",u"Наименование", u"Номер", u"Дата", u"Секретность", u"Избранное", u"Действующий"]
        self.ui.table_search.setColumnCount(len(headers))
        self.ui.table_search.setHorizontalHeaderLabels(headers)
        self.ui.table_search.setColumnHidden(0, True)
        self.ui.table_search.setRowCount(len(searched_list))
        for n, i in enumerate(searched_list):
            self.ui.table_search.setItem(n, 0, QTableWidgetItem(str(i[0])))
            self.ui.table_search.setItem(n, 1, QTableWidgetItem(QtCore.QString.fromUtf8(i[1])))
            self.ui.table_search.setItem(n, 2, QTableWidgetItem(QtCore.QString.fromUtf8(i[2])))
            self.ui.table_search.setItem(n, 3, QTableWidgetItem(QtCore.QString.fromUtf8(i[3])))
            self.ui.table_search.setItem(n, 4, QTableWidgetItem(QDate.fromString(i[4], "yyyy-MM-dd")
                                                                                            .toString("dd.MM.yyyy")))
            self.ui.table_search.setItem(n, 5, QTableWidgetItem(self.secret_dict[i[5]]))
            self.ui.table_search.setItem(n, 6, QTableWidgetItem('+' if i[6] else ''))
            self.ui.table_search.setItem(n, 7, QTableWidgetItem('+' if i[6] else ''))


    def reload_table_favorites(self):
        favorites_list = self.db.show_favorites()
        self.ui.table_favorites.clear()
        headers = ["id", u"Наименование", u"Номер", u"Дата"]
        self.ui.table_favorites.setColumnCount(len(headers))
        self.ui.table_favorites.setHorizontalHeaderLabels(headers)
        self.ui.table_favorites.setColumnHidden(0, True)
        self.ui.table_favorites.setRowCount(len(favorites_list))
        for row_number, it in enumerate(favorites_list):
            self.ui.table_favorites.setItem(row_number, 0, QTableWidgetItem(str(it[0])))
            self.ui.table_favorites.setItem(row_number, 1, QTableWidgetItem(QtCore.QString.fromUtf8(it[1])))
            self.ui.table_favorites.setItem(row_number, 2, QTableWidgetItem(QtCore.QString.fromUtf8(it[2])))
            self.ui.table_favorites.setItem(row_number, 3, QTableWidgetItem(QDate.fromString(it[3],"yyyy-MM-dd")
                                                                            .toString("dd.MM.yyyy")))

    def show_last_ten_documents(self):
        last_ten = self.db.show_last_ten_documents()
        self.ui.table_search.clear()
        headers = ["id", u"Вид",u"Наименование", u"Номер", u"Дата", u"Секретность", u"Избранное", u"Действующий"]
        self.ui.table_search.setColumnCount(len(headers))
        self.ui.table_search.setHorizontalHeaderLabels(headers)
        self.ui.table_search.setColumnHidden(0, True)
        self.ui.table_search.setRowCount(len(last_ten))
        for n, i in enumerate(last_ten):
            self.ui.table_search.setItem(n, 0, QTableWidgetItem(str(i[0])))
            self.ui.table_search.setItem(n, 1, QTableWidgetItem(QtCore.QString.fromUtf8(i[1])))
            self.ui.table_search.setItem(n, 2, QTableWidgetItem(QtCore.QString.fromUtf8(i[2])))
            self.ui.table_search.setItem(n, 3, QTableWidgetItem(QtCore.QString.fromUtf8(i[3])))
            self.ui.table_search.setItem(n, 4, QTableWidgetItem(QDate.fromString(i[4], "yyyy-MM-dd")
                                                                                            .toString("dd.MM.yyyy")))
            self.ui.table_search.setItem(n, 5, QTableWidgetItem(self.secret_dict[i[5]]))
            self.ui.table_search.setItem(n, 6, QTableWidgetItem('+' if i[6] else ''))
            self.ui.table_search.setItem(n, 7, QTableWidgetItem('+' if i[6] else ''))

    def add_structure(self):
        add_structure_dialog = QDialog()
        add_structure_dialog.setWindowTitle(QtCore.QString.fromUtf8('Добавить издателя'))
        add_structure_dialog_layout = QGridLayout(add_structure_dialog)
        name_edit = QLineEdit()
        add_structure_dialog_layout.addWidget(name_edit)
        btns = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        btns.accepted.connect(lambda: add_structure_dialog.accept())
        btns.rejected.connect(lambda: add_structure_dialog.reject())
        add_structure_dialog_layout.addWidget(btns)
        if add_structure_dialog.exec_():
            self.db.insert_structure(unicode(name_edit.text()))
        self.reload_combobox_structure()

    def reload_combobox_structure(self):
        self.add_document_dialog.ui.comboBox_structure.clear()
        self.dict_structures = {i[0]: QtCore.QString.fromUtf8(i[1]) for i in self.db.show_structures()}
        [self.add_document_dialog.ui.comboBox_structure.addItem(i) for i in self.dict_structures.values()]

    def add_category(self):
        add_category_dialog = QDialog()
        add_category_dialog.setWindowTitle(QtCore.QString.fromUtf8('Добавить категорию'))
        add_category_dialog_layout = QGridLayout(add_category_dialog)
        name_edit = QLineEdit()
        add_category_dialog_layout.addWidget(name_edit)
        btns = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        btns.accepted.connect(lambda: add_category_dialog.accept())
        btns.rejected.connect(lambda: add_category_dialog.reject())
        add_category_dialog_layout.addWidget(btns)
        if add_category_dialog.exec_():
            self.db.insert_category(unicode(name_edit.text()))
        self.reload_combobox_category()

    def reload_combobox_category(self):
        self.add_document_dialog.ui.comboBox_category.clear()
        self.dict_categories = {i[0]: QtCore.QString.fromUtf8(i[1]) for i in self.db.show_categories()}
        [self.add_document_dialog.ui.comboBox_category.addItem(i) for i in self.dict_categories.values()]

    def add_path_to_files(self, path_to_file_list):
        chosen = [str(QFileDialog.getOpenFileName(self, 'Open file'))][0]
        chosen = os.path.normpath(chosen)
        chosen = chosen.decode('utf-8').encode(sys.getfilesystemencoding())
        path_to_file_list.append(chosen)
        self.add_document_dialog.ui.label_7.setText(QtCore.QString.fromUtf8(' '.join(self.path_to_file_list)))
        self.add_document_dialog.activateWindow()

    def add_document(self):
        self.add_document_dialog = AddDocumentDialog()
        self.reload_combobox_category()
        self.reload_combobox_structure()
        list_of_values = ['name', 'number', 'release_date', 'structure_id', 'date_of_insert', 'secret', 'annotation',
                          'favorite', 'is_current', 'category_id']
        dict_of_values = dict.fromkeys(list_of_values, str())
        self.add_document_dialog.ui.pushButton_add_structure.clicked.connect(lambda: self.add_structure())
        self.add_document_dialog.ui.pushButton_add_category.clicked.connect(lambda: self.add_category())
        self.add_document_dialog.ui.pushButton_bind_files.clicked.connect(lambda: self.add_path_to_files(
                                                                                  self.path_to_file_list))
        [self.add_document_dialog.ui.comboBox_secret.addItem(i) for i in self.secret_dict.values()]
        if self.add_document_dialog.exec_():
            dict_of_values['name'] = unicode(self.add_document_dialog.ui.lineEdit_name_document.text())
            dict_of_values['number'] = unicode(self.add_document_dialog.ui.LineEdit_number_document.text())
            dict_of_values['release_date'] = \
                str(self.add_document_dialog.ui.dateEdit_release.date().toString('yyyy-MM-dd'))
            dict_of_values['structure_id'] = get_keys_from_value(self.dict_structures, unicode(
                self.add_document_dialog.ui.comboBox_structure.currentText()))[0]
            dict_of_values['secret'] = get_keys_from_value(self.secret_dict, unicode(
                self.add_document_dialog.ui.comboBox_secret.currentText()))[0]
            dict_of_values['annotation'] = unicode(self.add_document_dialog.ui.textEdit_annotation.toPlainText())
            dict_of_values['favorite'] = self.add_document_dialog.ui.checkBox_is_favorite.isChecked()
            dict_of_values['is_current'] = self.add_document_dialog.ui.checkBox_is_current.isChecked()
            dict_of_values['category_id'] = get_keys_from_value(self.dict_categories, unicode(
                self.add_document_dialog.ui.comboBox_category.currentText()))[0]

            added_id = self.db.insert_document(dict_of_values['name'], dict_of_values['number'],
                                               dict_of_values['release_date'], dict_of_values['structure_id'],
                                               dict_of_values['secret'], dict_of_values['annotation'],
                                               dict_of_values['category_id'], dict_of_values['favorite'],
                                               dict_of_values['is_current'])


            self.set_main_completer()
            self.reload_table_favorites()
            if added_id and len(self.path_to_file_list) > 0:
                for i in self.path_to_file_list:
                    self.db.insert_file(added_id, i)
                    self.path_to_file_list = []

    def run_search_dialog(self):
        run_search_dialog = AddSearchDialog()
        self.dict_categories = {i[0]: QtCore.QString.fromUtf8(i[1]) for i in self.db.show_categories()}
        run_search_dialog.ui.comboBox_category.addItem('')
        run_search_dialog.ui.comboBox_structure.addItem('')
        run_search_dialog.ui.comboBox_secret.addItem('')

        [run_search_dialog.ui.comboBox_category.addItem(i) for i in self.dict_categories.values()]
        self.dict_structures = {i[0]: QtCore.QString.fromUtf8(i[1]) for i in self.db.show_structures()}
        [run_search_dialog.ui.comboBox_structure.addItem(i) for i in self.dict_structures.values()]
        [run_search_dialog.ui.comboBox_secret.addItem(i) for i in self.secret_dict.values()]
        run_search_dialog.ui.checkBox_is_current.setChecked(True)
        run_search_dialog.ui.dateEdit_release_to.setDate(QDate.currentDate())
        run_search_dialog.ui.dateEdit_release_from.setDate(QDate(1980, 1, 1))
        list_of_values = ['name', 'number', 'release_date_from', 'release_date_to', 'structure_id',
                          'secret', 'is_current', 'category_id']
        dict_of_values = dict.fromkeys(list_of_values, str())

        if run_search_dialog.exec_():
            dict_of_values['name'] = unicode(run_search_dialog.ui.lineEdit_name_document.text())
            dict_of_values['number'] = unicode(run_search_dialog.ui.LineEdit_number_document.text())
            dict_of_values['release_date_from'] = \
                str(run_search_dialog.ui.dateEdit_release_from.date().toString('yyyy-MM-dd'))
            dict_of_values['release_date_to'] = \
                str(run_search_dialog.ui.dateEdit_release_to.date().toString('yyyy-MM-dd'))
            try:
                dict_of_values['structure_id'] = get_keys_from_value(self.dict_structures, unicode(
                    run_search_dialog.ui.comboBox_structure.currentText()))[0]
            except:
                dict_of_values['structure_id'] = ''
            try:
                dict_of_values['secret'] = get_keys_from_value(self.secret_dict, unicode(
                    run_search_dialog.ui.comboBox_secret.currentText()))[0]
            except:
                dict_of_values['secret'] = ''
            dict_of_values['is_current'] = run_search_dialog.ui.checkBox_is_current.isChecked()
            try:
                dict_of_values['category_id'] = get_keys_from_value(self.dict_categories, unicode(
                    run_search_dialog.ui.comboBox_category.currentText()))[0]
            except:
                dict_of_values['category_id'] = ''
            self.update_search_table(self.db.show_all_coincidence(dict_of_values))



