# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'task_creation_window.ui'
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
from PySide6.QtWidgets import (QApplication, QDateTimeEdit, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_creation_window(object):
    def setupUi(self, creation_window):
        if not creation_window.objectName():
            creation_window.setObjectName(u"creation_window")
        creation_window.resize(509, 322)
        creation_window.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_2 = QVBoxLayout(creation_window)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.window_title = QLabel(creation_window)
        self.window_title.setObjectName(u"window_title")
        font = QFont()
        font.setBold(True)
        self.window_title.setFont(font)
        self.window_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.window_title)

        self.title_layout = QHBoxLayout()
        self.title_layout.setObjectName(u"title_layout")
        self.title_label = QLabel(creation_window)
        self.title_label.setObjectName(u"title_label")

        self.title_layout.addWidget(self.title_label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.title_layout.addItem(self.horizontalSpacer)

        self.title_edit = QTextEdit(creation_window)
        self.title_edit.setObjectName(u"title_edit")
        self.title_edit.setMaximumSize(QSize(16777215, 26))

        self.title_layout.addWidget(self.title_edit)


        self.verticalLayout_2.addLayout(self.title_layout)

        self.due_date_layout = QHBoxLayout()
        self.due_date_layout.setObjectName(u"due_date_layout")
        self.due_date_label = QLabel(creation_window)
        self.due_date_label.setObjectName(u"due_date_label")

        self.due_date_layout.addWidget(self.due_date_label)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.due_date_layout.addItem(self.horizontalSpacer_3)

        self.due_date_edit = QDateTimeEdit(creation_window)
        self.due_date_edit.setObjectName(u"due_date_edit")
        self.due_date_edit.setMinimumSize(QSize(200, 0))

        self.due_date_layout.addWidget(self.due_date_edit)


        self.verticalLayout_2.addLayout(self.due_date_layout)

        self.description_layout = QHBoxLayout()
        self.description_layout.setObjectName(u"description_layout")
        self.description_label = QLabel(creation_window)
        self.description_label.setObjectName(u"description_label")
        self.description_label.setMinimumSize(QSize(0, 0))
        self.description_label.setMaximumSize(QSize(16777215, 40))

        self.description_layout.addWidget(self.description_label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.description_layout.addItem(self.horizontalSpacer_2)

        self.description_edit = QTextEdit(creation_window)
        self.description_edit.setObjectName(u"description_edit")
        self.description_edit.setMaximumSize(QSize(16777215, 50))

        self.description_layout.addWidget(self.description_edit)


        self.verticalLayout_2.addLayout(self.description_layout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.button_layout = QHBoxLayout()
        self.button_layout.setObjectName(u"button_layout")
        self.button_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.button_layout.addItem(self.button_spacer)

        self.back_button = QPushButton(creation_window)
        self.back_button.setObjectName(u"back_button")

        self.button_layout.addWidget(self.back_button)

        self.create_button = QPushButton(creation_window)
        self.create_button.setObjectName(u"create_button")

        self.button_layout.addWidget(self.create_button)

        self.button_spacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.button_layout.addItem(self.button_spacer_2)


        self.verticalLayout_2.addLayout(self.button_layout)


        self.retranslateUi(creation_window)

        QMetaObject.connectSlotsByName(creation_window)
    # setupUi

    def retranslateUi(self, creation_window):
        creation_window.setWindowTitle(QCoreApplication.translate("creation_window", u"Widget", None))
        self.window_title.setText(QCoreApplication.translate("creation_window", u"Task Creation", None))
        self.title_label.setText(QCoreApplication.translate("creation_window", u"Title:", None))
        self.due_date_label.setText(QCoreApplication.translate("creation_window", u"Due Date: ", None))
        self.due_date_edit.setDisplayFormat(QCoreApplication.translate("creation_window", u"dd.MM.yyyy", None))
        self.description_label.setText(QCoreApplication.translate("creation_window", u"Description", None))
        self.back_button.setText(QCoreApplication.translate("creation_window", u"Back", None))
        self.create_button.setText(QCoreApplication.translate("creation_window", u"Create", None))
    # retranslateUi

