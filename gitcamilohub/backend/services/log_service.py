"""Log service."""

from backend.domain.entities.log_entry import LogEntry
from backend.structures.log_list import LogList


class LogService:
    def __init__(self, log_list: LogList):
        self._log_list = log_list

    def add(self, message: str, level: str = "INFO", stage: str = "") -> None:
        self._log_list.append(LogEntry(message, level, stage))

    def clear(self) -> None:
        self._log_list.clear()

    def get_logs(self, level: str = "", keyword: str = "") -> list[dict]:
        if keyword.strip():
            return self._log_list.search(keyword)
        if level and level != "TODOS":
            return self._log_list.filter_by_level(level)
        return self._log_list.all()
