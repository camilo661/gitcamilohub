"""Pipeline factory."""

from backend.domain.entities.pipeline_stage import PipelineStage
from backend.structures.pipeline_linked_list import PipelineLinkedList


class PipelineFactory:
    DEFAULT_STAGES = [
        ("Checkout", "Clonar repositorio y obtener codigo fuente", 0.05),
        ("Instalar Dependencias", "Instalar paquetes necesarios", 0.08),
        ("Linter", "Analisis estatico del codigo", 0.10),
        ("Pruebas Unitarias", "Ejecucion automatica de pruebas", 0.12),
        ("Build", "Compilacion y empaquetado de artefactos", 0.08),
        ("Despliegue", "Publicacion automatizada en produccion", 0.05),
    ]

    @classmethod
    def create_default_pipeline(cls) -> PipelineLinkedList:
        pipeline = PipelineLinkedList()
        for name, description, fail_chance in cls.DEFAULT_STAGES:
            pipeline.append(PipelineStage(name, description, fail_chance))
        return pipeline
