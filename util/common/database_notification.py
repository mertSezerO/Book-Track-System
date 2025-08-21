from dataclasses import dataclass

@dataclass
class DBNotification:
    success: bool
    message: str
    resource: object = None