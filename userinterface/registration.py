# -*- coding: utf-8 -*-
import os
import sys

from PyQt4.QtCore import Qt
from PyQt4.QtGui import QWidget, QApplication, QPushButton, QLineEdit, QLabel, QFont, QHBoxLayout, QVBoxLayout, \
    QIcon, QFrame

PATH = os.path.abspath(os.curdir)
PATH_PIC = os.path.split(PATH)


class Registration(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.setWindowTitle('Регистрация'.decode('utf-8'))
        self.setFixedSize(400, 300)
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setAlignment(Qt.AlignHCenter | Qt.AlignCenter)

        self.form_layout = QVBoxLayout()
        self.form_layout.setAlignment(Qt.AlignHCenter | Qt.AlignCenter)
        self.form_layout.setSpacing(15)

        self.main_frame = QFrame(self)
        self.main_frame.setFrameShape(QFrame.Box)
        self.main_frame.setStyleSheet(
            'background-color: white; border-radius: 5px; border: 1px solid grey; height: 30;')
        self.main_frame.setFixedSize(300, 230)

        self.date_layout = QHBoxLayout()
        self.date_layout.setSpacing(0)
        self.btn_layout = QHBoxLayout()

        self.name_font = QFont()
        self.name_font.setFamily('Century Gothic')
        self.name_font.setBold(True)
        self.name_font.setPixelSize(28)

        self.input_font = QFont()
        self.input_font.setPixelSize(14)
        self.input_font.setFamily('Century Gothic')

        self.label_name = QLabel(self)
        self.label_name.setText('Регистрация'.decode('utf-8'))
        self.label_name.setFont(self.name_font)

        self.login = QLineEdit(self)
        self.login.setPlaceholderText('Имя пользователя'.decode('utf-8'))
        self.login.setFont(self.input_font)
        self.login.setStyleSheet('border-radius: 0px;')

        self.password = QLineEdit(self)
        self.password.setPlaceholderText('Пароль'.decode('utf-8'))
        self.password.setFont(self.input_font)
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setStyleSheet('border-radius: 0px;')

        self.password_again = QLineEdit(self)
        self.password_again.setPlaceholderText('Повторите пароль'.decode('utf-8'))
        self.password_again.setFont(self.input_font)
        self.password_again.setEchoMode(QLineEdit.Password)
        self.password_again.setStyleSheet('border-radius: 0px;')

        self.date_input = QLineEdit(self)
        self.date_input.setFont(self.input_font)
        self.date_input.setPlaceholderText('Дата рождения'.decode('utf-8'))
        self.date_input.setStyleSheet('border-radius: 0px;')

        self.calendar_icon = QIcon()
        self.calendar_icon.addFile(os.path.join(PATH_PIC[0], 'pic', 'calendar'))
        self.calendar_btn = QPushButton(self)
        self.calendar_btn.setIcon(self.calendar_icon)
        self.calendar_btn.setFixedSize(40, 30)
        self.calendar_btn.setStyleSheet('border-radius: 0px;')

        self.btn_ok = QPushButton(self)
        self.btn_ok.setText('Войти'.decode('utf-8'))
        self.btn_ok.setFont(self.input_font)
        self.btn_ok.setStyleSheet('background: rgb(133, 255, 51);')

        self.cancel = QPushButton(self)
        self.cancel.setText('Отмена'.decode('utf-8'))
        self.cancel.setFont(self.input_font)
        self.cancel.setStyleSheet('background: rgb(255, 30, 30);')
        self.cancel.clicked.connect(sys.exit)

        self.date_layout.addWidget(self.date_input)
        self.date_layout.addWidget(self.calendar_btn)

        self.btn_layout.addWidget(self.btn_ok)
        self.btn_layout.addWidget(self.cancel)

        self.form_layout.addWidget(self.login)
        self.form_layout.addWidget(self.password)
        self.form_layout.addWidget(self.password_again)
        self.form_layout.addLayout(self.date_layout)
        self.form_layout.addLayout(self.btn_layout)

        self.main_frame.setLayout(self.form_layout)

        self.main_layout.addWidget(self.label_name)
        self.main_layout.addWidget(self.main_frame)
        self.main_layout.addStretch(1)

    def match_password(self):
        return True if self.password.text() == self.password_again.text() else False



if __name__ == '__main__':
    app = QApplication(sys.argv)
    auth = Registration()
    auth.show()
    sys.exit(app.exec_())
