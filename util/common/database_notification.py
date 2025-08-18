from dataclasses import dataclass

@dataclass
class DBNotification:
    success: bool
    message: str
    result: object | None