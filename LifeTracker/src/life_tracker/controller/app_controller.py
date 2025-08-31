from PyQt6.QtWidgets import QStackedWidget, QListWidgetItem

from src.life_tracker import (Task, load_tasks, MainWindow,
                              DetailWindow, MainWindowController,
                              DetailWindowController)

class AppController:
    """Main application controller managing tasks and screen navigation."""

    def __init__(self):
        # Load tasks from CSV
        self.tasks: list[Task] = load_tasks()
        self.current_task_index = None

        # Create UI windows
        self.main_window = MainWindow()
        self.detail_window = DetailWindow()

        # Create sub-controllers for each window
        self.main_controller = MainWindowController(self, self.main_window)
        self.detail_controller = DetailWindowController(self, self.detail_window)

        # Stack screens
        self.window_stack = QStackedWidget()
        self.window_stack.addWidget(self.main_window)
        self.window_stack.addWidget(self.detail_window)

        # Show initial screen
        self.refresh_list()

    def show_screen(self, screen: str):
        """Switch between Main and Detail screens."""
        match screen:
            case "Main":
                self.window_stack.setCurrentWidget(self.main_window)
            case "Detail":
                self.window_stack.setCurrentWidget(self.detail_window)
            case _:
                print("Error: Screen not found!")

        self.window_stack.show()

    def refresh_list(self):
        """Refresh the task list in MainWindow."""
        self.main_window.clear_task_list()

        for task in self.tasks:

            status_prefix = f"[{task.status}]  "
            self.main_window.add_list_item(status_prefix + task.title)

        # Update info label (extra feature)
        total = len(self.tasks)
        done = sum(1 for t in self.tasks if t.status == "done")
        self.main_window.info_label.setText(f"Tasks: {total}\n" + f"Done: {done}")
