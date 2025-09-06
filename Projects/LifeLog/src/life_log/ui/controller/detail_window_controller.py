from src.life_log import save_tasks
from src.life_log.constants import STATUS_COLOR
from datetime import date


class DetailWindowController:
    """Controller for the DetailWindow, handling task interactions and updates."""

    def __init__(self, app_manager, view):
        """Initialize the controller with the app manager and the view.

        Args:
            app_manager: The main application manager.
            view: The DetailWindow instance.
        """
        self.app_manager = app_manager
        self.view = view
        self.current_task = None

        self.view.status_menu.currentIndexChanged.connect(self.on_status_changed)
        self.view.back_button.pressed.connect(self.on_back_pressed)
        self.view.save_button.pressed.connect(self.on_save_pressed)
        self.view.title_apply_button.pressed.connect(self.on_title_apply_pressed)

    def set_task(self, task):
        """Load a task into the view for editing.

        Args:
            task: The Task object to display.
        """
        self.current_task = task
        self.view.set_title(task.title)
        self.view.set_status(task.status, STATUS_COLOR.get(task.status, "black"))
        self.view.set_description(task.description)
        self.view.set_due_date(task.due_date)

    def on_status_changed(self):
        """Update the status label in the view when the status menu changes."""
        if not self.current_task:
            return
        status_text = self.view.get_status_text()
        self.view.set_status(status_text, STATUS_COLOR.get(status_text, "black"))

    def on_title_apply_pressed(self):
        """Apply the current title from the entry field to the title label."""
        if not self.current_task:
            return
        self.view.set_title(self.view.get_title_text())

    def on_back_pressed(self):
        """Return to the main screen."""
        self.app_manager.show_screen("Main")

    def on_save_pressed(self):
        """Save the current task's data from the view and return to the main screen."""
        self.current_task.title = self.view.get_title_text()
        self.current_task.status = self.view.get_status_text()
        self.current_task.description = self.view.get_description_text()
        self.current_task.due_date = self.view.date_edit.date().toPython()

        self.app_manager.refresh_list()
        save_tasks(self.app_manager.tasks)
        print(f"Task successfully saved: {self.current_task.title}")
        self.app_manager.show_screen("Main")
