"""Append-only list for logs."""

from backend.domain.entities.log_entry import LogEntry


class LogList:
    def __init__(self):
        self._entries: list[LogEntry] = []

    def append(self, entry: LogEntry) -> None:
        self._entries.append(entry)

    def clear(self) -> None:
        self._entries.clear()

    def count(self) -> int:
        return len(self._entries)

    def all(self) -> list[dict]:
        return [entry.to_dict() for entry in self._entries]

    def filter_by_level(self, level: str) -> list[dict]:
        return [entry.to_dict() for entry in self._entries if entry.level == level]

    def search(self, keyword: str) -> list[dict]:
        value = keyword.lower()
        return [entry.to_dict() for entry in self._entries if value in entry.message.lower()]
