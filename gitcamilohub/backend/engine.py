"""Facade layer used by Streamlit."""

from backend.application.state import ApplicationState


class EngineFacade:
    @staticmethod
    def create_state() -> ApplicationState:
        return ApplicationState()

    @staticmethod
    def enqueue_job(state: ApplicationState, repo: str, branch: str, developer: str) -> dict:
        return state.pipeline_service.enqueue_job(state.job_factory.create(repo, branch, developer))

    @staticmethod
    def run_next_job(state: ApplicationState) -> dict:
        return state.pipeline_service.run_next_job()

    @staticmethod
    def emergency_rollback(state: ApplicationState) -> dict:
        return state.pipeline_service.rollback()

    @staticmethod
    def get_agents(state: ApplicationState) -> list[dict]:
        return state.agent_array.to_list()

    @staticmethod
    def get_queue(state: ApplicationState) -> list[dict]:
        return state.job_queue.to_list()

    @staticmethod
    def get_queue_size(state: ApplicationState) -> int:
        return state.job_queue.size()

    @staticmethod
    def get_pipeline_stages(state: ApplicationState) -> list[dict]:
        return state.pipeline.to_list()

    @staticmethod
    def get_deploy_stack(state: ApplicationState) -> list[dict]:
        return state.deployment_service.history()

    @staticmethod
    def get_current_deployment(state: ApplicationState) -> dict | None:
        return state.deployment_service.current()

    @staticmethod
    def get_logs(state: ApplicationState, level: str = "", keyword: str = "") -> list[dict]:
        return state.log_service.get_logs(level, keyword)

    @staticmethod
    def get_history(state: ApplicationState) -> list[dict]:
        return state.pipeline_service.history()

    @staticmethod
    def clear_logs(state: ApplicationState) -> None:
        state.log_service.clear()

    @staticmethod
    def free_agent_count(state: ApplicationState) -> int:
        return state.metrics_service.free_agent_count()


create_state = EngineFacade.create_state
enqueue_job = EngineFacade.enqueue_job
run_next_job = EngineFacade.run_next_job
emergency_rollback = EngineFacade.emergency_rollback
get_agents = EngineFacade.get_agents
get_queue = EngineFacade.get_queue
get_queue_size = EngineFacade.get_queue_size
get_pipeline_stages = EngineFacade.get_pipeline_stages
get_deploy_stack = EngineFacade.get_deploy_stack
get_current_deployment = EngineFacade.get_current_deployment
get_logs = EngineFacade.get_logs
get_history = EngineFacade.get_history
clear_logs = EngineFacade.clear_logs
free_agent_count = EngineFacade.free_agent_count
