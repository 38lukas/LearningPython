import csv
from pathlib import Path
from .model import Task, task_to_dict, dict_to_task

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)
TASKS_PATH = DATA_DIR / "tasks.csv"


def save_tasks(tasks: list[Task]):
    """Save a list of tasks to a CSV file.

    Args:
        tasks (list[Task]): List of tasks to save.
    """
    with open(TASKS_PATH, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["title", "status", "description", "due date"])
        writer.writeheader()
        for task in tasks:
            writer.writerow(task_to_dict(task))
    print("Tasks saved!")


def load_tasks() -> list[Task]:
    """Load tasks from the CSV file.

    Returns:
        list[Task]: List of Task objects loaded from the CSV.
    """
    if not TASKS_PATH.exists():
        return []
    with open(TASKS_PATH, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        print("Tasks loaded!")
        return [dict_to_task(row) for row in reader]
