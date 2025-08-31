import sys
from PyQt6.QtWidgets import QApplication

from src.life_tracker import AppController

def main():
    """Start the application."""
    app = QApplication(sys.argv)
    controller = AppController()
    controller.show_screen("Main")
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
