from src.life_log import save_tasks
from src.life_log.constants import STATUS_COLOR


class DetailWindowController:
    def __init__(self, app_manager, view):
        self.app_manager = app_manager
        self.view = view
        self.current_task = None

        self.view.status_menu.currentIndexChanged.connect(self.on_status_changed)
        self.view.back_button.clicked.connect(self.on_back_clicked)
        self.view.description_entry.textChanged.connect(self.on_description_changed)
        self.view.title_apply_button.pressed.connect(self.on_title_apply_pressed)

    def set_task(self, task):
        self.current_task = task
        self.view.set_title(task.title)
        self.view.set_status(task.status, STATUS_COLOR.get(task.status, "black"))
        self.view.set_description(task.description)

    def on_status_changed(self):
        if not self.current_task:
            return
        self.current_task.status = self.view.get_status_text()
        self.set_task(self.current_task)  # View aktualisieren

    def on_description_changed(self):
        if not self.current_task:
            return
        self.current_task.description = self.view.get_description_text()

    def on_title_apply_pressed(self):
        if not self.current_task:
            return
        self.current_task.title = self.view.get_title_text()
        self.set_task(self.current_task)
        print(f"Title successfully applied: {self.current_task.title}")

    def on_back_clicked(self):
        self.app_manager.refresh_list()
        save_tasks(self.app_manager.tasks)
        self.app_manager.show_screen("Main")
