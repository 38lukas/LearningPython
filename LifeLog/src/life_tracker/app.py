import sys
from PySide6.QtWidgets import QApplication
from src.life_tracker import ApplicationManager

def main():
    app = QApplication(sys.argv)
    controller = ApplicationManager()
    controller.show_screen("Main")
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
