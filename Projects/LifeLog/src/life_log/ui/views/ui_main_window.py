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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QListWidget, QListWidgetItem, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

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
        self.window_title = QLabel(self.main_layout)
        self.window_title.setObjectName(u"window_title")
        font = QFont()
        font.setBold(True)
        self.window_title.setFont(font)
        self.window_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.window_title)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.main_layout)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.sorting_menu = QComboBox(self.main_layout)
        self.sorting_menu.addItem("")
        self.sorting_menu.addItem("")
        self.sorting_menu.addItem("")
        self.sorting_menu.setObjectName(u"sorting_menu")
        self.sorting_menu.setEditable(False)

        self.horizontalLayout.addWidget(self.sorting_menu)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.task_list = QListWidget(self.main_layout)
        self.task_list.setObjectName(u"task_list")

        self.verticalLayout.addWidget(self.task_list)

        self.button_layout = QHBoxLayout()
        self.button_layout.setObjectName(u"button_layout")
        self.add_task_button = QPushButton(self.main_layout)
        self.add_task_button.setObjectName(u"add_task_button")

        self.button_layout.addWidget(self.add_task_button)

        self.delete_task_button = QPushButton(self.main_layout)
        self.delete_task_button.setObjectName(u"delete_task_button")

        self.button_layout.addWidget(self.delete_task_button)


        self.verticalLayout.addLayout(self.button_layout)

        self.exit_button = QPushButton(self.main_layout)
        self.exit_button.setObjectName(u"exit_button")

        self.verticalLayout.addWidget(self.exit_button)

        MainWindow.setCentralWidget(self.main_layout)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.window_title.setText(QCoreApplication.translate("MainWindow", u"LifeLog", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Sort by:", None))
        self.sorting_menu.setItemText(0, QCoreApplication.translate("MainWindow", u"Status", None))
        self.sorting_menu.setItemText(1, QCoreApplication.translate("MainWindow", u"Title", None))
        self.sorting_menu.setItemText(2, QCoreApplication.translate("MainWindow", u"Due Date", None))

        self.add_task_button.setText(QCoreApplication.translate("MainWindow", u"Add Task", None))
        self.delete_task_button.setText(QCoreApplication.translate("MainWindow", u"Delete Task", None))
        self.exit_button.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
    # retranslateUi

