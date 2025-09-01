from src.life_tracker import save_tasks

class DetailWindowController:
    def __init__(self, app_controller, view):
        self.app_controller = app_controller
        self.view = view

        self.view.status_menu.currentIndexChanged.connect(self.on_status_changed)
        self.view.back_button.clicked.connect(self.on_back_clicked)

    def on_status_changed(self):
        task = self.view.current_task
        if not task:
            return
        task.status = self.view.status_menu.currentText()
        self.view.status_label.setText(f"Status: {task.status}")
        self.app_controller.refresh_list()
        save_tasks(self.app_controller.tasks)

    def on_back_clicked(self):
        self.app_controller.show_screen("Main")
