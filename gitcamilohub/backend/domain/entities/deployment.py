"""Deployment entity."""

from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Deployment:
    version: str
    repository: str
    commit_hash: str
    agent_name: str
    deployed_at: str = field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    def to_dict(self) -> dict:
        return {
            "version": self.version,
            "repositorio": self.repository,
            "commit": self.commit_hash,
            "agente": self.agent_name,
            "desplegado": self.deployed_at,
        }
