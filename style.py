style = """
<style>

/* ============================= */
/* ROOT COLORS */
/* ============================= */

:root {
    --bg-main: linear-gradient(90deg,rgba(131, 58, 180, 1) 0%, rgba(52, 213, 224, 1) 50%, rgba(255, 200, 0, 1) 100%); /* Dark gray background */
    --bg-card: transparent;    /* Remove big card */
    --bg-bubble: #2a2a2a;      
    --bg-user: #3b82f6;
    --border-subtle: #333333;
    --text-main: #f1f1f1;
    --text-muted: #aaaaaa;
    --accent: #3b82f6;
}

/* ============================= */
/* GLOBAL */
/* ============================= */

html, body, section.main {
    background-color: var(--bg-main) !important;
    color: var(--text-main);
    font-family: "Inter", "Segoe UI", sans-serif;
}

/* Remove Streamlit container styling */
.block-container {
    background-color: transparent !important;
    max-width: 900px;
    margin: 40px auto;
    padding: 0;
}

/* REMOVE big vertical block box */
[data-testid="stVerticalBlock"] > div {
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
    padding: 0 !important;
}

/* ============================= */
/* CHAT BUBBLES */
/* ============================= */

[data-testid="stChatMessage"] {
    border-radius: 12px;
    padding: 14px 18px;
    margin-bottom: 14px;
    background-color: var(--bg-bubble);
    border: 1px solid var(--border-subtle);
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
    background-color: #2a2a2a !important;
    color: var(--text-main) !important;
    border-radius: 10px !important;
    border: 1px solid var(--border-subtle) !important;
    padding: 12px !important;
}

textarea:focus {
    border: 1px solid var(--accent) !important;
    box-shadow: 0 0 0 2px rgba(59,130,246,0.3);
}

/* ============================= */
/* BUTTON */
/* ============================= */

button[kind="primary"] {
    background-color: var(--accent);
    border-radius: 8px;
    border: none;
}

button[kind="primary"]:hover {
    background-color: #2563eb;
}

</style>
"""
