"""Job entity."""

from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Job:
    identifier: str
    repository: str
    branch: str
    developer: str
    submitted_at: str = field(default_factory=lambda: datetime.now().strftime("%H:%M:%S"))
    status: str = "en espera"

    def mark_running(self) -> None:
        self.status = "ejecutando"

    def mark_completed(self, success: bool) -> None:
        self.status = "completado" if success else "fallido"

    def to_dict(self) -> dict:
        return {
            "id": self.identifier,
            "repositorio": self.repository,
            "rama": self.branch,
            "desarrollador": self.developer,
            "enviado": self.submitted_at,
            "estado": self.status,
        }
