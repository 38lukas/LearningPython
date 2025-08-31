from dataclasses import dataclass

@dataclass
class Task:
    """
    Data model representing a single task.

    Attributes:
        title (str): The task description.
        status (str): Either 'pending' or 'done'. Default is 'pending'.
    """
    title: str
    status: str = "pending"

def task_to_dict(task: Task) -> dict:
    """
    Convert a Task object to a dictionary for storage.

    Args:
        task (Task): The task to convert.

    Returns:
        dict: Dictionary with 'title' and 'status' keys.
    """
    return {"title": task.title, "status": task.status}

def dict_to_task(data: dict) -> Task:
    """
    Convert a dictionary to a Task object.

    Args:
        data (dict): Dictionary containing 'title' and 'status'.

    Returns:
        Task: Corresponding Task object.
    """
    return Task(title=data["title"], status=data["status"])
