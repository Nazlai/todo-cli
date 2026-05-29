from enum import Enum
from datetime import datetime
from .storage import Storage


class Status(str, Enum):
    TODO: str = "TODO"
    IN_PROGRESS: str = "IN_PROGRESS"
    DONE: str = "DONE"


class Task:
    def __init__(self, description: str):
        now = datetime.now()
        self.description = description
        self.status = Status.TODO
        self.createdAt = now
        self.updatedAt = now


class TodoRepository:
    def __init__(self, storage: Storage):
        self.storage = storage

    def add(self, description: str) -> int:
        task = Task(description)
        id = self.storage.insert(task)

        return id

    def edit(self, id: str, description: str):
        return self.storage.update(id, {"description": description})

    def edit_status(self, id: str, status: Status):
        return self.storage.update(id, {"status": status})

    def remove(self, id: str):
        return self.storage.delete(id)

    def find_all(self, status: Status):
        tasks = self.storage.find_all()

        if not status:
            return tasks

        result = filter(lambda x: x[1]["status"] == status, tasks.items())

        return dict(result)

    def find(self, id: str):
        task = self.storage.find(id)

        if task:
            return task

        return None
