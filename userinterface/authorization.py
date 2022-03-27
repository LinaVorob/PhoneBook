# -*- coding: utf-8 -*-
import os
import sys

from PyQt4.QtCore import Qt
from PyQt4.QtGui import QWidget, QApplication, QLabel, QFont, QVBoxLayout, QLineEdit, QHBoxLayout, QPushButton, \
    QCheckBox, QIcon, QFrame


class AuthWindow(QWidget):
    '''
    class for Authorization new user
    '''

    PATH = os.path.abspath(os.curdir)
    PATH_PIC = os.path.split(PATH)

    def __init__(self):
        QWidget.__init__(self)

        self.setWindowTitle('Авторизация'.decode('utf-8'))
        self.setFixedSize(400, 300)

        self.lock = QIcon()
        self.lock.addFile(os.path.join(self.PATH_PIC[0], 'pic', 'lock.svg'))
        self.setWindowIcon(self.lock)

        self.main_layout = QVBoxLayout(self)
        self.main_layout.setAlignment(Qt.AlignHCenter | Qt.AlignCenter)

        self.main_frame = QFrame(self)
        self.main_frame.setFrameShape(QFrame.Box)
        self.main_frame.setStyleSheet(
            'background-color: white; border-radius: 5px; border: 1px solid grey; height: 30;')
        self.main_frame.setFixedSize(300, 230)

        self.form_layout = QVBoxLayout()
        self.form_layout.setAlignment(Qt.AlignHCenter | Qt.AlignCenter)

        self.btn_layout = QHBoxLayout()
        self.remember_layout = QHBoxLayout()
        self.show_password_layout = QHBoxLayout()
        self.forget_layout = QHBoxLayout()

        self.name_font = QFont()
        self.name_font.setFamily('Century Gothic')
        self.name_font.setBold(True)
        self.name_font.setPixelSize(28)

        self.input_font = QFont()
        self.input_font.setPixelSize(14)
        self.input_font.setFamily('Century Gothic')

        self.label_name = QLabel(self)
        self.label_name.setText('Окно авторизации'.decode('utf-8'))
        self.label_name.setFont(self.name_font)

        self.login = QLineEdit(self)
        self.login.setPlaceholderText('Имя пользователя'.decode('utf-8'))
        self.login.setFont(self.input_font)
        self.login.setStyleSheet('border-radius: 0px;')

        self.password = QLineEdit(self)
        self.password.setPlaceholderText('Пароль'.decode('utf-8'))
        self.password.setFont(self.input_font)
        self.password.setStyleSheet('border-radius: 0px;')
        self.password.setEchoMode(QLineEdit.Password)

        self.enter = QPushButton(self)
        self.enter.setText('Войти'.decode('utf-8'))
        self.enter.setFont(self.input_font)
        self.enter.setStyleSheet('background: rgb(133, 255, 51);')

        self.registration = QPushButton(self)
        self.registration.setText('Регистрация'.decode('utf-8'))
        self.registration.setFont(self.input_font)
        self.registration.setStyleSheet('background: rgb(220, 220, 220)')

        self.cancel = QPushButton(self)
        self.cancel.setText('Отмена'.decode('utf-8'))
        self.cancel.setFont(self.input_font)
        self.cancel.setStyleSheet('background: rgb(255, 30, 30);')
        self.cancel.clicked.connect(sys.exit)

        self.remember = QCheckBox(self)
        self.remember.setText('Запомнить меня'.decode('utf-8'))
        self.remember.setFont(self.input_font)
        self.remember.setStyleSheet('border: 0px')

        self.show_password = QCheckBox(self)
        self.show_password.setText('Показать пароль'.decode('utf-8'))
        self.show_password.setFont(self.input_font)
        self.show_password.setStyleSheet('border: 0px')
        self.show_password.stateChanged.connect(self.func_show_password)

        self.forget = QLabel(self)
        self.forget.setText("<a href='#'> Забыли пароль? </a>".decode('utf-8'))
        self.forget.setStyleSheet('border: 0px')
        self.forget.setFont(self.input_font)

        self.btn_layout.addWidget(self.enter)
        self.btn_layout.addWidget(self.registration)
        self.btn_layout.addWidget(self.cancel)

        self.remember_layout.addStretch(1)
        self.remember_layout.addWidget(self.remember)
        self.remember_layout.addStretch(1)

        self.show_password_layout.addStretch(1)
        self.show_password_layout.addWidget(self.show_password)
        self.show_password_layout.addStretch(1)

        self.forget_layout.addStretch(1)
        self.forget_layout.addWidget(self.forget)
        self.forget_layout.addStretch(1)

        self.form_layout.addWidget(self.login)
        self.form_layout.addWidget(self.password)
        self.form_layout.addLayout(self.btn_layout)
        self.form_layout.addLayout(self.remember_layout)
        self.form_layout.addLayout(self.show_password_layout)
        self.form_layout.addLayout(self.forget_layout)

        self.main_frame.setLayout(self.form_layout)

        self.main_layout.addWidget(self.label_name)
        self.main_layout.addWidget(self.main_frame)
        self.main_layout.addStretch(1)

    def func_show_password(self):
        self.password.setEchoMode(QLineEdit.Normal if self.show_password.isChecked() else QLineEdit.Password)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    auth = AuthWindow()
    auth.show()
    sys.exit(app.exec_())
