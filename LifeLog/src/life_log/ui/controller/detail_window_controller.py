from PyQt6.QtWidgets import QPushButton, QTextEdit

from src.life_log import save_tasks

class DetailWindowController:
    def __init__(self, app_manager, view):
        self.app_manager = app_manager
        self.view = view

        self.view.status_menu.currentIndexChanged.connect(self.on_status_changed)
        self.view.back_button.clicked.connect(self.on_back_clicked)
        self.view.description_entry.textChanged.connect(self.on_description_changed)

    def on_status_changed(self):
        task = self.view.current_task
        if not task:
            return

        task.status = self.view.status_menu.currentText()
        self.view.set_task(task)

    def on_description_changed(self):
        task = self.view.current_task
        if not task:
            return
        task.description = self.view.description_entry.toPlainText()

    def on_back_clicked(self):
        self.app_manager.refresh_list()
        save_tasks(self.app_manager.tasks)

        self.app_manager.show_screen("Main")