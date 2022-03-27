# -*- coding: utf-8 -*-
import datetime

import mysql.connector

from util import UnknownUser, WrongPassword


class PhoneDB:
    def __init__(self):
        self.user_id = 1
        try:
            self.conn = mysql.connector.connect(host="localhost", user="root", passwd='LinVor96',
                                                database='phonebooks', port=3306)
            self.cursor = self.conn.cursor()
        except mysql.connector.errors.ProgrammingError:
            self.conn = mysql.connector.connect(host="localhost", user="root", passwd='LinVor96',
                                                port=3306)

        if not self.conn.database:
            self.cursor = self.conn.cursor()
            self.create_DB()
            self.create_user_table()
            self.create_contacts_table()

    def login(self, login, password):
        self.cursor.execute('SELECT * FROM users WHERE login = (%s);', (login,))
        query = self.cursor.fetchall()
        if not query:
            raise UnknownUser
        else:
            if query[0][3] == password:
                return True
            else:
                raise WrongPassword

    def logout(self):
        pass

    def registration(self, login, birthday, password):
        self.cursor.execute("INSERT INTO users (login, birthday, password, last_entrance) VALUES (%s, %s, %s, %s)",
                            (login, birthday, password, datetime.datetime.now()))
        self.conn.commit()

    def add_contact(self, name, phone, birthday):
        self.cursor.execute("INSERT INTO contacts (user_id, name, phone, birthday) VALUES (%s, %s, %s, %s)",
                            (self.user_id, name, phone, birthday))
        self.conn.commit()

    def del_contact(self, phone):
        self.cursor.execute("DELETE FROM contacts WHERE phone = (%s)", (phone,))
        self.conn.commit()

    def birthday(self):
        pass

    def create_DB(self):
        self.cursor.execute("CREATE DATABASE phonebooks;")
        self.cursor.execute("USE phonebooks;")
        self.conn.commit()

    def create_user_table(self):
        query = "CREATE TABLE users(ID int PRIMARY KEY AUTO_INCREMENT, login VARCHAR(30) UNIQUE, " \
                "birthday DATE, password VARCHAR(256), last_entrance DATETIME);"
        self.cursor.execute(query)
        self.conn.commit()

    def create_contacts_table(self):
        query = "CREATE TABLE contacts(ID int PRIMARY KEY AUTO_INCREMENT, user_id int, name VARCHAR(256), " \
                "phone BIGINT UNSIGNED NOT NULL UNIQUE, birthday DATE, FOREIGN KEY (user_id) REFERENCES users (id));"
        self.cursor.execute(query)
        self.conn.commit()


if __name__ == "__main__":
    con = PhoneDB()
    date_birth = datetime.datetime(1996, 2, 28)
    date_birth2 = datetime.datetime(1996, 2, 15)
    date_birth3 = datetime.datetime(1968, 2, 8)
    date_birth.strftime('%Y-%m-%d')
    # con.registration('Dwigons', date_birth2, 'linamalina')
    # con.registration('Topi', date_birth, 'Goblinparol1')
    # con.add_contact("Лукс Лина Игоревна".decode('utf-8'), 89643348501, date_birth)
    # con.add_contact('Лукс Владислав Андреевич'.decode('utf-8'), 89520971492, date_birth2)
    # con.add_contact('Воробьева Марина Абраровна'.decode('utf-8'), 89062443068, date_birth3)
    con.login('Gary', '123')
    # con.login('Topi', 'Goblinparol1')
    # con.del_contact(89062443068)
