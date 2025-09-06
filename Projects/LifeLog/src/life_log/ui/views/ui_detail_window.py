# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'detail_window.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateTimeEdit, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_DetailWindow(object):
    def setupUi(self, DetailWindow):
        if not DetailWindow.objectName():
            DetailWindow.setObjectName(u"DetailWindow")
        DetailWindow.resize(448, 326)
        self.verticalLayout = QVBoxLayout(DetailWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(DetailWindow)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.info_layout = QVBoxLayout()
        self.info_layout.setObjectName(u"info_layout")
        self.title_layout = QHBoxLayout()
        self.title_layout.setObjectName(u"title_layout")
        self.title_titel = QLabel(DetailWindow)
        self.title_titel.setObjectName(u"title_titel")

        self.title_layout.addWidget(self.title_titel)

        self.title_label = QLabel(DetailWindow)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setMinimumSize(QSize(0, 0))

        self.title_layout.addWidget(self.title_label)

        self.title_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.title_layout.addItem(self.title_spacer)

        self.title_entry = QTextEdit(DetailWindow)
        self.title_entry.setObjectName(u"title_entry")
        self.title_entry.setMinimumSize(QSize(175, 0))
        self.title_entry.setMaximumSize(QSize(100, 26))

        self.title_layout.addWidget(self.title_entry)

        self.title_apply_button = QPushButton(DetailWindow)
        self.title_apply_button.setObjectName(u"title_apply_button")

        self.title_layout.addWidget(self.title_apply_button)


        self.info_layout.addLayout(self.title_layout)

        self.status_layout = QHBoxLayout()
        self.status_layout.setObjectName(u"status_layout")
        self.status_title = QLabel(DetailWindow)
        self.status_title.setObjectName(u"status_title")

        self.status_layout.addWidget(self.status_title)

        self.status_label = QLabel(DetailWindow)
        self.status_label.setObjectName(u"status_label")
        self.status_label.setMinimumSize(QSize(80, 0))

        self.status_layout.addWidget(self.status_label)

        self.status_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.status_layout.addItem(self.status_spacer)

        self.status_menu = QComboBox(DetailWindow)
        self.status_menu.addItem("")
        self.status_menu.addItem("")
        self.status_menu.addItem("")
        self.status_menu.setObjectName(u"status_menu")
        self.status_menu.setEditable(False)

        self.status_layout.addWidget(self.status_menu)


        self.info_layout.addLayout(self.status_layout)

        self.due_date_layout = QHBoxLayout()
        self.due_date_layout.setObjectName(u"due_date_layout")
        self.date_label = QLabel(DetailWindow)
        self.date_label.setObjectName(u"date_label")

        self.due_date_layout.addWidget(self.date_label)

        self.date_edit = QDateTimeEdit(DetailWindow)
        self.date_edit.setObjectName(u"date_edit")

        self.due_date_layout.addWidget(self.date_edit)


        self.info_layout.addLayout(self.due_date_layout)

        self.description_layout = QHBoxLayout()
        self.description_layout.setObjectName(u"description_layout")
        self.description_label = QLabel(DetailWindow)
        self.description_label.setObjectName(u"description_label")

        self.description_layout.addWidget(self.description_label)

        self.description_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.description_layout.addItem(self.description_spacer)

        self.description_entry = QTextEdit(DetailWindow)
        self.description_entry.setObjectName(u"description_entry")
        self.description_entry.setMaximumSize(QSize(16777215, 50))

        self.description_layout.addWidget(self.description_entry)


        self.info_layout.addLayout(self.description_layout)


        self.verticalLayout.addLayout(self.info_layout)

        self.verticalSpacer = QSpacerItem(10, 200, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.button_layout = QHBoxLayout()
        self.button_layout.setObjectName(u"button_layout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.button_layout.addItem(self.horizontalSpacer)

        self.back_button = QPushButton(DetailWindow)
        self.back_button.setObjectName(u"back_button")

        self.button_layout.addWidget(self.back_button)

        self.save_button = QPushButton(DetailWindow)
        self.save_button.setObjectName(u"save_button")

        self.button_layout.addWidget(self.save_button)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.button_layout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.button_layout)


        self.retranslateUi(DetailWindow)

        QMetaObject.connectSlotsByName(DetailWindow)
    # setupUi

    def retranslateUi(self, DetailWindow):
        DetailWindow.setWindowTitle(QCoreApplication.translate("DetailWindow", u"Task Detail", None))
        self.label.setText(QCoreApplication.translate("DetailWindow", u"Task Details", None))
        self.title_titel.setText(QCoreApplication.translate("DetailWindow", u"Titel:", None))
        self.title_label.setText(QCoreApplication.translate("DetailWindow", u"Task Title", None))
        self.title_apply_button.setText(QCoreApplication.translate("DetailWindow", u"Change", None))
        self.status_title.setText(QCoreApplication.translate("DetailWindow", u"Status:", None))
        self.status_label.setText(QCoreApplication.translate("DetailWindow", u"Pending", None))
        self.status_menu.setItemText(0, QCoreApplication.translate("DetailWindow", u"Pending", None))
        self.status_menu.setItemText(1, QCoreApplication.translate("DetailWindow", u"Finished", None))
        self.status_menu.setItemText(2, QCoreApplication.translate("DetailWindow", u"In Progress", None))

        self.status_menu.setCurrentText(QCoreApplication.translate("DetailWindow", u"Pending", None))
        self.date_label.setText(QCoreApplication.translate("DetailWindow", u"Due Date:", None))
        self.date_edit.setDisplayFormat(QCoreApplication.translate("DetailWindow", u"dd.MM.yyyy", None))
        self.description_label.setText(QCoreApplication.translate("DetailWindow", u"Description:", None))
        self.back_button.setText(QCoreApplication.translate("DetailWindow", u"Back", None))
        self.save_button.setText(QCoreApplication.translate("DetailWindow", u"Save", None))
    # retranslateUi

