from .todorepository import TodoRepository, Status
from .logactiondecorator import log_action_decorator
from .logresultdecorator import log_result_decorator
from .exceptiondecorator import exception_decorator


class TodoController:
    def __init__(self, repository: TodoRepository):
        self.repository = repository

    @log_result_decorator
    @log_action_decorator("add")
    def add(self, payload: str):
        return self.repository.add(payload)

    @exception_decorator
    @log_result_decorator
    @log_action_decorator("update")
    def update(self, id: str, description: str):
        return self.repository.edit(id, description)

    @exception_decorator
    @log_result_decorator
    @log_action_decorator("delete")
    def delete(self, id: str):
        return self.repository.remove(id)

    @exception_decorator
    @log_result_decorator
    @log_action_decorator("mark todo")
    def mark_todo(self, id: str):
        return self.repository.edit_status(id, Status.TODO)

    @exception_decorator
    @log_result_decorator
    @log_action_decorator("mark in progress")
    def mark_in_progress(self, id: str):
        return self.repository.edit_status(id, Status.IN_PROGRESS)

    @exception_decorator
    @log_result_decorator
    @log_action_decorator("mark done")
    def mark_done(self, id: str):
        return self.repository.edit_status(id, Status.DONE)

    @exception_decorator
    @log_result_decorator
    def list(self, status: Status = None):
        return self.repository.find_all(status)

    @exception_decorator
    @log_result_decorator
    @log_action_decorator("get by id")
    def getById(self, id: str):
        return self.repository.find(id)
