style = """
<style>

/* ============================= */
/* ROOT COLORS */
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
/* GLOBAL */
/* ============================= */

html, body {
    background-color: var(--bg-main);
    color: var(--text-main);
    font-family: "Inter", "Segoe UI", sans-serif;
}

/* Main content area */
section.main {
    background-color: var(--bg-main) !important;
}

/* Remove default white wrappers */
.block-container {
    background-color: transparent !important;
    max-width: 1100px;
    margin: 40px auto;
    padding: 0;
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

/* ============================= */
/* HEADER */
/* ============================= */

h1 {
    text-align: center;
    font-weight: 600;
    letter-spacing: 0.5px;
    color: var(--text-main);
    margin: 40px 0 60px 0;
}

/* ============================= */
/* CHAT AREA CARD */
/* ============================= */

[data-testid="stVerticalBlock"] > div {
    background-color: var(--bg-card);
    border-radius: 18px;
    border: 1px solid var(--border-subtle);
    padding: 40px;
    box-shadow: 0 20px 50px rgba(0,0,0,0.4);
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
    transition: 0.2s ease;
}

/* User bubble */
[data-testid="stChatMessage"]:has(div[data-testid="chatAvatarIcon-user"]) {
    background-color: var(--bg-user);
    border: none;
    color: white;
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
}

textarea:focus {
    border: 1px solid var(--accent) !important;
    box-shadow: 0 0 0 3px rgba(59,130,246,0.2);
}

/* ============================= */
/* BUTTON */
/* ============================= */

button[kind="primary"] {
    background-color: var(--accent);
    border-radius: 10px;
    border: none;
}

button[kind="primary"]:hover {
    background-color: #2563eb;
}

/* ============================= */
/* SCROLLBAR */
/* ============================= */

::-webkit-scrollbar {
    width: 8px;
}

::-webkit-scrollbar-thumb {
    background: #1f2937;
    border-radius: 10px;
}

::-webkit-scrollbar-thumb:hover {
    background: #334155;
}

</style>
"""
