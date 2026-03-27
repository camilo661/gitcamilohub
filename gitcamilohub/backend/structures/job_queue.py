"""FIFO queue for jobs."""

from collections import deque

from backend.domain.entities.job import Job


class JobQueue:
    def __init__(self):
        self._jobs: deque[Job] = deque()

    def enqueue(self, job: Job) -> None:
        self._jobs.append(job)

    def dequeue(self) -> Job | None:
        return self._jobs.popleft() if self._jobs else None

    def is_empty(self) -> bool:
        return not self._jobs

    def size(self) -> int:
        return len(self._jobs)

    def to_list(self) -> list[dict]:
        return [job.to_dict() for job in self._jobs]
