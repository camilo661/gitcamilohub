"""Sidebar controls."""

import streamlit as st

from backend.config import CatalogSingleton
from backend.engine import EngineFacade


class SidebarController:
    def __init__(self, engine_state):
        self._engine_state = engine_state
        self._catalog = CatalogSingleton()

    def render(self):
        with st.sidebar:
            st.markdown(
                '<div class="sidebar-shell">'
                '<div class="sidebar-brand">'
                '<h2>GitCamiloHub</h2>'
                '<p>Controla jobs, agentes y despliegues desde una vista inspirada en plataformas de desarrollo modernas.</p>'
                '</div>'
                '</div>',
                unsafe_allow_html=True,
            )
            st.divider()
            self._render_enqueue()
            st.divider()
            self._render_execute()
            st.divider()
            self._render_rollback()
            st.divider()
            self._render_reset()

    def _render_enqueue(self):
        st.markdown("### Nuevo Job")
        repo = st.selectbox("Repositorio", self._catalog.repositories, key="repo_sel")
        branch = st.selectbox("Rama", self._catalog.branches, key="branch_sel")
        developer = st.text_input("Desarrollador", value="camilo", key="dev_sel")
        if st.button("Encolar job", use_container_width=True):
            job = EngineFacade.enqueue_job(self._engine_state, repo, branch, developer)
            st.success(f'{job["id"]} listo en la cola')
            st.rerun()

    def _render_execute(self):
        st.markdown("### Ejecutar Pipeline")
        st.caption("Procesa el siguiente job disponible y actualiza el stack de despliegue.")
        if st.button("Ejecutar siguiente job", use_container_width=True, type="primary"):
            result = EngineFacade.run_next_job(self._engine_state)
            if result["ok"]:
                pipeline_result = result["resultado"]
                if pipeline_result["exito"]:
                    st.success(f'Pipeline completado: {pipeline_result["despliegue"]["version"]}')
                else:
                    st.error("El pipeline fallo. Revisa la consola de logs.")
            else:
                st.warning(result["mensaje"])
            st.rerun()

    def _render_rollback(self):
        st.markdown("### Rollback")
        st.caption("Revierte la ultima version desplegada y restaura la anterior.")
        if st.button("Ejecutar rollback", use_container_width=True):
            rollback = EngineFacade.emergency_rollback(self._engine_state)
            if rollback["ok"]:
                st.warning(
                    f'Revertida: {rollback["version_removida"]["version"]} | '
                    f'Restaurada: {rollback["version_restaurada"]["version"]}'
                )
            else:
                st.error(rollback["mensaje"])
            st.rerun()

    def _render_reset(self):
        st.markdown("### Mantenimiento")
        left, right = st.columns(2)
        if left.button("Limpiar logs", use_container_width=True):
            EngineFacade.clear_logs(self._engine_state)
            st.rerun()
        if right.button("Reset total", use_container_width=True):
            st.session_state["engine"] = EngineFacade.create_state()
            st.rerun()
