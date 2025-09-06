from PySide6.QtWidgets import QStackedWidget
from src.life_log import (
    Task, load_tasks, MainWindow, DetailWindow,
    MainWindowController, DetailWindowController,
    TaskCreationWindowController, TaskCreationWindow
)


class ApplicationManager:
    """Manages application state, windows, and task data."""

    def __init__(self, app):
        """Initialize the application manager and all windows/controllers.

        Args:
            app: The main QApplication instance.
        """
        self.app = app
        self.tasks: list[Task] = load_tasks()
        self.current_task_index: int | None = None

        # Windows
        self.main_window = MainWindow()
        self.detail_window = DetailWindow()
        self.task_creation_window = TaskCreationWindow()

        # Controllers
        self.main_controller = MainWindowController(self, self.main_window)
        self.detail_controller = DetailWindowController(self, self.detail_window)
        self.task_creation_controller = TaskCreationWindowController(self, self.task_creation_window)

        # Window stack
        self.window_stack = QStackedWidget()
        self.window_stack.addWidget(self.main_window)
        self.window_stack.addWidget(self.detail_window)
        self.window_stack.addWidget(self.task_creation_window)

        self.show_screen("Main")
        self.refresh_list()

    def show_screen(self, screen: str):
        """Switch to a specific screen in the stacked widget.

        Args:
            screen (str): The name of the screen to display ("Main", "Detail", "Task Creation").
        """
        if screen == "Main":
            self.window_stack.setCurrentWidget(self.main_window)
        elif screen == "Detail":
            self.window_stack.setCurrentWidget(self.detail_window)
        elif screen == "Task Creation":
            self.window_stack.setCurrentWidget(self.task_creation_window)
        else:
            print(f"Screen '{screen}' not found")

        print(f"Switching to screen: {screen}")
        self.window_stack.show()

    def refresh_list(self):
        """Refresh the task list in the main window and update optional info labels."""
        self.main_window.clear_task_list()
        for task in self.tasks:
            self.main_window.add_list_item(task)

        total = len(self.tasks)
        done = sum(1 for t in self.tasks if t.status.lower() == "done")
        if hasattr(self.main_window, "info_label"):
            self.main_window.info_label.setText(f"Tasks: {total}\nDone: {done}")
