import csv
from pathlib import Path
from .model import Task, task_to_dict, dict_to_task

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)
TASKS_PATH = DATA_DIR / "tasks.csv" # Main Path

def save_tasks(tasks: list[Task]):
    """
    Saves task to a csv file

    Args:
        tasks (list[Task]): The Tasks you want to save
    """
    with open(TASKS_PATH, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["title", "status", "description", "due date"])
        writer.writeheader()
        for task in tasks:
            writer.writerow(task_to_dict(task))

    print("Task saved!")

def load_tasks() -> list[Task]:
    """
    Loads Tasks from a given csv

    Returns:
        tasks (list[Task]): The Tasks from the csv
    """
    if not TASKS_PATH.exists():
        return []
    with open(TASKS_PATH, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        print("Task loaded!")
        return [dict_to_task(row) for row in reader]
