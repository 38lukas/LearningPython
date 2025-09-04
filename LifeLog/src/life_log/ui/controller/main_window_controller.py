from src.life_log import Task
from src.life_log import save_tasks

class MainWindowController:
    def __init__(self, app_manager, view):
        self.app_manager = app_manager
        self.view = view

        # Setting up signals
        self.view.add_task_button.pressed.connect(self.add_task)
        self.view.delete_task_button.pressed.connect(self.delete_task)
        self.view.exit_button.pressed.connect(self.on_exit_button_pressed)

        self.view.task_entry.returnPressed.connect(self.add_task)   # Using Enter
        self.view.task_list.itemDoubleClicked.connect(self.open_detail_screen)


    def add_task(self):
        title = self.view.task_entry.text().strip()
        if not title:
            return
        task = Task(title=title, status="Pending")
        self.app_manager.tasks.append(task)
        self.view.task_entry.clear()
        self.app_manager.refresh_list()
        save_tasks(self.app_manager.tasks)

    def delete_task(self):
        row = self.view.task_list.currentRow()
        if 0 <= row < len(self.app_manager.tasks):
            del self.app_manager.tasks[row]
            self.app_manager.refresh_list()
            save_tasks(self.app_manager.tasks)

    def open_detail_screen(self, item):
        row = self.view.task_list.row(item)
        if 0 <= row < len(self.app_manager.tasks):
            self.app_manager.current_task_index = row
            task = self.app_manager.tasks[row]
            self.app_manager.detail_controller.set_task(task)
            self.app_manager.show_screen("Detail")

    def on_exit_button_pressed(self):
        print("Ending Application...")
        self.app_manager.app.quit()