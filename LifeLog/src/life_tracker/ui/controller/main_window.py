from PySide6.QtGui import Qt
from PySide6.QtWidgets import QMainWindow, QListWidgetItem
from src.life_tracker.ui.views.ui_main_window import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

    def add_list_item(self, text: str):
        if text:
            item = QListWidgetItem(text)
            item.setTextAlignment(Qt.AlignmentFlag.AlignLeft)
            self.task_list.addItem(item)

    def clear_task_list(self):
        self.task_list.clear()
