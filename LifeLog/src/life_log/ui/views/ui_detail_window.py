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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_DetailWindow(object):
    def setupUi(self, DetailWindow):
        if not DetailWindow.objectName():
            DetailWindow.setObjectName(u"DetailWindow")
        DetailWindow.resize(800, 600)
        self.verticalLayout = QVBoxLayout(DetailWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.info_layout = QVBoxLayout()
        self.info_layout.setObjectName(u"info_layout")
        self.titel_label = QLabel(DetailWindow)
        self.titel_label.setObjectName(u"titel_label")

        self.info_layout.addWidget(self.titel_label)

        self.status_layout = QHBoxLayout()
        self.status_layout.setObjectName(u"status_layout")
        self.status_label = QLabel(DetailWindow)
        self.status_label.setObjectName(u"status_label")

        self.status_layout.addWidget(self.status_label)

        self.status_menu = QComboBox(DetailWindow)
        self.status_menu.addItem("")
        self.status_menu.addItem("")
        self.status_menu.addItem("")
        self.status_menu.setObjectName(u"status_menu")
        self.status_menu.setEditable(False)

        self.status_layout.addWidget(self.status_menu)


        self.info_layout.addLayout(self.status_layout)

        self.description_label = QLabel(DetailWindow)
        self.description_label.setObjectName(u"description_label")

        self.info_layout.addWidget(self.description_label)

        self.description_entry = QTextEdit(DetailWindow)
        self.description_entry.setObjectName(u"description_entry")

        self.info_layout.addWidget(self.description_entry)


        self.verticalLayout.addLayout(self.info_layout)

        self.verticalSpacer = QSpacerItem(10, 200, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.back_button = QPushButton(DetailWindow)
        self.back_button.setObjectName(u"back_button")

        self.verticalLayout.addWidget(self.back_button)


        self.retranslateUi(DetailWindow)

        QMetaObject.connectSlotsByName(DetailWindow)
    # setupUi

    def retranslateUi(self, DetailWindow):
        DetailWindow.setWindowTitle(QCoreApplication.translate("DetailWindow", u"Task Detail", None))
        self.titel_label.setText(QCoreApplication.translate("DetailWindow", u"Task Title", None))
        self.status_label.setText(QCoreApplication.translate("DetailWindow", u"Status:", None))
        self.status_menu.setItemText(0, QCoreApplication.translate("DetailWindow", u"Pending", None))
        self.status_menu.setItemText(1, QCoreApplication.translate("DetailWindow", u"Finished", None))
        self.status_menu.setItemText(2, QCoreApplication.translate("DetailWindow", u"In Progress", None))

        self.status_menu.setCurrentText(QCoreApplication.translate("DetailWindow", u"Pending", None))
        self.description_label.setText(QCoreApplication.translate("DetailWindow", u"Description:", None))
        self.back_button.setText(QCoreApplication.translate("DetailWindow", u"Back", None))
    # retranslateUi

