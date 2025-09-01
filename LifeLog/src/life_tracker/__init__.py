from src.life_tracker.model import (Task, dict_to_task, task_to_dict)
from src.life_tracker.storage import (save_tasks, load_tasks)
from src.life_tracker.ui.controller.main_window import MainWindow
from src.life_tracker.ui.controller.detail_window import DetailWindow
from src.life_tracker.ui.controller.main_window_controller import MainWindowController
from src.life_tracker.ui.controller.detail_window_controller import DetailWindowController
from src.life_tracker.ui.app_manager import ApplicationManager