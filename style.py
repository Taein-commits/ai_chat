style = """
<style>

/* ============================= */
/* ROOT */
/* ============================= */

html, body {
    margin: 0;
    height: 100%;
}

/* ============================= */
/* ANIMATED GRADIENT BACKGROUND */
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
    animation: gradientMove 12s ease infinite;
    min-height: 100vh;
}

/* Gradient Animation */
@keyframes gradientMove {
    0% { background-position: 0% 50%; }
    25% { background-position: 50% 100%; }
    50% { background-position: 100% 50%; }
    75% { background-position: 50% 0%; }
    100% { background-position: 0% 50%; }
}

/* ============================= */
/* REMOVE DEFAULT STREAMLIT BG */
/* ============================= */

section.main,
.block-container,
[data-testid="stHeader"],
[data-testid="stToolbar"],
[data-testid="stSidebar"],
[data-testid="stVerticalBlock"] > div {
    background: transparent !important;
}

/* ============================= */
/* CHAT BUBBLES */
/* ============================= */

[data-testid="stChatMessage"] {
    border-radius: 14px;
    padding: 14px 18px;
    margin-bottom: 14px;
    background: rgba(0,0,0,0.45);
    backdrop-filter: blur(6px);
    border: 1px solid rgba(255,255,255,0.1);
    color: white;
}

/* User bubble */
[data-testid="stChatMessage"]:has(div[data-testid="chatAvatarIcon-user"]) {
    background: rgba(59,130,246,0.8);
    border: none;
}

/* ============================= */
/* CHAT INPUT */
/* ============================= */

textarea {
    background: rgba(0,0,0,0.6) !important;
    color: white !important;
    border-radius: 12px !important;
    border: 1px solid rgba(255,255,255,0.2) !important;
}

textarea:focus {
    border: 1px solid #3b82f6 !important;
    box-shadow: 0 0 10px rgba(59,130,246,0.5);
}

/* ============================= */
/* BUTTON */
/* ============================= */

button[kind="primary"] {
    background: #3b82f6;
    border-radius: 8px;
    border: none;
}

button[kind="primary"]:hover {
    background: #2563eb;
}

/* ============================= */
/* SMOOTH FADE IN */
/* ============================= */

[data-testid="stChatMessage"] {
    animation: fadeIn 0.3s ease-in-out;
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(6px); }
    to { opacity: 1; transform: translateY(0); }
}

</style>
"""
