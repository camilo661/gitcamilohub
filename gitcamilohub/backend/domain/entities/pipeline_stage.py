"""Pipeline stage entity."""

from dataclasses import dataclass


@dataclass
class PipelineStage:
    name: str
    description: str
    fail_chance: float = 0.10
    status: str = "pendiente"
    duration: float = 0.0

    def reset(self) -> None:
        self.status = "pendiente"
        self.duration = 0.0

    def mark_running(self) -> None:
        self.status = "ejecutando"

    def mark_success(self, duration: float) -> None:
        self.status = "exitoso"
        self.duration = duration

    def mark_failed(self, duration: float) -> None:
        self.status = "fallido"
        self.duration = duration

    def mark_skipped(self) -> None:
        self.status = "omitido"

    def to_dict(self) -> dict:
        return {
            "nombre": self.name,
            "descripcion": self.description,
            "estado": self.status,
            "duracion": self.duration,
        }
