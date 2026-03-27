"""Dashboard renderer."""

import streamlit as st

from backend.engine import EngineFacade
from frontend.components import render_console, render_kpi, render_panel_header, render_pipeline_flow


class DashboardRenderer:
    def __init__(self, engine_state):
        self._engine_state = engine_state

    def render(self):
        self._render_header()
        self._render_kpis()
        self._render_workspace_row()
        self._render_pipeline()
        self._render_activity_row()
        self._render_logs()
        self._render_footer()

    def _render_header(self):
        agents = EngineFacade.get_agents(self._engine_state)
        queue = EngineFacade.get_queue(self._engine_state)
        deployment = EngineFacade.get_current_deployment(self._engine_state)
        deployment_label = deployment["version"] if deployment else "Sin despliegue"
        st.markdown(
            '<div class="hero">'
            '<span class="hero-kicker">Git Workflow Simulator</span>'
            '<div class="brand">GitCamiloHub</div>'
            '<div class="brand-sub">Simulador CI/CD con arquitectura modular orientada a objetos. '
            'Gestiona cola, agentes, pipeline, despliegues y logs en una interfaz inspirada en herramientas tipo GitHub.</div>'
            '<div class="hero-grid">'
            f'<div class="hero-stat"><span class="hero-stat-label">Agentes registrados</span><span class="hero-stat-value">{len(agents)}</span></div>'
            f'<div class="hero-stat"><span class="hero-stat-label">Jobs en espera</span><span class="hero-stat-value">{len(queue)}</span></div>'
            f'<div class="hero-stat"><span class="hero-stat-label">Version activa</span><span class="hero-stat-value">{deployment_label}</span></div>'
            "</div>"
            "</div>",
            unsafe_allow_html=True,
        )

    def _render_kpis(self):
        agents = EngineFacade.get_agents(self._engine_state)
        queue_size = EngineFacade.get_queue_size(self._engine_state)
        current_deployment = EngineFacade.get_current_deployment(self._engine_state)
        history = EngineFacade.get_history(self._engine_state)
        success_count = sum(1 for item in history if item["exito"])
        total_count = len(history)
        cols = st.columns(5)
        render_kpi(cols[0], f'{EngineFacade.free_agent_count(self._engine_state)}/{len(agents)}', "Agentes libres", "#8ddb9a")
        render_kpi(cols[1], queue_size, "Jobs en cola", "#f2cc60" if queue_size else "#8b949e")
        render_kpi(cols[2], current_deployment["version"] if current_deployment else "-", "Version activa", "#b392f0")
        render_kpi(cols[3], success_count, "Pipelines exitosos", "#8ddb9a")
        render_kpi(cols[4], total_count - success_count, "Pipelines fallidos", "#ff938f" if total_count - success_count else "#8b949e")
        st.markdown("<div style='height:0.35rem;'></div>", unsafe_allow_html=True)

    def _render_workspace_row(self):
        left, right = st.columns(2)
        with left:
            st.markdown('<div class="panel-card">', unsafe_allow_html=True)
            render_panel_header("Agentes de ejecucion", "Array fijo de nodos disponibles para procesar jobs.")
            for agent in EngineFacade.get_agents(self._engine_state):
                css_class = "agent-free" if agent["estado"] == "disponible" else "agent-busy"
                status_class = "status-free" if agent["estado"] == "disponible" else "status-busy"
                job_text = (
                    f'<div class="meta-line">Job actual: <code>{agent["trabajo"]}</code></div>'
                    if agent["trabajo"]
                    else '<div class="meta-line">Sin trabajo asignado</div>'
                )
                st.markdown(
                    f'<div class="agent-card {css_class}">'
                    f'<div><strong>{agent["nombre"]}</strong></div>'
                    f'<div class="meta-line">{agent["sistema"]}</div>'
                    f'<div style="margin-top:0.6rem;"><span class="status-badge {status_class}">{agent["estado"].upper()}</span></div>'
                    f'{job_text}'
                    f"</div>",
                    unsafe_allow_html=True,
                )
            st.markdown("</div>", unsafe_allow_html=True)

        with right:
            st.markdown('<div class="panel-card">', unsafe_allow_html=True)
            render_panel_header("Cola de jobs", "Orden FIFO de pushes pendientes por procesar.")
            queue_items = EngineFacade.get_queue(self._engine_state)
            if not queue_items:
                st.info("La cola esta vacia. Puedes encolar un nuevo job desde la barra lateral.")
            for index, job in enumerate(queue_items):
                css_class = "next-job" if index == 0 else "waiting-job"
                label = "Siguiente" if index == 0 else f"Posicion {index + 1}"
                st.markdown(
                    f'<div class="queue-card {css_class}">'
                    f'<div><strong>{job["repositorio"]}</strong> <code>{job["id"]}</code></div>'
                    f'<div class="meta-line">Rama: <strong>{job["rama"]}</strong> | Estado: {job["estado"]}</div>'
                    f'<div class="meta-line">{label} | Dev: {job["desarrollador"]} | Hora: {job["enviado"]}</div>'
                    f"</div>",
                    unsafe_allow_html=True,
                )
            st.markdown("</div>", unsafe_allow_html=True)

    def _render_pipeline(self):
        st.markdown('<div class="panel-card">', unsafe_allow_html=True)
        render_panel_header("Pipeline visual", "Lista enlazada simple con avance secuencial por etapa.")
        stages = EngineFacade.get_pipeline_stages(self._engine_state)
        render_pipeline_flow(stages)
        with st.expander("Ver detalle de etapas"):
            columns = st.columns(3)
            for index, stage in enumerate(stages):
                duration = f' | {stage["duracion"]}s' if stage["duracion"] > 0 else ""
                columns[index % 3].markdown(
                    f'**{stage["nombre"]}**  \n_{stage["descripcion"]}_  \n`{stage["estado"]}`{duration}'
                )
        st.markdown("</div>", unsafe_allow_html=True)

    def _render_activity_row(self):
        left, right = st.columns(2)
        with left:
            st.markdown('<div class="panel-card">', unsafe_allow_html=True)
            render_panel_header("Stack de despliegues", "Pila LIFO para versionado y rollback.")
            items = EngineFacade.get_deploy_stack(self._engine_state)
            if not items:
                st.info("Aun no hay despliegues en el stack.")
            for index, deployment in enumerate(items):
                css_class = "stack-top" if index == 0 else "stack-rest"
                label = "Produccion" if index == 0 else f"Historial {index + 1}"
                st.markdown(
                    f'<div class="stack-card {css_class}">'
                    f'<div><strong>{deployment["version"]}</strong></div>'
                    f'<div class="meta-line">{label} | Repo: {deployment["repositorio"]}</div>'
                    f'<div class="meta-line">Commit: <code>{deployment["commit"]}</code> | Agente: {deployment["agente"]}</div>'
                    f'<div class="meta-line">Fecha: {deployment["desplegado"]}</div>'
                    f"</div>",
                    unsafe_allow_html=True,
                )
            st.markdown("</div>", unsafe_allow_html=True)

        with right:
            st.markdown('<div class="panel-card">', unsafe_allow_html=True)
            render_panel_header("Historial de ejecuciones", "Resultado consolidado de pipelines procesados.")
            items = EngineFacade.get_history(self._engine_state)
            if not items:
                st.info("Aun no se ha ejecutado ningun pipeline.")
            for execution in items[:10]:
                job = execution["job"]
                version = execution["despliegue"]["version"] if execution["despliegue"] else "Sin despliegue"
                color = "#8ddb9a" if execution["exito"] else "#ff938f"
                status = "Exitoso" if execution["exito"] else "Fallido"
                st.markdown(
                    f'<div class="history-card" style="border-left:4px solid {color};">'
                    f'<div><strong>{job["repositorio"]}</strong> <code>{job["id"]}</code></div>'
                    f'<div class="meta-line">Rama: {job["rama"]} | Dev: {job["desarrollador"]}</div>'
                    f'<div class="meta-line">Resultado: {status} | Version: {version}</div>'
                    f"</div>",
                    unsafe_allow_html=True,
                )
            st.markdown("</div>", unsafe_allow_html=True)

    def _render_logs(self):
        st.markdown('<div class="panel-card">', unsafe_allow_html=True)
        render_panel_header("Consola de logs", "Trazabilidad del flujo con filtros por nivel y busqueda textual.")
        filter_col, search_col = st.columns([1, 2])
        with filter_col:
            level = st.selectbox("Filtrar por nivel", ["TODOS", "INFO", "SUCCESS", "WARNING", "ERROR"])
        with search_col:
            keyword = st.text_input("Buscar en logs", placeholder="Escribe para filtrar...")
        logs = EngineFacade.get_logs(self._engine_state, level, keyword)
        render_console(logs)
        if logs:
            total_logs = len(EngineFacade.get_logs(self._engine_state))
            st.caption(f"Mostrando {len(logs)} de {total_logs} entradas registradas")
        st.markdown("</div>", unsafe_allow_html=True)

    def _render_footer(self):
        st.markdown(
            '<div class="footer-note">GitCamiloHub | interfaz inspirada en plataformas de desarrollo colaborativo | 2026</div>',
            unsafe_allow_html=True,
        )
