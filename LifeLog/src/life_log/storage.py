import csv
from pathlib import Path
from .model import Task, task_to_dict, dict_to_task

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)
TASKS_PATH = DATA_DIR / "tasks.csv"

def save_tasks(tasks: list[Task]):
    with open(TASKS_PATH, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["title", "status", "description"])
        writer.writeheader()
        for t in tasks:
            writer.writerow(task_to_dict(t))

    print("Task saved!")

def load_tasks() -> list[Task]:
    if not TASKS_PATH.exists():
        return []
    with open(TASKS_PATH, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        print("Task loaded!")
        return [dict_to_task(row) for row in reader]
