"""Job factory with consecutive identifiers."""

from backend.domain.entities.job import Job


class JobFactory:
    def __init__(self):
        self._counter = 0

    def create(self, repository: str, branch: str, developer: str) -> Job:
        self._counter += 1
        return Job(f"JOB-{self._counter:04d}", repository, branch, developer)
