from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QSpacerItem, QHBoxLayout, QComboBox


class DetailWindow(QWidget):
    """Pure UI for viewing a task and toggling status."""

    def __init__(self):
        super().__init__()
        self.current_task = None

        self.setWindowTitle("Task Detail")
        self.setGeometry(200, 200, 400, 400)

        # Hauptlayout
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Task info VBox
        self.info_layout = QVBoxLayout()
        layout.addLayout(self.info_layout)

        self.titel_label = QLabel()

        self.status_layout = QHBoxLayout()
        self.status_label = QLabel()
        self.status_layout.addWidget(self.status_label)

        self.info_layout.addWidget(self.titel_label)
        self.info_layout.addLayout(self.status_layout)

        self.status_menu = QComboBox()
        self.status_menu.addItem("Pending")
        self.status_menu.addItem("In Progress")
        self.status_menu.addItem("Finished")

        self.status_layout.addWidget(self.status_menu)

        # Spacer
        self.spacer = QSpacerItem(10, 200)
        layout.addItem(self.spacer)

        # Back
        self.back_button = QPushButton("Back")
        layout.addWidget(self.back_button)

    def set_task(self, task):
        """Display the given task."""
        self.current_task = task
        self.titel_label.setText(f"Titel: {task.title}")
        self.status_label.setText(f"Status: {task.status}")
