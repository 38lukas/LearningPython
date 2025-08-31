from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QListWidget, QListWidgetItem, QLabel
from PyQt6.QtCore import Qt

class MainWindow(QWidget):
    """Pure UI for displaying tasks and adding/deleting them."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Life Tracker")
        self.setGeometry(200, 200, 400, 400)

        layout = QVBoxLayout()
        self.setLayout(layout)

        # Input field for new tasks
        self.task_entry = QLineEdit()
        self.task_entry.setPlaceholderText("Enter new task")
        layout.addWidget(self.task_entry)

        self.add_button = QPushButton("Add Task")  # Add task button
        layout.addWidget(self.add_button)

        self.task_list = QListWidget() # Task list
        layout.addWidget(self.task_list)

        # Delete task button
        self.delete_button = QPushButton("Delete Selected Task")
        layout.addWidget(self.delete_button)

        # Info label (Statistik)
        self.info_label = QLabel("0 tasks (0 done)")
        layout.addWidget(self.info_label)

    def add_list_item(self, text: str):
        """Add a single item to the task list."""
        if text:
            item = QListWidgetItem(text)
            item.setTextAlignment(Qt.AlignmentFlag.AlignLeft)
            self.task_list.addItem(item)

    def clear_task_list(self):
        """Clear all items from the task list."""
        self.task_list.clear()
