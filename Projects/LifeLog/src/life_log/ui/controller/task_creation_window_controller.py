from src.life_log import Task, save_tasks


class TaskCreationWindowController:
    """Controller for TaskCreationWindow, handling task creation and navigation."""

    def __init__(self, app_manager, view):
        """Initialize the controller with the app manager and the view.

        Args:
            app_manager: The main application manager.
            view: The TaskCreationWindow instance.
        """
        self.app_manager = app_manager
        self.view = view

        self.view.create_button.pressed.connect(self.on_create_pressed)
        self.view.back_button.pressed.connect(self.on_back_pressed)

    def on_create_pressed(self):
        """Create a new task from input fields and save it."""
        title = self.view.title_edit.toPlainText().strip() or "No Title"
        description = self.view.description_edit.toPlainText().strip() or "No Description"
        due_date = self.view.due_date_edit.date().toPython()

        task = Task(title=title, description=description, due_date=due_date)

        self.app_manager.tasks.append(task)
        self.app_manager.refresh_list()
        save_tasks(self.app_manager.tasks)

        self.view.reset_ui()
        self.app_manager.show_screen("Main")

    def on_back_pressed(self):
        """Return to the main screen without creating a task."""
        self.app_manager.show_screen("Main")
