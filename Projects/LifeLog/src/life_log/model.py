import datetime
from dataclasses import dataclass
from datetime import date, datetime

@dataclass
class Task:
    """
    Represents a Task

    Attributes:
        title (str): The Task title
        status (str): Status of the Task (In Progress, Pending, Finished)
        description (str): Description of the task
        due_date (date): The Date the task is due
    """
    title: str = "No Title"
    status: str = "Pending"
    description: str = "No Description"
    due_date: date = datetime.today().date()

def task_to_dict(task: Task) -> dict:
    """
    Turns a Task into a dictionary

    Args:
        task (Task): the Task you want to convert

    Returns:
        dict: the dict from the Task
    """
    return {"title": task.title,
            "status": task.status,
            "description": task.description,
            "due date": task.due_date.strftime('%Y-%m-%d')}

def dict_to_task(data: dict) -> Task:
    """
    Turns a dictionary into a Task object

    Args:
        dict: the dict from the Task

    Returns:
        task (Task): the Task you want to convert
    """
    return Task(title=data["title"],
                status=data["status"],
                description=data["description"],
                due_date=datetime.strptime(data["due date"], "%Y-%m-%d").date())

