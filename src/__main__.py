import sys
from .todocontroller import TodoController
from .todorepository import TodoRepository
from .storage import Storage

commands = {
    "add",
    "update",
    "delete",
    "mark_todo",
    "mark_in_progress",
    "mark_done",
    "list",
    "getById",
}


def main():
    storage = Storage("my_db")
    todoRepository = TodoRepository(storage)
    todoController = TodoController(todoRepository)

    argumentLength = len(sys.argv)

    if argumentLength == 1:
        print("not enough arguments, consult py-todo --help for list of commands")
        return

    if sys.argv[1] == "--help":
        print(help(todoController))
        return

    command = sys.argv[1]

    if command in commands:
        method = getattr(todoController, command)
        method(*sys.argv[2:])

    if command not in commands:
        print("did you mean one of the following command?")

        for i in commands:
            print(i)


if __name__ == "__main__":
    main()
