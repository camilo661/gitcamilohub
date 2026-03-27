"""Reusable Streamlit components."""

import streamlit as st

from frontend.styles import LOG_ICON, STAGE_CSS, STAGE_ICON


def render_kpi(column, value, label, color="#FFFFFF"):
    column.markdown(
        f'<div class="kpi-box">'
        f'<div class="kpi-lbl">{label}</div>'
        f'<div class="kpi-val" style="color:{color};">{value}</div>'
        f"</div>",
        unsafe_allow_html=True,
    )


def render_panel_header(title: str, caption: str):
    st.markdown(
        f'<div class="section-title">{title}</div>'
        f'<div class="section-caption">{caption}</div>',
        unsafe_allow_html=True,
    )


def render_pipeline_flow(stages: list[dict]):
    html = '<div class="flow-wrap">'
    for index, stage in enumerate(stages):
        css_class = STAGE_CSS.get(stage["estado"], "s-pendiente")
        icon = STAGE_ICON.get(stage["estado"], "")
        duration = f' {stage["duracion"]}s' if stage["duracion"] > 0 else ""
        html += f'<span class="stage-pill {css_class}">{icon} {stage["nombre"]}{duration}</span>'
        if index < len(stages) - 1:
            html += '<span class="stage-arrow">-></span>'
    html += "</div>"
    st.markdown(html, unsafe_allow_html=True)


def render_console(logs: list[dict]):
    if not logs:
        st.markdown(
            '<div class="console"><span style="color:#6e7681;">[ consola vacia - ejecuta un job ]</span></div>',
            unsafe_allow_html=True,
        )
        return

    html = '<div class="console">'
    for entry in logs:
        css_class = f'l-{entry["nivel"]}'
        icon = LOG_ICON.get(entry["nivel"], ".")
        stage = f'<span style="color:#6e7681;">[{entry["etapa"]}]</span> ' if entry["etapa"] else ""
        html += (
            f'<div class="{css_class}">'
            f'<span style="color:#6e7681;">{entry["hora"]}</span> '
            f'{icon} {stage}{entry["mensaje"]}</div>'
        )
    html += "</div>"
    st.markdown(html, unsafe_allow_html=True)
