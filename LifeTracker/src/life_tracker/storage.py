import csv
from pathlib import Path
from model import Task, task_to_dict, dict_to_task

# Path to the CSV file storing tasks
PATH = Path("../../data/tasks.csv")

def save_tasks(tasks: list[Task]):
    """
    Save a list of Task objects to a CSV file.

    Creates parent directories if they do not exist.

    Args:
        tasks (list[Task]): List of tasks to save.
    """
    # Ensure the parent directory exists
    PATH.parent.mkdir(parents=True, exist_ok=True)

    # Write tasks to CSV
    with open(PATH, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["title", "status"])
        writer.writeheader()
        for t in tasks:
            writer.writerow(task_to_dict(t))

def load_tasks() -> list[Task]:
    """
    Load tasks from the CSV file.

    Returns:
        list[Task]: List of Task objects. Returns empty list if file doesn't exist.
    """
    if not PATH.exists():
        return []

    with open(PATH, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return [dict_to_task(row) for row in reader]
