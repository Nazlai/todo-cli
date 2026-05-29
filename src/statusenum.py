from enum import Enum


class Status(str, Enum):
    TODO: str = "TODO"
    IN_PROGRESS: str = "IN_PROGRESS"
    DONE: str = "DONE"
