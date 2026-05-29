from datetime import datetime
from .storage import Storage
from .statusenum import Status


class Task:
    def __init__(self, description: str):
        now = datetime.now()
        self.description = description
        self.status = Status.TODO
        self.createdAt = now
        self.updatedAt = now


# fixme
# actions should return a type
# but Task doesnt have an id while values returned from storage does have an id
# consider extracting Task from repository so controller could reuse the same interface?


class TodoRepository:
    def __init__(self, storage: Storage):
        self.storage = storage

    def add(self, description: str):
        task = Task(description)

        return self.storage.insert(task)

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
