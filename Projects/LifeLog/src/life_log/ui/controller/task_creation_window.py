from datetime import datetime
from PySide6.QtWidgets import QWidget
from src.life_log import Task
from src.life_log.ui.views.ui_task_creation_window import Ui_creation_window


class TaskCreationWindow(QWidget, Ui_creation_window):
    """Window for creating a new task."""

    def __init__(self):
        """Initialize the TaskCreationWindow and set up the UI."""
        super().__init__()
        self.setupUi(self)
        self.due_date_edit.setDate(datetime.today().date())

    def reset_ui(self):
        """Reset all input fields to their default state."""
        self.title_edit.clear()
        self.due_date_edit.setDate(datetime.today().date())
        self.description_edit.clear()
