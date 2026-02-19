style = """
<style>

/* ============================= */
/* ROOT VARIABLES (clean control) */
/* ============================= */

:root {
    --bg-main: #0b1220;
    --bg-card: #111827;
    --bg-bubble: #1f2937;
    --bg-user: #1e40af;
    --border-subtle: #1f2937;
    --border-light: #334155;
    --text-main: #e5e7eb;
    --text-muted: #94a3b8;
    --accent: #3b82f6;
}

/* ============================= */
/* GLOBAL BACKGROUND */
/* ============================= */

html, body, [data-testid="stAppViewContainer"] {
    background-color: var(--bg-main);
    color: var(--text-main);
    font-family: "Inter", "Segoe UI", -apple-system, BlinkMacSystemFont, sans-serif;
}

/* Remove Streamlit top spacing */
.block-container {
    max-width: 1100px;
    margin: 40px auto;
    padding: 40px;
    background-color: var(--bg-card);
    border-radius: 18px;
    border: 1px solid var(--border-subtle);
    box-shadow: 0 20px 50px rgba(0,0,0,0.4);
}

/* ============================= */
/* SIDEBAR */
/* ============================= */

[data-testid="stSidebar"] {
    background-color: #0f172a;
    border-right: 1px solid var(--border-subtle);
}

[data-testid="stSidebar"] * {
    color: var(--text-muted) !important;
}

[data-testid="stSidebar"] .stSelectbox,
[data-testid="stSidebar"] .stCheckbox {
    background-color: transparent;
}

/* ============================= */
/* HEADER */
/* ============================= */

h1 {
    text-align: center;
    font-weight: 600;
    letter-spacing: 0.5px;
    color: var(--text-main);
    margin-bottom: 50px;
}

/* ============================= */
/* CHAT BUBBLES */
/* ============================= */

[data-testid="stChatMessage"] {
    border-radius: 14px;
    padding: 18px 20px;
    margin-bottom: 16px;
    background-color: var(--bg-bubble);
    border: 1px solid var(--border-subtle);
    transition: all 0.2s ease;
}

/* Assistant bubble */
[data-testid="stChatMessage"]:has(div[data-testid="chatAvatarIcon-assistant"]) {
    background-color: var(--bg-bubble);
}

/* User bubble */
[data-testid="stChatMessage"]:has(div[data-testid="chatAvatarIcon-user"]) {
    background-color: var(--bg-user);
    border: none;
    color: white;
    box-shadow: 0 4px 20px rgba(30,64,175,0.4);
}

/* Hover subtle lift */
[data-testid="stChatMessage"]:hover {
    border: 1px solid var(--border-light);
}

/* ============================= */
/* CHAT INPUT */
/* ============================= */

textarea {
    background-color: #0f172a !important;
    color: var(--text-main) !important;
    border-radius: 12px !important;
    border: 1px solid var(--border-subtle) !important;
    padding: 14px !important;
    font-size: 15px !important;
    transition: all 0.2s ease;
}

/* Focus effect */
textarea:focus {
    border: 1px solid var(--accent) !important;
    box-shadow: 0 0 0 3px rgba(59,130,246,0.2);
}

/* Input container spacing */
[data-testid="stChatInput"] {
    margin-top: 30px;
}

/* ============================= */
/* BUTTONS */
/* ============================= */

button[kind="primary"] {
    background-color: var(--accent);
    border-radius: 10px;
    border: none;
    padding: 8px 18px;
    font-weight: 500;
    transition: all 0.2s ease;
}

button[kind="primary"]:hover {
    background-color: #2563eb;
    box-shadow: 0 5px 18px rgba(59,130,246,0.3);
}

/* ============================= */
/* SELECT / DROPDOWN */
/* ============================= */

div[data-baseweb="select"] {
    background-color: #0f172a !important;
    border-radius: 10px;
    border: 1px solid var(--border-subtle) !important;
}

/* ============================= */
/* SCROLLBAR */
/* ============================= */

::-webkit-scrollbar {
    width: 8px;
}

::-webkit-scrollbar-track {
    background: #0b1220;
}

::-webkit-scrollbar-thumb {
    background: #1f2937;
    border-radius: 10px;
}

::-webkit-scrollbar-thumb:hover {
    background: #334155;
}

/* ============================= */
/* REMOVE STREAMLIT HEADER */
/* ============================= */

header[data-testid="stHeader"] {
    background: transparent;
}

/* ============================= */
/* OPTIONAL: SUBTLE PAGE GLOW */
/* ============================= */

[data-testid="stAppViewContainer"]::before {
    content: "";
    position: fixed;
    width: 800px;
    height: 800px;
    top: -200px;
    right: -200px;
    background: radial-gradient(circle, rgba(59,130,246,0.08), transparent 70%);
    z-index: 0;
    pointer-events: none;
}

</style>
"""
