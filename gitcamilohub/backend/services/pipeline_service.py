"""Coordinates queue, agents and pipeline execution."""

from backend.domain.entities.job import Job
from backend.services.deployment_service import DeploymentService
from backend.services.log_service import LogService
from backend.services.pipeline_simulator import PipelineSimulator
from backend.structures.agent_array import AgentArray
from backend.structures.job_queue import JobQueue
from backend.structures.pipeline_linked_list import PipelineLinkedList


class PipelineService:
    def __init__(
        self,
        agent_array: AgentArray,
        job_queue: JobQueue,
        pipeline: PipelineLinkedList,
        deployment_service: DeploymentService,
        log_service: LogService,
        pipeline_simulator: PipelineSimulator,
    ):
        self._agent_array = agent_array
        self._job_queue = job_queue
        self._pipeline = pipeline
        self._deployment_service = deployment_service
        self._log_service = log_service
        self._pipeline_simulator = pipeline_simulator
        self._history: list[dict] = []

    def enqueue_job(self, job: Job) -> dict:
        self._job_queue.enqueue(job)
        self._log_service.add(
            f"{job.identifier} en cola - {job.developer} hizo push a {job.repository}:{job.branch}",
            "INFO",
            "Cola",
        )
        return job.to_dict()

    def run_next_job(self) -> dict:
        if self._job_queue.is_empty():
            return {"ok": False, "mensaje": "La cola esta vacia - encola un job primero."}

        agent = self._agent_array.find_free()
        if agent is None:
            return {"ok": False, "mensaje": "Todos los agentes estan ocupados."}

        job = self._job_queue.dequeue()
        if job is None:
            return {"ok": False, "mensaje": "No hay jobs disponibles para ejecutar."}

        job.mark_running()
        agent.assign(job.identifier)
        self._log_service.add(
            f"Iniciando {job.identifier} en {agent.name} ({agent.operating_system})",
            "INFO",
            "Motor",
        )
        success, stage_results = self._pipeline_simulator.run(self._pipeline, self._log_service)
        agent.release()
        job.mark_completed(success)

        result = {
            "job": job.to_dict(),
            "agente": agent.to_dict(),
            "etapas": stage_results,
            "exito": success,
            "despliegue": None,
        }

        if success:
            deployment = self._deployment_service.deploy(job.repository, agent.name)
            self._log_service.add(
                f"{deployment.version} desplegada en produccion desde {agent.name}",
                "SUCCESS",
                "Despliegue",
            )
            result["despliegue"] = deployment.to_dict()
        else:
            self._log_service.add(
                f"{job.identifier} fallo - sin despliegue a produccion",
                "ERROR",
                "Motor",
            )

        self._history.append(result)
        return {"ok": True, "resultado": result}

    def rollback(self) -> dict:
        removed, restored = self._deployment_service.rollback()
        if removed is None or restored is None:
            return {"ok": False, "mensaje": "Se necesitan al menos 2 versiones en el stack para hacer rollback."}
        self._log_service.add(
            f"Rollback de emergencia: {removed.version} revertida -> {restored.version} restaurada",
            "WARNING",
            "Rollback",
        )
        return {
            "ok": True,
            "version_removida": removed.to_dict(),
            "version_restaurada": restored.to_dict(),
        }

    def history(self) -> list[dict]:
        return list(reversed(self._history))
