"""Root application state object."""

from backend.factories.agent_factory import AgentFactory
from backend.factories.job_factory import JobFactory
from backend.factories.pipeline_factory import PipelineFactory
from backend.services.deployment_service import DeploymentService
from backend.services.log_service import LogService
from backend.services.metrics_service import MetricsService
from backend.services.pipeline_service import PipelineService
from backend.services.pipeline_simulator import PipelineSimulator
from backend.structures.agent_array import AgentArray
from backend.structures.deployment_stack import DeploymentStack
from backend.structures.job_queue import JobQueue
from backend.structures.log_list import LogList


class ApplicationState:
    """Composes all application dependencies."""

    def __init__(self):
        self.agent_array = AgentArray(AgentFactory.create_default_agents())
        self.job_queue = JobQueue()
        self.deployment_stack = DeploymentStack()
        self.log_list = LogList()
        self.pipeline = PipelineFactory.create_default_pipeline()
        self.job_factory = JobFactory()
        self.log_service = LogService(self.log_list)
        self.deployment_service = DeploymentService(self.deployment_stack)
        self.pipeline_simulator = PipelineSimulator()
        self.pipeline_service = PipelineService(
            self.agent_array,
            self.job_queue,
            self.pipeline,
            self.deployment_service,
            self.log_service,
            self.pipeline_simulator,
        )
        self.metrics_service = MetricsService(
            self.agent_array,
            self.job_queue,
            self.deployment_service,
            self.pipeline_service,
        )
