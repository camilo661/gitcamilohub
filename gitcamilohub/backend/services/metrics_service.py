"""Read-only metrics service."""

from backend.services.deployment_service import DeploymentService
from backend.services.pipeline_service import PipelineService
from backend.structures.agent_array import AgentArray
from backend.structures.job_queue import JobQueue


class MetricsService:
    def __init__(
        self,
        agent_array: AgentArray,
        job_queue: JobQueue,
        deployment_service: DeploymentService,
        pipeline_service: PipelineService,
    ):
        self._agent_array = agent_array
        self._job_queue = job_queue
        self._deployment_service = deployment_service
        self._pipeline_service = pipeline_service

    def free_agent_count(self) -> int:
        return sum(1 for agent in self._agent_array.all() if agent.is_free())
