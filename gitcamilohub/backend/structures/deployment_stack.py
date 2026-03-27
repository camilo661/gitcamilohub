"""LIFO stack for deployments."""

from backend.domain.entities.deployment import Deployment


class DeploymentStack:
    def __init__(self):
        self._deployments: list[Deployment] = []

    def push(self, deployment: Deployment) -> None:
        self._deployments.append(deployment)

    def pop(self) -> Deployment | None:
        return self._deployments.pop() if self._deployments else None

    def peek(self) -> Deployment | None:
        return self._deployments[-1] if self._deployments else None

    def size(self) -> int:
        return len(self._deployments)

    def to_list(self) -> list[dict]:
        return [deployment.to_dict() for deployment in reversed(self._deployments)]
