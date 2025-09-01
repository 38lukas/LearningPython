from src.life_tracker import Task
from src.life_tracker import save_tasks

class MainWindowController:
    def __init__(self, app_controller, view):
        self.app_controller = app_controller
        self.view = view

        self.view.add_task_button.clicked.connect(self.add_task)
        self.view.delete_task_button.clicked.connect(self.delete_task)
        self.view.task_entry.returnPressed.connect(self.add_task)
        self.view.task_list.itemDoubleClicked.connect(self.open_detail_screen)

    def add_task(self):
        title = self.view.task_entry.text().strip()
        if not title:
            return
        task = Task(title=title, status="Pending")
        self.app_controller.tasks.append(task)
        self.view.task_entry.clear()
        self.app_controller.refresh_list()
        save_tasks(self.app_controller.tasks)

    def delete_task(self):
        row = self.view.task_list.currentRow()
        if 0 <= row < len(self.app_controller.tasks):
            del self.app_controller.tasks[row]
            self.app_controller.refresh_list()
            save_tasks(self.app_controller.tasks)

    def open_detail_screen(self, item):
        row = self.view.task_list.row(item)
        if 0 <= row < len(self.app_controller.tasks):
            self.app_controller.current_task_index = row
            task = self.app_controller.tasks[row]
            self.app_controller.detail_window.set_task(task)
            self.app_controller.show_screen("Detail")
