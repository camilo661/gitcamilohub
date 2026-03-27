"""Log entry entity."""

from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class LogEntry:
    message: str
    level: str = "INFO"
    stage: str = ""
    timestamp: str = field(default_factory=lambda: datetime.now().strftime("%H:%M:%S.%f")[:-3])

    def to_dict(self) -> dict:
        return {
            "hora": self.timestamp,
            "nivel": self.level,
            "etapa": self.stage,
            "mensaje": self.message,
        }
