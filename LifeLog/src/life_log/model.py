from dataclasses import dataclass

@dataclass
class Task:
    title: str
    status: str = "pending"
    description: str = "No Description"

def task_to_dict(task: Task) -> dict:
    return {"title": task.title, "status": task.status, "description": task.description}

def dict_to_task(data: dict) -> Task:
    return Task(title=data["title"], status=data["status"], description=data["description"])
