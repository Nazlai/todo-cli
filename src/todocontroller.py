from .todorepository import TodoRepository, Status
from .logactiondecorator import log_action_decorator
from .logresultdecorator import log_result_decorator


class TodoController:
    def __init__(self, repository: TodoRepository):
        self.repository = repository

    @log_result_decorator
    @log_action_decorator("add")
    def add(self, payload: str):
        return self.repository.add(payload)

    @log_result_decorator
    @log_action_decorator("update")
    def update(self, id: str, description: str):
        return self.repository.edit(id, description)

    @log_result_decorator
    @log_action_decorator("delete")
    def delete(self, id: str):
        return self.repository.remove(id)

    @log_result_decorator
    @log_action_decorator("mark todo")
    def mark_todo(self, id: str):
        return self.repository.edit_status(id, Status.TODO)

    @log_result_decorator
    @log_action_decorator("mark in progress")
    def mark_in_progress(self, id: str):
        return self.repository.edit_status(id, Status.IN_PROGRESS)

    @log_result_decorator
    @log_action_decorator("mark done")
    def mark_done(self, id: str):
        return self.repository.edit_status(id, Status.DONE)

    @log_result_decorator
    def list(self, status: Status = None):
        return self.repository.find_all(status)

    @log_result_decorator
    @log_action_decorator("get by id")
    def getById(self, id: str):
        return self.repository.find(id)
