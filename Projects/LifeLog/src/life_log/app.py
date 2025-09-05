import sys
import datetime
from PySide6.QtWidgets import QApplication
from src.life_log import ApplicationManager

def main():
    """
    Starts the application
    """
    app = QApplication(sys.argv)
    app_manager = ApplicationManager(app)
    app_manager.show_screen("Main")
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
