from PySide6.QtGui import Qt, QColor
from PySide6.QtWidgets import QMainWindow, QListWidgetItem, QWidget, QLabel, QHBoxLayout

from src.life_log import Task
from src.life_log.ui.views.ui_main_window import Ui_MainWindow
from src.life_log.constants import STATUS_COLOR


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

    def add_list_item(self, task: Task):
        if not task:
            return

        item = QListWidgetItem()
        widget = QWidget()
        layout = QHBoxLayout()
        layout.setContentsMargins(5, 2, 5, 2)
        layout.setSpacing(10)
        widget.setLayout(layout)

        # Setting up Labels
        status_label = QLabel(f"{task.status}")
        status_label.setStyleSheet(f"color: {STATUS_COLOR.get(task.status, 'black')}; font-weight: bold;")
        status_label.setFixedWidth(100)
        title_label = QLabel(task.title)

        date_str = task.due_date.strftime('%d.%m.%Y')
        due_date_label = QLabel(date_str)


        layout.addWidget(status_label)
        layout.addWidget(title_label)
        layout.addWidget(due_date_label)

        # Adding to the List
        self.task_list.addItem(item)
        self.task_list.setItemWidget(item, widget)
        item.setSizeHint(widget.sizeHint())
        item.setToolTip(task.description)

    def clear_task_list(self):
        self.task_list.clear()
