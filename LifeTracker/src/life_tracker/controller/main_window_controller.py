from src.life_tracker import (Task, save_tasks)

class MainWindowController:
    """Controller for MainWindow actions (add, delete tasks)."""

    def __init__(self, app_controller, view):
        self.app_controller = app_controller
        self.view = view

        # Connect events from the UI to controller methods
        self.view.add_button.clicked.connect(self.add_task)
        self.view.delete_button.clicked.connect(self.delete_task)
        self.view.task_entry.returnPressed.connect(self.add_task)
        self.view.task_list.itemDoubleClicked.connect(self.open_detail_screen)

    def add_task(self):
        """Add a new task from input field."""
        title = self.view.task_entry.text().strip()
        if not title:
            return
        new_task = Task(title=title, status="Pending")
        self.app_controller.tasks.append(new_task)
        self.view.task_entry.clear()
        self.app_controller.refresh_list()
        save_tasks(self.app_controller.tasks)

    def delete_task(self):
        """Delete the selected task."""
        row = self.view.task_list.currentRow()
        if row < 0 or row >= len(self.app_controller.tasks):
            return

        del self.app_controller.tasks[row]
        self.app_controller.refresh_list()
        save_tasks(self.app_controller.tasks)

    def open_detail_screen(self, item):
        """Open the detail screen for a double-clicked task."""
        row = self.view.task_list.row(item)
        if row < 0 or row >= len(self.app_controller.tasks):
            return

        self.app_controller.current_task_index = row
        task = self.app_controller.tasks[row]

        # Set task in DetailWindow and switch
        self.app_controller.detail_window.set_task(task)
        self.app_controller.show_screen("Detail")
