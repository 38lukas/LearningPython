from src.life_log.model import (Task, dict_to_task, task_to_dict)
from src.life_log.storage import (save_tasks, load_tasks)
from src.life_log.ui.controller.main_window import MainWindow
from src.life_log.ui.controller.detail_window import DetailWindow
from src.life_log.ui.controller.main_window_controller import MainWindowController
from src.life_log.ui.controller.detail_window_controller import DetailWindowController
from src.life_log.ui.app_manager import ApplicationManager