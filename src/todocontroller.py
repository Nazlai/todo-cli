from .todorepository import TodoRepository
from .logresultdecorator import log_result
from .exceptiondecorator import log_exception
from .logalldecorator import log_all_items
from .statusenum import Status


class TodoController:
    def __init__(self, repository: TodoRepository):
        self.repository = repository

    @log_result
    def add(self, payload: str):
        return self.repository.add(payload)

    @log_exception
    @log_result
    def update(self, id: str, description: str):
        return self.repository.edit(id, description)

    @log_exception
    @log_result
    def delete(self, id: str):
        return self.repository.remove(id)

    @log_exception
    @log_result
    def mark_todo(self, id: str):
        return self.repository.edit_status(id, Status.TODO)

    @log_exception
    @log_result
    def mark_in_progress(self, id: str):
        return self.repository.edit_status(id, Status.IN_PROGRESS)

    @log_exception
    @log_result
    def mark_done(self, id: str):
        return self.repository.edit_status(id, Status.DONE)

    @log_exception
    @log_all_items
    def list(self, status: Status = None):
        return self.repository.find_all(status)

    @log_exception
    @log_result
    def get_by_id(self, id: str):
        return self.repository.find(id)
