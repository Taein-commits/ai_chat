style = """
<style>

/* ============================= */
/* GLOBAL RESET */
/* ============================= */

html, body {
    margin: 0;
    height: 100%;
}

/* ============================= */
/* FULL SCREEN ANIMATED BACKGROUND */
/* ============================= */

[data-testid="stAppViewContainer"] {
    background: linear-gradient(
        -45deg,
        #833ab4,
        #34d5e0,
        #ffc800,
        #ff4ecd
    );
    background-size: 400% 400%;
    animation: gradientMove 15s ease infinite;
    min-height: 100vh;
}

/* Background Animation */
@keyframes gradientMove {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* ============================= */
/* REMOVE DEFAULT STREAMLIT WHITE BACKGROUNDS */
/* ============================= */

section.main,
.block-container,
[data-testid="stHeader"],
[data-testid="stToolbar"],
[data-testid="stVerticalBlock"] > div {
    background: transparent !important;
}

/* ============================= */
/* SIDEBAR */
/* ============================= */

section[data-testid="stSidebar"] > div {
    background: #1e1e1e !important;
}

/* ============================= */
/* BOTTOM CHAT BAR (GRADIENT) */
/* ============================= */

[data-testid="stBottom"] {
    background: linear-gradient(
        90deg,
        rgba(131,58,180,0.95),
        rgba(52,213,224,0.95),
        rgba(255,200,0,0.95)
    );
    backdrop-filter: blur(8px);
    border-top: 1px solid rgba(255,255,255,0.2);
}

/* ============================= */
/* CHAT BUBBLES (GLASS STYLE) */
/* ============================= */

[data-testid="stChatMessage"] {
    border-radius: 16px;
    padding: 14px 18px;
    margin-bottom: 14px;
    background: rgba(0,0,0,0.45);
    backdrop-filter: blur(6px);
    border: 1px solid rgba(255,255,255,0.1);
    color: white;
    animation: fadeIn 0.3s ease-in-out;
}

/* User bubble */
[data-testid="stChatMessage"]:has(div[data-testid="chatAvatarIcon-user"]) {
    background: rgba(59,130,246,0.85);
    border: none;
}

/* Fade Animation */
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(6px); }
    to { opacity: 1; transform: translateY(0); }
}

/* ============================= */
/* CHAT INPUT */
/* ============================= */

[data-testid="stChatInput"] {
    background: transparent !important;
}

[data-testid="stChatInput"] textarea {
    background: rgba(0,0,0,0.7) !important;
    color: white !important;
    border-radius: 12px !important;
    border: 1px solid rgba(255,255,255,0.2) !important;
}

[data-testid="stChatInput"] textarea:focus {
    border: 1px solid #3b82f6 !important;
    box-shadow: 0 0 12px rgba(59,130,246,0.6);
}

/* ============================= */
/* BUTTON */
/* ============================= */

button[kind="primary"] {
    background: #3b82f6;
    border-radius: 10px;
    border: none;
}

button[kind="primary"]:hover {
    background: #2563eb;
}

</style>
"""
