"""Singly linked list for pipeline stages."""

from backend.domain.entities.pipeline_stage import PipelineStage


class PipelineNode:
    def __init__(self, stage: PipelineStage):
        self.stage = stage
        self.next: "PipelineNode | None" = None


class PipelineLinkedList:
    def __init__(self):
        self.head: PipelineNode | None = None
        self._count = 0

    def append(self, stage: PipelineStage) -> None:
        node = PipelineNode(stage)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node
        self._count += 1

    def reset(self) -> None:
        current = self.head
        while current is not None:
            current.stage.reset()
            current = current.next

    def to_list(self) -> list[dict]:
        items: list[dict] = []
        current = self.head
        while current is not None:
            items.append(current.stage.to_dict())
            current = current.next
        return items
