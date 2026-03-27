"""Simulates pipeline execution."""

import random

from backend.services.log_service import LogService
from backend.structures.pipeline_linked_list import PipelineLinkedList, PipelineNode


class PipelineSimulator:
    def __init__(self, random_generator: random.Random | None = None):
        self._random = random_generator or random.Random()

    def run(self, pipeline: PipelineLinkedList, log_service: LogService) -> tuple[bool, list[dict]]:
        pipeline.reset()
        current: PipelineNode | None = pipeline.head
        results: list[dict] = []
        overall_success = True

        while current is not None:
            stage = current.stage
            stage.mark_running()
            log_service.add(f"Ejecutando etapa: {stage.name}", "INFO", stage.name)
            duration = round(self._random.uniform(0.4, 3.0), 2)

            if self._random.random() < stage.fail_chance:
                stage.mark_failed(duration)
                log_service.add(f"{stage.name} fallo y detuvo el pipeline", "ERROR", stage.name)
                results.append(stage.to_dict())
                current = current.next
                while current is not None:
                    current.stage.mark_skipped()
                    results.append(current.stage.to_dict())
                    current = current.next
                overall_success = False
                break

            stage.mark_success(duration)
            log_service.add(f"{stage.name} completado en {duration}s", "SUCCESS", stage.name)
            results.append(stage.to_dict())
            current = current.next

        return overall_success, results
