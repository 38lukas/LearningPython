# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(90, 40, 631, 441))
        self.main_layout = QVBoxLayout(self.verticalLayoutWidget)
        self.main_layout.setObjectName(u"main_layout")
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.task_entry = QLineEdit(self.verticalLayoutWidget)
        self.task_entry.setObjectName(u"task_entry")

        self.main_layout.addWidget(self.task_entry)

        self.add_task_button = QPushButton(self.verticalLayoutWidget)
        self.add_task_button.setObjectName(u"add_task_button")

        self.main_layout.addWidget(self.add_task_button)

        self.task_list = QListWidget(self.verticalLayoutWidget)
        self.task_list.setObjectName(u"task_list")

        self.main_layout.addWidget(self.task_list)

        self.delete_task_button = QPushButton(self.verticalLayoutWidget)
        self.delete_task_button.setObjectName(u"delete_task_button")

        self.main_layout.addWidget(self.delete_task_button)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 25))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.add_task_button.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.delete_task_button.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
    # retranslateUi

