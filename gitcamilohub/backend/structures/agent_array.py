"""Fixed-size array for execution agents."""

from backend.domain.entities.agent import Agent


class AgentArray:
    def __init__(self, agents: list[Agent]):
        self._agents = list(agents)
        self._size = len(self._agents)

    def get(self, index: int) -> Agent:
        if index < 0 or index >= self._size:
            raise IndexError("Agent index out of bounds")
        return self._agents[index]

    def find_free(self) -> Agent | None:
        for agent in self._agents:
            if agent.is_free():
                return agent
        return None

    def all(self) -> list[Agent]:
        return list(self._agents)

    def size(self) -> int:
        return self._size

    def to_list(self) -> list[dict]:
        return [agent.to_dict() for agent in self._agents]
