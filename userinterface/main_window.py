# -*- coding: utf-8 -*-
import os
import sys

from PyQt4.QtCore import Qt
from PyQt4.QtGui import QMainWindow, QApplication, QTabWidget, QWidget, QIcon, QTabBar, QStylePainter, \
    QStyleOptionTab, QStyle, QAction, QTableWidget, QTableWidgetItem, QLabel, QPixmap, QVBoxLayout, QGridLayout, QColor


class TabBar(QTabBar):
    PATH = os.path.abspath(os.curdir)
    PATH_PIC = os.path.split(PATH)

    def paintEvent(self, event):
        painter = QStylePainter(self)
        option = QStyleOptionTab()
        for index in range(self.count()):
            self.initStyleOption(option, index)
            painter.drawControl(QStyle.CE_TabBarTabShape, option)
            painter.drawText(self.tabRect(index),
                             Qt.AlignCenter | Qt.TextDontClip,
                             self.tabText(index))

    def tabSizeHint(self, index):
        size = QTabBar.tabSizeHint(self, index)
        size.setHeight = 50
        size.setWidth = 200
        if size.width() < size.height():
            size.transpose()
        return size


class TabWidget(QTabWidget):
    def __init__(self, parent=None):
        QTabWidget.__init__(self, parent)
        self.setTabBar(TabBar())


class MainWindow(QMainWindow):
    PATH = os.path.abspath(os.curdir)
    PATH_PIC = os.path.split(PATH)

    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle('Телефонная книга'.decode('utf-8'))
        self.setFixedSize(500, 710)

        bar = self.menuBar()
        self.menu = bar.addMenu('Меню'.decode('utf-8'))

        self.add_contact = QAction('Добавить контакт'.decode('utf-8'), self)
        self.add_contact.setShortcut('Ctrl+D')

        self.delete = QAction('Удалить контакт'.decode('utf-8'), self)
        self.logout = QAction('Выйти из аккаунта'.decode('utf-8'), self)

        self.menu.addAction(self.add_contact)
        self.menu.addAction(self.delete)
        self.menu.addAction(self.logout)

        self.icon = QIcon()
        self.icon.addFile(os.path.join(self.PATH_PIC[0], 'pic', 'phone.svg'))

        self.setWindowIcon(self.icon)

        self.tab_abc = TabWidget()
        self.tab_abc.setTabPosition(QTabWidget.West)
        self.tab_abc.insertTab(0, QWidget(), '')

        num_letter = 1040
        for item in range(1, 4):
            self.tab = QWidget()

            self.tab_layout = QVBoxLayout(self.tab)
            self.user_login_layout = QGridLayout()
            self.user_login_layout.setColumnStretch(0, 10)

            self.user_avatar = QLabel()
            self.avatar = QPixmap(os.path.join(self.PATH_PIC[0], 'pic', 'user.svg'))
            self.user_avatar.setPixmap(self.avatar)
            self.user_login = QLabel()
            self.user_login.setText('Вы вошли как ___'.decode('utf-8'))

            self.user_login_layout.addWidget(self.user_avatar, 0, 10)
            self.user_login_layout.addWidget(self.user_login, 0, 11)

            self.table = QTableWidget()
            self.table.setRowCount(20)
            self.table.setColumnCount(3)
            self.table.setHorizontalHeaderLabels(
                ('Имя'.decode('utf-8'), "Телефон".decode('utf-8'), "Дата рождения".decode('utf-8')))
            self.table.verticalHeader().hide()

            self.tab_layout.addLayout(self.user_login_layout)
            self.tab_layout.addWidget(self.table)
            self.tab_abc.insertTab(item, self.tab, unichr(num_letter) + unichr(num_letter + 1))
            num_letter += 2

        self.tab_abc.setCurrentIndex(1)

        self.setCentralWidget(self.tab_abc)

        self.table_item = QTableWidgetItem()
        self.table_item2 = QTableWidgetItem()
        self.table_item.setText('testing')
        self.table_item2.setText('testing2')
        self.table.setItem(0, 0, self.table_item)
        self.table.setItem(10, 2, self.table_item2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    auth = MainWindow()
    auth.show()
    sys.exit(app.exec_())
