"""Centralized CSS and UI dictionaries."""

STAGE_CSS = {
    "pendiente": "s-pendiente",
    "ejecutando": "s-ejecutando",
    "exitoso": "s-exitoso",
    "fallido": "s-fallido",
    "omitido": "s-omitido",
}

STAGE_ICON = {
    "pendiente": "WAIT",
    "ejecutando": "RUN",
    "exitoso": "OK",
    "fallido": "ERR",
    "omitido": "SKIP",
}

LOG_ICON = {"INFO": "INFO", "SUCCESS": "OK", "WARNING": "WARN", "ERROR": "ERR"}

GLOBAL_CSS = """
<style>
:root {
    --bg-main: #0d1117;
    --bg-panel: #161b22;
    --bg-elevated: #1f2630;
    --bg-soft: #0f141b;
    --border: #30363d;
    --text-main: #e6edf3;
    --text-soft: #8b949e;
    --text-muted: #6e7681;
    --green: #2ea043;
    --blue: #58a6ff;
    --red: #f85149;
    --orange: #d29922;
    --purple: #8957e5;
}

.stApp {
    background:
        radial-gradient(circle at top left, rgba(88, 166, 255, 0.12), transparent 24%),
        radial-gradient(circle at top right, rgba(46, 160, 67, 0.08), transparent 18%),
        linear-gradient(180deg, #0d1117 0%, #0b1016 100%);
    color: var(--text-main);
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0f141b 0%, #0b1016 100%);
    border-right: 1px solid var(--border);
}

.sidebar-shell {
    padding: 0.4rem 0 0.2rem 0;
}

.sidebar-brand {
    padding: 1rem;
    border: 1px solid rgba(88, 166, 255, 0.15);
    border-radius: 16px;
    background:
        linear-gradient(135deg, rgba(88, 166, 255, 0.14), rgba(46, 160, 67, 0.08)),
        var(--bg-panel);
    box-shadow: 0 16px 40px rgba(0, 0, 0, 0.18);
}

.sidebar-brand h2 {
    margin: 0;
    color: var(--text-main);
    font-size: 1.25rem;
    font-weight: 800;
}

.sidebar-brand p {
    margin: 0.45rem 0 0 0;
    color: var(--text-soft);
    font-size: 0.88rem;
    line-height: 1.5;
}

.hero {
    padding: 1.35rem 1.45rem;
    border: 1px solid rgba(88, 166, 255, 0.18);
    border-radius: 22px;
    background:
        linear-gradient(135deg, rgba(88, 166, 255, 0.16), rgba(137, 87, 229, 0.12)),
        linear-gradient(180deg, rgba(22, 27, 34, 0.95), rgba(13, 17, 23, 0.98));
    box-shadow: 0 24px 60px rgba(0, 0, 0, 0.22);
    margin-bottom: 1rem;
}

.hero-kicker {
    display: inline-block;
    padding: 0.28rem 0.65rem;
    border-radius: 999px;
    background: rgba(46, 160, 67, 0.14);
    border: 1px solid rgba(46, 160, 67, 0.35);
    color: #8ddb9a;
    font-size: 0.72rem;
    font-weight: 700;
    letter-spacing: 0.08em;
    text-transform: uppercase;
}

.brand {
    margin-top: 0.9rem;
    font-size: 3rem;
    font-weight: 900;
    line-height: 1.02;
    letter-spacing: -0.04em;
    color: var(--text-main);
}

.brand-sub {
    margin-top: 0.65rem;
    color: #9da7b3;
    font-size: 1rem;
    line-height: 1.65;
    max-width: 920px;
}

.hero-grid {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 0.8rem;
    margin-top: 1.1rem;
}

.hero-stat {
    padding: 0.9rem 1rem;
    border-radius: 16px;
    background: rgba(13, 17, 23, 0.65);
    border: 1px solid rgba(240, 246, 252, 0.06);
}

.hero-stat-label {
    display: block;
    color: var(--text-soft);
    font-size: 0.78rem;
    margin-bottom: 0.28rem;
}

.hero-stat-value {
    color: var(--text-main);
    font-size: 1.05rem;
    font-weight: 700;
}

.section-title {
    color: var(--text-main);
    font-size: 1.05rem;
    font-weight: 800;
    margin: 0 0 0.2rem 0;
}

.section-caption {
    color: var(--text-soft);
    font-size: 0.87rem;
    margin: 0 0 1rem 0;
}

.panel-card {
    background: linear-gradient(180deg, rgba(22, 27, 34, 0.95), rgba(13, 17, 23, 0.98));
    border: 1px solid var(--border);
    border-radius: 20px;
    padding: 1rem;
    box-shadow: 0 12px 30px rgba(0, 0, 0, 0.16);
    margin-bottom: 1rem;
}

.agent-card,
.queue-card,
.history-card,
.stack-card {
    border-radius: 16px;
    padding: 0.9rem 1rem;
    margin-bottom: 0.75rem;
    border: 1px solid var(--border);
    background: rgba(31, 38, 48, 0.55);
}

.agent-card { border-left: 4px solid var(--blue); }
.agent-free { border-left-color: var(--green); }
.agent-busy { border-left-color: var(--orange); }

.status-badge {
    display: inline-block;
    padding: 0.24rem 0.52rem;
    border-radius: 999px;
    font-size: 0.72rem;
    font-weight: 700;
    letter-spacing: 0.03em;
}

.status-free {
    background: rgba(46, 160, 67, 0.12);
    color: #8ddb9a;
    border: 1px solid rgba(46, 160, 67, 0.24);
}

.status-busy {
    background: rgba(210, 153, 34, 0.12);
    color: #f2cc60;
    border: 1px solid rgba(210, 153, 34, 0.26);
}

.queue-card.next-job { border-left: 4px solid var(--blue); }
.queue-card.waiting-job { border-left: 4px solid #444c56; }

.meta-line {
    color: var(--text-soft);
    font-size: 0.84rem;
    margin-top: 0.35rem;
}

.flow-wrap {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 0.45rem;
    margin: 0.8rem 0 0 0;
}

.stage-pill {
    padding: 0.5rem 0.8rem;
    border-radius: 999px;
    font-size: 0.76rem;
    font-weight: 800;
    white-space: nowrap;
    letter-spacing: 0.02em;
    border: 1px solid var(--border);
}

.s-pendiente  { background: rgba(110, 118, 129, 0.10); color: #9aa4ae; }
.s-ejecutando { background: rgba(88, 166, 255, 0.12); color: #7fc1ff; border-color: rgba(88, 166, 255, 0.35); }
.s-exitoso    { background: rgba(46, 160, 67, 0.12); color: #8ddb9a; border-color: rgba(46, 160, 67, 0.32); }
.s-fallido    { background: rgba(248, 81, 73, 0.12); color: #ff938f; border-color: rgba(248, 81, 73, 0.28); }
.s-omitido    { background: rgba(110, 118, 129, 0.08); color: #768390; }

.stage-arrow {
    color: var(--text-muted);
    font-size: 1rem;
    font-weight: 700;
}

.console {
    background: #0b1016;
    border: 1px solid var(--border);
    border-radius: 18px;
    padding: 1rem 1.1rem;
    max-height: 420px;
    overflow-y: auto;
    font-family: "Consolas", "Courier New", monospace;
    font-size: 0.8rem;
    line-height: 1.75;
}

.l-INFO    { color: #9ecbff; }
.l-SUCCESS { color: #8ddb9a; }
.l-WARNING { color: #f2cc60; }
.l-ERROR   { color: #ff938f; }

.stack-top {
    border-left: 4px solid var(--purple);
    background: rgba(137, 87, 229, 0.10);
}

.stack-rest {
    border-left: 4px solid #444c56;
    background: rgba(31, 38, 48, 0.48);
}

.kpi-box {
    text-align: left;
    border-radius: 18px;
    padding: 1rem 1rem 0.95rem 1rem;
    background: linear-gradient(180deg, rgba(22, 27, 34, 0.96), rgba(15, 20, 27, 0.98));
    border: 1px solid var(--border);
    box-shadow: 0 10px 28px rgba(0, 0, 0, 0.14);
}

.kpi-lbl {
    font-size: 0.78rem;
    color: var(--text-soft);
    margin-bottom: 0.45rem;
    text-transform: uppercase;
    letter-spacing: 0.08em;
}

.kpi-val {
    font-size: 2rem;
    font-weight: 900;
    color: var(--text-main);
    line-height: 1;
}

.footer-note {
    text-align: center;
    color: var(--text-muted);
    font-size: 0.8rem;
    padding: 0.3rem 0 1.2rem 0;
}

div[data-testid="stButton"] > button {
    border-radius: 12px;
    border: 1px solid var(--border);
    background: linear-gradient(180deg, #212830 0%, #1b2129 100%);
    color: var(--text-main);
    font-weight: 700;
}

div[data-testid="stButton"] > button[kind="primary"] {
    background: linear-gradient(180deg, #238636 0%, #1f7a32 100%);
    border-color: rgba(46, 160, 67, 0.55);
}

div[data-testid="stSelectbox"] label,
div[data-testid="stTextInput"] label {
    color: var(--text-soft) !important;
}

div[data-baseweb="select"] > div,
div[data-testid="stTextInput"] input {
    background: #0f141b !important;
    border-color: var(--border) !important;
    color: var(--text-main) !important;
    border-radius: 12px !important;
}
</style>
"""
