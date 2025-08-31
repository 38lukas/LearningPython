import sys
from PyQt6.QtWidgets import QApplication, QStackedWidget
from model import Task
from storage import save_tasks, load_tasks
from ui.main_window import MainWindow
from ui.detail_window import DetailWindow

class Controller:
    """Main controller managing tasks and screen navigation."""

    def __init__(self):
        """Initialize the controller, load tasks, and setup UI."""
        # Load tasks from CSV
        self.tasks: list[Task] = load_tasks()
        self.current_task_index = None

        # Create UI screens
        self.main_window = MainWindow(self)
        self.detail_window = DetailWindow(self)

        # Stack screens in QStackedWidget
        self.window_stack = QStackedWidget()
        self.window_stack.addWidget(self.main_window)
        self.window_stack.addWidget(self.detail_window)

        # Show main screen initially
        self.refresh_list()

    def show_screen(self, screen: str):
        """
        Switch between Main and Detail screens.

        Args:
            screen: 'Main' or 'Detail'
        """
        if not screen:
            return

        match screen:
            case "Main":
                self.window_stack.setCurrentWidget(self.main_window)
            case "Detail":
                self.window_stack.setCurrentWidget(self.detail_window)
            case _:
                print("Error: Screen not found!")

        self.window_stack.show()

    def refresh_list(self):
        """Refresh the task list displayed in MainWindow."""
        self.main_window.clear_task_list()
        for task in self.tasks:
            status_icon = "✅ " if task.status == "done" else "❌ "
            self.main_window.add_list_item(status_icon + task.title)

    def add_task(self):
        """Add a new task from MainWindow input."""
        title = self.main_window.task_entry.text().strip()
        if not title:
            return
        new_task = Task(title=title, status="pending")
        self.tasks.append(new_task)
        self.main_window.task_entry.clear()
        self.refresh_list()
        save_tasks(self.tasks)

    def delete_task(self):
        """Delete the selected task from the list."""
        row = self.main_window.task_list.currentRow()
        if row < 0 or row >= len(self.tasks):
            return

        del self.tasks[row]
        self.refresh_list()
        save_tasks(self.tasks)

    def open_detail_screen(self, item):
        """
        Open the DetailWindow for the double-clicked task.

        Args:
            item: QListWidgetItem that was double-clicked
        """
        row = self.main_window.task_list.row(item)
        if row < 0 or row >= len(self.tasks):
            return

        self.current_task_index = row
        task = self.tasks[row]

        # Set task in DetailWindow and switch screen
        self.detail_window.set_task(task)
        self.show_screen("Detail")


def main():
    """Start the application."""
    app = QApplication(sys.argv)
    controller = Controller()
    controller.show_screen("Main")
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
