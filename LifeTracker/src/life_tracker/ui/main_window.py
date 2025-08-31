from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QListWidget, QListWidgetItem
from PyQt6.QtCore import Qt

class MainWindow(QWidget):
    """Main window to display tasks and add/delete them."""

    def __init__(self, controller):
        """Initialize the main window and its widgets."""
        super().__init__()
        self.controller = controller
        self.setWindowTitle("Life Tracker")
        self.setGeometry(200, 200, 400, 400)

        layout = QVBoxLayout()
        self.setLayout(layout)

        # Input field for new tasks
        self.task_entry = QLineEdit()
        self.task_entry.setPlaceholderText("Enter new task")
        layout.addWidget(self.task_entry)

        # Add task button
        self.add_button = QPushButton("Add Task")
        layout.addWidget(self.add_button)

        # Task list
        self.task_list = QListWidget()
        layout.addWidget(self.task_list)

        # Delete task button
        self.delete_button = QPushButton("Delete Selected Task")
        layout.addWidget(self.delete_button)

        # Connect events
        self.add_button.clicked.connect(self.controller.add_task)
        self.delete_button.clicked.connect(self.controller.delete_task)
        self.task_entry.returnPressed.connect(self.controller.add_task)
        self.task_list.itemDoubleClicked.connect(self.controller.open_detail_screen)

    def add_list_item(self, text: str):
        """Add a single item to the task list."""
        if text:
            item = QListWidgetItem(text)
            item.setTextAlignment(Qt.AlignmentFlag.AlignLeft)
            self.task_list.addItem(item)

    def clear_task_list(self):
        """Clear all items from the task list."""
        self.task_list.clear()
