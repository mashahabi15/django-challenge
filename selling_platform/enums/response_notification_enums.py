from enum import Enum, unique


@unique
class ResponseNotificationType(Enum):
    success = "success"
    warning = "warning"
    error = "error"
