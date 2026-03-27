"""Agent entity."""

from dataclasses import dataclass


@dataclass
class Agent:
    identifier: int
    name: str
    operating_system: str
    status: str = "disponible"
    current_job: str | None = None

    def assign(self, job_id: str) -> None:
        self.status = "ocupado"
        self.current_job = job_id

    def release(self) -> None:
        self.status = "disponible"
        self.current_job = None

    def is_free(self) -> bool:
        return self.status == "disponible"

    def to_dict(self) -> dict:
        return {
            "id": self.identifier,
            "nombre": self.name,
            "sistema": self.operating_system,
            "estado": self.status,
            "trabajo": self.current_job,
        }
