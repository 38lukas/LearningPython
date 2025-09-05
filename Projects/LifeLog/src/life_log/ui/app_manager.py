from PySide6.QtWidgets import QStackedWidget
from src.life_log import Task
from src.life_log import load_tasks
from src.life_log import MainWindow
from src.life_log import DetailWindow
from src.life_log import MainWindowController
from src.life_log import DetailWindowController

class ApplicationManager:
    def __init__(self, app):
        self.app = app

        self.tasks: list[Task] = load_tasks()
        self.current_task_index: int | None = None

        self.main_window = MainWindow()
        self.detail_window = DetailWindow()

        self.main_controller = MainWindowController(self, self.main_window)
        self.detail_controller = DetailWindowController(self, self.detail_window)

        self.window_stack = QStackedWidget()
        self.window_stack.addWidget(self.main_window)
        self.window_stack.addWidget(self.detail_window)

        self.show_screen("Main")
        self.refresh_list()

    def show_screen(self, screen: str):
        if screen == "Main":
            self.window_stack.setCurrentWidget(self.main_window)
        elif screen == "Detail":
            self.window_stack.setCurrentWidget(self.detail_window)
        else:
            print(f"Screen '{screen}' not found")
        self.window_stack.show()

    def refresh_list(self):
        self.main_window.clear_task_list()
        for task in self.tasks:
            self.main_window.add_list_item(task)

        # Optional info
        total = len(self.tasks)
        done = sum(1 for t in self.tasks if t.status.lower() == "done")
        if hasattr(self.main_window, "info_label"):
            self.main_window.info_label.setText(f"Tasks: {total}\nDone: {done}")
