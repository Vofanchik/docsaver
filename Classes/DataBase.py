# coding=utf-8
import datetime
import os
import sqlite3


class DataBase:
    def __init__(self):
        self.conn = sqlite3.connect('NPB.db')
        self.conn.text_factory = str
        self.cur = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cur.execute(
            '''CREATE TABLE IF NOT EXISTS structures(
           id integer primary key,
           name text
           )''')

        self.cur.execute(
            '''CREATE TABLE IF NOT EXISTS categories(
           id integer primary key,
           name text
           )''')

        self.cur.execute(
            '''CREATE TABLE IF NOT EXISTS files(
            id integer primary key,
            id_documents integer,
            name text,
            format_file text,
            file_blob blob,
            FOREIGN KEY (id_documents) REFERENCES documents(id),
            Unique(name, id_documents)
           )''')

        self.cur.execute(
            '''CREATE TABLE IF NOT EXISTS documents(
           id integer primary key,
           name text,
           number text,
           release_date text,
           structure_id integer,
           date_of_insert text,
           secret INTEGER,
           annotation text,
           favorite bool,
           is_current bool,
           category_id integer,
           FOREIGN KEY (structure_id) REFERENCES structures(id),
           FOREIGN KEY (category_id) REFERENCES categories(id),
           UNIQUE(release_date,name)
           )''')
        self.conn.commit()

    def insert_document(self, name, number, release_date, structure_id,
                        secret, annotation, category_id, favorite=False, is_current=True,
                        date_of_insert = datetime.datetime.now().strftime('%Y-%m-%d')):
        try:
            self.cur.execute("INSERT INTO documents(name, number, release_date, structure_id, date_of_insert,"
                             " secret, annotation, favorite, is_current, category_id) VALUES(?,?,?,?,?,?,?,?,?,?)",
                             (name, number, release_date, structure_id, date_of_insert, secret,
                              annotation, favorite, is_current, category_id))
            self.conn.commit()
            return self.cur.lastrowid

        except sqlite3.Error as error:
            print(error)
            return None

    def insert_file(self, id_documents, full_file_name, format_file=''):
        try:
            file_name = os.path.split(full_file_name)[1]
            list_name = file_name.split('.')
            if len(list_name) > 1:
                format_file = list_name.pop()
                name = ''.join(list_name)
            else:
                name = file_name

            self.cur.execute("INSERT INTO files(id_documents, name, format_file, file_blob)"
                             "VALUES(?,?,?,?)", (id_documents, name, format_file,
                                                 self.convert_to_binary_data(full_file_name),))
            self.conn.commit()

        except sqlite3.Error as error:
            print(error)
            return error

    def insert_structure(self, name):
        try:
            self.cur.execute("INSERT INTO structures(name) VALUES(?)", (name,))
            self.conn.commit()
        except sqlite3.Error as error:
            print(error)
            return error

    def insert_category(self, name):
        try:
            self.cur.execute("INSERT INTO categories(name) VALUES(?)", (name,))
            self.conn.commit()
        except sqlite3.Error as error:
            print(error)
            return error

    def show_structures(self):
        return self.cur.execute('''SELECT * FROM structures''').fetchall()

    def show_categories(self):
        return self.cur.execute('''SELECT * FROM categories''').fetchall()

    def show_id_name_all_documents(self):
        return self.cur.execute('''SELECT id, name FROM documents''').fetchall()

    def show_favorites(self):
        return self.cur.execute('''SELECT * FROM documents where favorite = 1''').fetchall()

    def show_document_by_id(self, id_document):
        return self.cur.execute('''SELECT documents.id, structures.name, documents.name, documents.number, 
        documents.release_date, documents.secret, documents.favorite, documents.is_current
         FROM documents lEFT JOIN structures ON documents.structure_id = structures.id
         where documents.id = ?''', (id_document,)).fetchone()

    @staticmethod
    def convert_to_binary_data(filename):
        # Преобразование данных в двоичный формат
        with open(filename, 'rb') as f:
            blob_data = f.read()
        return blob_data

    @staticmethod
    def write_to_file(data, filename):
        # Преобразование двоичных данных в нужный формат
        with open(filename, 'wb') as f:
            f.write(data)

    def save_data(self, id_documents, destination):
        self.cur.execute("SELECT * from files where id_documents = ?", (id_documents,))
        records = self.cur.fetchall()
        for r in records:
            f_name = r[2]
            if r[3] != '':
                f_format = '.' + r[3]
            else:
                f_format = ''
            f_blob = r[4]
            save_path = os.path.join(destination, f_name + f_format)
            self.write_to_file(f_blob, save_path)



if __name__ == "__main__":
    a = DataBase()
    # a.insert_document("Об охране здоровья граждан", "2016-07-23", 1, datetime.datetime.now().strftime('%Y-%m-%d')
    #                   3, "Зло", False, True)
    # a.insert_file(1, '../323fz.pdf')
    # a.save_data(1, './')
    # a.insert_structure('gg')
    print a.show_document_by_id(2)