import logging

from .common import LogData

class Logger:
    

    def __init__(self):
        self.__loggers: dict[str, logging.Logger] = {}
        self.__create_logger("controller", "logs/logs_controller.log", logging.INFO)
        self.__create_logger("view", "logs/logs_view.log", logging.DEBUG)

    def __create_logger(self, name: str, file: str, level: int):
        logger = logging.getLogger(name)
        logger.setLevel(level)
        formatter = logging.Formatter(
            "%(asctime)s %(levelname)s: %(message)s", "%Y-%m-%d %H:%M:%S"
        )

        handler = logging.FileHandler(filename=file, encoding="utf-8")
        handler.setFormatter(formatter)
        handler.setLevel(level)

        logger.addHandler(handler)
        logger.propagate = False
        self.__loggers[name] = logger

    def __check_logger_exist(self, name: str) -> logging.Logger:
        if name not in self.__loggers:
            raise ValueError(f"Logger '{name}' not initialized. Call Logger.setup() first.")

    def get_logger(self, name: str) -> logging.Logger:
        self.__check_logger_exist(name)
        return self.__loggers[name]
    
    def log(self, log_data: LogData):
        self.__check_logger_exist(log_data.source)
        log_method = getattr(self.__loggers[log_data.source], log_data.level.lower(), None)
        if not log_method:
            raise AttributeError(f"Invalid log level: {log_data.level}")
        
        log_method(log_data.format_message())
