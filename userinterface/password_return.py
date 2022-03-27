# -*- coding: utf-8 -*-

import sys

from PyQt4.QtCore import Qt
from PyQt4.QtGui import QWidget, QApplication, QVBoxLayout, QFont, QLabel, QLineEdit, QHBoxLayout, QPushButton, QFrame


class PasswordReturn(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.setWindowTitle('Восстановление пароля'.decode('utf-8'))
        self.setFixedSize(350, 300)

        self.main_layout = QVBoxLayout(self)
        self.main_layout.setAlignment(Qt.AlignHCenter | Qt.AlignCenter)

        self.form_layout = QVBoxLayout()
        self.form_layout.setAlignment(Qt.AlignHCenter | Qt.AlignCenter)
        self.form_layout.setSpacing(25)

        self.btn_layout = QHBoxLayout()

        self.main_frame = QFrame(self)
        self.main_frame.setFrameShape(QFrame.Box)
        self.main_frame.setStyleSheet('background-color: white; border-radius: 5px; border: 1px solid grey')
        self.main_frame.setFixedSize(270, 200)

        self.name_font = QFont()
        self.name_font.setFamily('Century Gothic')
        self.name_font.setBold(True)
        self.name_font.setPixelSize(20)

        self.input_font = QFont()
        self.input_font.setPixelSize(14)
        self.input_font.setFamily('Century Gothic')

        self.label_name = QLabel(self)
        self.label_name.setText('Восстановление пароля'.decode('utf-8'))
        self.label_name.setFont(self.name_font)

        self.user_email = QLineEdit()
        self.user_email.setPlaceholderText('Адрес электронной почты'.decode('utf-8'))
        self.user_email.setFont(self.input_font)
        self.user_email.setStyleSheet('border-radius: 0px')
        self.user_email.setFixedHeight(30)

        self.send_new_password = QPushButton(self)
        self.send_new_password.setText('Сменить пароль'.decode('utf-8'))
        self.send_new_password.setFont(self.input_font)
        self.send_new_password.setStyleSheet('background: rgb(200, 200, 200);')
        self.send_new_password.setFixedHeight(30)

        self.cancel = QPushButton(self)
        self.cancel.setText('Отмена'.decode('utf-8'))
        self.cancel.setFont(self.input_font)
        self.cancel.setStyleSheet('background: rgb(255, 30, 30);')
        self.cancel.setFixedHeight(30)
        self.cancel.clicked.connect(sys.exit)

        self.btn_layout.addWidget(self.send_new_password)
        self.btn_layout.addWidget(self.cancel)

        self.form_layout.addWidget(self.user_email)
        self.form_layout.addLayout(self.btn_layout)

        self.main_frame.setLayout(self.form_layout)

        self.main_layout.addWidget(self.label_name)
        self.main_layout.addStretch(1)
        self.main_layout.addWidget(self.main_frame)
        self.main_layout.addStretch(1)
        self.clearFocus()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    auth = PasswordReturn()
    auth.show()
    sys.exit(app.exec_())
