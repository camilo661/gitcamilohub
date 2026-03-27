"""Deployment and rollback service."""

import random

from backend.domain.entities.deployment import Deployment
from backend.structures.deployment_stack import DeploymentStack


class DeploymentService:
    def __init__(self, deployment_stack: DeploymentStack, random_generator: random.Random | None = None):
        self._deployment_stack = deployment_stack
        self._version_counter = 0
        self._random = random_generator or random.Random()

    def deploy(self, repository: str, agent_name: str) -> Deployment:
        self._version_counter += 1
        deployment = Deployment(
            f"v1.{self._version_counter}.0",
            repository,
            f"abc{self._random.randint(10000, 99999)}",
            agent_name,
        )
        self._deployment_stack.push(deployment)
        return deployment

    def rollback(self) -> tuple[Deployment | None, Deployment | None]:
        if self._deployment_stack.size() < 2:
            return None, None
        removed = self._deployment_stack.pop()
        return removed, self._deployment_stack.peek()

    def current(self) -> dict | None:
        deployment = self._deployment_stack.peek()
        return deployment.to_dict() if deployment else None

    def history(self) -> list[dict]:
        return self._deployment_stack.to_list()
