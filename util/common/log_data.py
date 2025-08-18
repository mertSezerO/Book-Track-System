from dataclasses import dataclass
from typing import Any


@dataclass
class LogData:
    message: str
    source: str
    level: str
    args: tuple[Any, ...] = ()
    kwargs: dict[str, Any] = None

    def __post_init__(self):
        if self.kwargs is None:
            self.kwargs = {}

    def format_message(self) -> str:
        return self.message.format(*(self.args), **(self.kwargs))