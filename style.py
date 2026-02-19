style = """
<style>

/* ============================= */
/* GLOBAL BACKGROUND */
/* ============================= */

html, body, [data-testid="stAppViewContainer"] {
    background-color: #0f172a;
    color: #e2e8f0;
    font-family: "Segoe UI", -apple-system, BlinkMacSystemFont, sans-serif;
}

/* ============================= */
/* SIDEBAR */
/* ============================= */

[data-testid="stSidebar"] {
    background-color: #111827;
    border-right: 1px solid #1f2937;
}

[data-testid="stSidebar"] * {
    color: #cbd5e1 !important;
}

/* ============================= */
/* MAIN CONTAINER */
/* ============================= */

.block-container {
    max-width: 1000px;
    margin: 40px auto;
    padding: 40px;
    background-color: #111827;
    border-radius: 16px;
    border: 1px solid #1f2937;
}

/* ============================= */
/* HEADER */
/* ============================= */

h1 {
    text-align: center;
    font-weight: 600;
    color: #e2e8f0;
    margin-bottom: 40px;
}

/* ============================= */
/* CHAT BUBBLES */
/* ============================= */

[data-testid="stChatMessage"] {
    border-radius: 12px;
    padding: 16px 18px;
    margin-bottom: 14px;
    background-color: #1e293b;
    border: 1px solid #273549;
    transition: 0.2s ease;
}

/* User bubble */
[data-testid="stChatMessage"]:has(div[data-testid="chatAvatarIcon-user"]) {
    background-color: #1d4ed8;
    border: none;
    color: white;
}

/* Assistant bubble */
[data-testid="stChatMessage"]:has(div[data-testid="chatAvatarIcon-assistant"]) {
    background-color: #1e293b;
}

/* Subtle hover */
[data-testid="stChatMessage"]:hover {
    border: 1px solid #334155;
}

/* ============================= */
/* CHAT INPUT */
/* ============================= */

textarea {
    background-color: #0f172a !important;
    color: #e2e8f0 !important;
    border-radius: 10px !important;
    border: 1px solid #334155 !important;
    padding: 12px !important;
    font-size: 15px !important;
}

/* Focus effect */
textarea:focus {
    border: 1px solid #3b82f6 !important;
    box-shadow: 0 0 0 2px rgba(59,130,246,0.2);
}

/* Chat input container */
[data-testid="stChatInput"] {
    margin-top: 20px;
}

/* ============================= */
/* BUTTONS */
/* ============================= */

button[kind="primary"] {
    background-color: #2563eb;
    border-radius: 8px;
    border: none;
}

button[kind="primary"]:hover {
    background-color: #1d4ed8;
}

/* ============================= */
/* DROPDOWNS & SELECT */
/* ============================= */

div[data-baseweb="select"] {
    background-color: #0f172a !important;
    border-radius: 8px;
}

/* ============================= */
/* SCROLLBAR */
/* ============================= */

::-webkit-scrollbar {
    width: 8px;
}

::-webkit-scrollbar-track {
    background: #0f172a;
}

::-webkit-scrollbar-thumb {
    background: #334155;
    border-radius: 8px;
}

::-webkit-scrollbar-thumb:hover {
    background: #475569;
}

</style>
"""
