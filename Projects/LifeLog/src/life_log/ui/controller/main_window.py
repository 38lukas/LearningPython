from PySide6.QtGui import Qt
from PySide6.QtWidgets import QMainWindow, QListWidgetItem, QWidget, QLabel, QHBoxLayout
from src.life_log import Task
from src.life_log.ui.views.ui_main_window import Ui_MainWindow
from src.life_log.constants import STATUS_COLOR


class MainWindow(QMainWindow, Ui_MainWindow):
    """Main window displaying a list of tasks with status, title, and due date."""

    def __init__(self, parent=None):
        """Initialize the MainWindow and set up the UI."""
        super().__init__(parent)
        self.setupUi(self)
        self.controller = None

    def add_list_item(self, task: Task):
        """Add a task to the list view with a custom widget.

        Args:
            task (Task): The task to add.
        """
        if not task:
            return

        item = QListWidgetItem()
        item.setData(Qt.UserRole, task.status or "")
        item.setData(Qt.UserRole + 1, task.title or "")
        item.setData(Qt.UserRole + 2, task.due_date)
        item.setToolTip(task.description)

        widget = QWidget()
        layout = QHBoxLayout()
        layout.setContentsMargins(5, 2, 5, 2)
        layout.setSpacing(10)
        widget.setLayout(layout)

        status_label = QLabel(task.status)
        status_label.setStyleSheet(f"color:{STATUS_COLOR.get(task.status,'black')}; font-weight:bold;")
        status_label.setFixedWidth(100)

        title_label = QLabel(task.title)
        due_date_label = QLabel(task.due_date.strftime('%d.%m.%Y') if task.due_date else "")

        layout.addWidget(status_label)
        layout.addWidget(title_label)
        layout.addWidget(due_date_label)

        self.task_list.addItem(item)
        self.task_list.setItemWidget(item, widget)
        item.setSizeHint(widget.sizeHint())

    def clear_task_list(self):
        """Clear all tasks from the list view."""
        for i in range(self.task_list.count()):
            widget = self.task_list.itemWidget(self.task_list.item(i))
            if widget:
                widget.deleteLater()
        self.task_list.clear()

    def sort_by_status(self):
        """Sort tasks by status using the controller."""
        if self.controller:
            self.controller.sort_tasks("status")

    def sort_by_title(self):
        """Sort tasks by title using the controller."""
        if self.controller:
            self.controller.sort_tasks("title")

    def sort_by_due_date(self):
        """Sort tasks by due date using the controller."""
        if self.controller:
            self.controller.sort_tasks("due_date")

    def refresh_task_list(self, tasks):
        """Refresh the task list with the provided tasks.

        Args:
            tasks (list[Task]): List of tasks to display.
        """
        self.clear_task_list()
        for task in tasks:
            self.add_list_item(task)
