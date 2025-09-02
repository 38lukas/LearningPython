from PySide6.QtWidgets import QWidget
from ..views.ui_detail_window import Ui_DetailWindow

class DetailWindow(QWidget, Ui_DetailWindow):
    def __init__(self):
        super().__init__()
        self.current_task = None
        self.setupUi(self)


    def set_task(self, task):
        self.current_task = task
        self.titel_label.setText(f"Titel: {task.title}")
        self.status_label.setText(f"Status: {task.status}")
        self.description_entry.setText(f"{task.description}")
        self.status_menu.setCurrentText(task.status)
