import datetime
from dataclasses import dataclass
from datetime import date, datetime

@dataclass
class Task:
    """Represents a task.

    Attributes:
        title (str): The task title.
        status (str): Status of the task ("Pending", "In Progress", "Finished").
        description (str): Description of the task.
        due_date (date): The date the task is due.
    """
    title: str = "No Title"
    status: str = "Pending"
    description: str = "No Description"
    due_date: date = datetime.today().date()


def task_to_dict(task: Task) -> dict:
    """Convert a Task object into a dictionary suitable for CSV storage.

    Args:
        task (Task): The Task to convert.

    Returns:
        dict: Dictionary representation of the Task.
    """
    return {
        "title": task.title,
        "status": task.status,
        "description": task.description,
        "due date": task.due_date.strftime('%Y-%m-%d')
    }


def dict_to_task(data: dict) -> Task:
    """Convert a dictionary into a Task object.

    Args:
        data (dict): Dictionary representation of a task.

    Returns:
        Task: Task object created from the dictionary.
    """
    return Task(
        title=data["title"],
        status=data["status"],
        description=data["description"],
        due_date=datetime.strptime(data["due date"], "%Y-%m-%d").date()
    )
