from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLineEdit, QListWidget

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Life Tracker – ToDo")
        self.resize(400, 300)

        # Widgets
        self.input = QLineEdit()          # Eingabefeld für neue Aufgabe
        self.add_button = QPushButton("Aufgabe hinzufügen")
        self.list_widget = QListWidget()  # Liste für Aufgaben

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.add_button)
        layout.addWidget(self.list_widget)
        self.setLayout(layout)

        # Signals
        self.add_button.clicked.connect(self.add_task)

    def add_task(self):
        """Neue Aufgabe hinzufügen"""
        title = self.input.text()
        if title:
            self.list_widget.addItem(title)
            self.input.clear()
