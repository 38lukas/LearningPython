from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from storage import save_tasks

class DetailWindow(QWidget):
    """Window to view a task and toggle its status."""

    def __init__(self, controller):
        """Initialize the window and its widgets."""
        super().__init__()
        self.controller = controller
        self.current_task = None

        self.setWindowTitle("Task Detail")
        self.setGeometry(200, 200, 400, 400)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.label = QLabel()
        self.toggle_button = QPushButton("Toggle Status")
        layout.addWidget(self.label)
        layout.addWidget(self.toggle_button)

        self.toggle_button.clicked.connect(self.toggle_status)

    def set_task(self, task):
        """Display the given task."""
        self.current_task = task
        self.label.setText(f"{task.title} (Status: {task.status})")

    def toggle_status(self):
        """Toggle the status of the current task and update main screen."""
        if not self.current_task:
            return

        self.current_task.status = "done" if self.current_task.status == "pending" else "pending"
        self.label.setText(f"{self.current_task.title} (Status: {self.current_task.status})")
        self.controller.refresh_list()
        save_tasks(self.controller.tasks)
        self.controller.show_screen("Main")
