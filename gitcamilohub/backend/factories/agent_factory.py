"""Agent factory."""

from backend.domain.entities.agent import Agent


class AgentFactory:
    DEFAULT_AGENTS = [
        (1, "Agente-Ubuntu", "Ubuntu 22.04 LTS"),
        (2, "Agente-Windows", "Windows Server 2022"),
        (3, "Agente-macOS", "macOS Ventura 13"),
        (4, "Agente-Alpine", "Alpine Linux 3.19"),
    ]

    @classmethod
    def create_default_agents(cls) -> list[Agent]:
        return [Agent(*agent_data) for agent_data in cls.DEFAULT_AGENTS]
