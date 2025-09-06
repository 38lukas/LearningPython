from datetime import date
from src.life_log import save_tasks


class MainWindowController:
    """Controller for MainWindow, handling task list operations and user interactions."""

    def __init__(self, app_manager, view):
        """Initialize the controller with the app manager and the view.

        Args:
            app_manager: The main application manager.
            view: The MainWindow instance.
        """
        self.app_manager = app_manager
        self.view = view
        self.view.controller = self

        self.view.add_task_button.pressed.connect(self.on_add_task_pressed)
        self.view.delete_task_button.pressed.connect(self.delete_task)
        self.view.exit_button.pressed.connect(self.on_exit_button_pressed)
        self.view.task_list.itemDoubleClicked.connect(self.open_detail_screen)
        self.view.sorting_menu.currentIndexChanged.connect(self.on_sorting_menu_changed)
        self.sort_tasks("status")

    def on_add_task_pressed(self):
        """Open the task creation screen and reset its UI."""
        self.app_manager.show_screen("Task Creation")
        self.app_manager.task_creation_window.reset_ui()

    def delete_task(self):
        """Delete the currently selected task and refresh the list."""
        row = self.view.task_list.currentRow()
        if 0 <= row < len(self.app_manager.tasks):
            del self.app_manager.tasks[row]
            self.app_manager.refresh_list()
            save_tasks(self.app_manager.tasks)

    def open_detail_screen(self, item):
        """Open the detail screen for a double-clicked task.

        Args:
            item (QListWidgetItem): The list item that was double-clicked.
        """
        row = self.view.task_list.row(item)
        if 0 <= row < len(self.app_manager.tasks):
            self.app_manager.current_task_index = row
            task = self.app_manager.tasks[row]
            self.app_manager.detail_controller.set_task(task)
            self.app_manager.show_screen("Detail")

    def on_exit_button_pressed(self):
        """Quit the application."""
        print("Ending Application...")
        self.app_manager.app.quit()

    def on_sorting_menu_changed(self, index):
        """Sort tasks based on the selected sorting menu index.

        Args:
            index (int): The index of the selected sorting option.
        """
        if index == 0:
            self.sort_tasks("status")
        elif index == 1:
            self.sort_tasks("title")
        elif index == 2:
            self.sort_tasks("due_date")

    def sort_tasks(self, mode: str):
        """Sort tasks according to the specified mode and refresh the list.

        Args:
            mode (str): Sorting mode ('status', 'title', or 'due_date').
        """
        if mode == "status":
            order = {"Pending": 0, "In Progress": 1, "Finished": 2}
            self.app_manager.tasks.sort(key=lambda t: order.get(t.status, 99))
        elif mode == "title":
            self.app_manager.tasks.sort(key=lambda t: (t.title or "").lower())
        elif mode == "due_date":
            self.app_manager.tasks.sort(key=lambda t: t.due_date or date.max)

        self.view.refresh_task_list(self.app_manager.tasks)
