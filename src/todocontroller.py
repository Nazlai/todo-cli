from .todorepository import TodoRepository, Status


class TodoController:
    def __init__(self, repository: TodoRepository):
        self.repository = repository

    def add(self, payload: str) -> str:
        id = self.repository.add(payload)

        print(f"Task added successfully (ID: {id})")

    def update(self, id: str, description: str):
        self.repository.edit(id, description)

        print(f"Task updated successfully (ID: {id})")

    def delete(self, id: str):
        self.repository.remove(id)

        # fixme
        # currently prints message even if id is not found in storage
        print(f"Task deleted successfully (ID: {id})")

    def mark_todo(self, id: str):
        self.repository.edit_status(id, Status.TODO)

        print(f"Task updated successfully (ID: {id})")

    def mark_in_progress(self, id: str):
        self.repository.edit_status(id, Status.IN_PROGRESS)

        print(f"Task updated successfully (ID: {id})")

    def mark_done(self, id: str):
        self.repository.edit_status(id, Status.DONE)

        print(f"Task updated successfully (ID: {id})")

    def list(self, status: Status = None):
        print(self.repository.find_all(status))

    def getById(self, id: str):
        print(self.repository.find(id))
