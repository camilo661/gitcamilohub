"""Compatibility exports for the modularized data structures."""

from backend.domain.entities.agent import Agent
from backend.domain.entities.deployment import Deployment
from backend.domain.entities.job import Job
from backend.domain.entities.log_entry import LogEntry
from backend.domain.entities.pipeline_stage import PipelineStage
from backend.factories.pipeline_factory import PipelineFactory
from backend.structures.agent_array import AgentArray
from backend.structures.deployment_stack import DeploymentStack
from backend.structures.job_queue import JobQueue
from backend.structures.log_list import LogList
from backend.structures.pipeline_linked_list import PipelineLinkedList


def build_default_pipeline() -> PipelineLinkedList:
    return PipelineFactory.create_default_pipeline()


__all__ = [
    "Agent",
    "Deployment",
    "Job",
    "LogEntry",
    "PipelineStage",
    "AgentArray",
    "DeploymentStack",
    "JobQueue",
    "LogList",
    "PipelineLinkedList",
    "build_default_pipeline",
]
