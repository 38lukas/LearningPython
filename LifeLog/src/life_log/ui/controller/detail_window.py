from PySide6.QtWidgets import QWidget

from src.life_log.ui.views.ui_detail_window import Ui_DetailWindow


class DetailWindow(QWidget, Ui_DetailWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def set_title(self, title):
        self.title_label.setText(title)
        self.title_label.setStyleSheet("font-weight: bold")

    def set_status(self, status, color):
        self.status_label.setText(status)
        self.status_label.setStyleSheet(f"color: {color}; font-weight: bold;")

    def set_description(self, description):
        self.description_entry.setText(description)

    def get_title_text(self):
        return self.title_entry.toPlainText()

    def get_description_text(self):
        return self.description_entry.toPlainText()

    def get_status_text(self):
        return self.status_menu.currentText()
