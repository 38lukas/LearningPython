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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(640, 473)
        MainWindow.setMinimumSize(QSize(640, 473))
        self.main_layout = QWidget(MainWindow)
        self.main_layout.setObjectName(u"main_layout")
        self.verticalLayout = QVBoxLayout(self.main_layout)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.main_layout)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.task_entry = QLineEdit(self.main_layout)
        self.task_entry.setObjectName(u"task_entry")

        self.verticalLayout.addWidget(self.task_entry)

        self.add_task_button = QPushButton(self.main_layout)
        self.add_task_button.setObjectName(u"add_task_button")

        self.verticalLayout.addWidget(self.add_task_button)

        self.task_list = QListWidget(self.main_layout)
        self.task_list.setObjectName(u"task_list")

        self.verticalLayout.addWidget(self.task_list)

        self.delete_task_button = QPushButton(self.main_layout)
        self.delete_task_button.setObjectName(u"delete_task_button")

        self.verticalLayout.addWidget(self.delete_task_button)

        self.exit_button = QPushButton(self.main_layout)
        self.exit_button.setObjectName(u"exit_button")

        self.verticalLayout.addWidget(self.exit_button)

        MainWindow.setCentralWidget(self.main_layout)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"LifeLog", None))
        self.add_task_button.setText(QCoreApplication.translate("MainWindow", u"Add Task", None))
        self.delete_task_button.setText(QCoreApplication.translate("MainWindow", u"Delete Task", None))
        self.exit_button.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
    # retranslateUi

