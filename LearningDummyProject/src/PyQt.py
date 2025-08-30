import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QLineEdit

def on_click():
    label.setText(eingabe_feld.text())

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Widgets Beispiel")
window.resize(900, 500)

# Widgets
eingabe_feld = QLineEdit()
button = QPushButton("Klick mich")
label = QLabel("Noch nichts passiert...")

# Signal verbinden
button.clicked.connect(on_click)

# Layout
layout = QVBoxLayout()
layout.addWidget(eingabe_feld)
layout.addWidget(label)
layout.addWidget(button)
window.setLayout(layout)

window.show()
sys.exit(app.exec())
