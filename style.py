style = """
<style>

/* ============================= */
/* GLOBAL BACKGROUND */
/* ============================= */

html, body, [data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #0f172a, #1e293b, #0f172a);
    background-attachment: fixed;
    color: white;
    font-family: 'Inter', sans-serif;
}

/* ============================= */
/* CENTER MAIN CONTAINER */
/* ============================= */

.block-container {
    max-width: 850px;
    margin: auto;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* ============================= */
/* CHAT MESSAGES */
/* ============================= */

[data-testid="stChatMessage"] {
    border-radius: 20px;
    padding: 14px 18px;
    margin-bottom: 12px;
    backdrop-filter: blur(10px);
    background: rgba(30, 41, 59, 0.6);
    border: 1px solid rgba(255,255,255,0.08);
    animation: fadeIn 0.3s ease-in-out;
    transition: 0.2s ease-in-out;
}

/* Hover smooth effect */
[data-testid="stChatMessage"]:hover {
    transform: scale(1.01);
}

/* User bubble */
[data-testid="stChatMessage"]:has(div[data-testid="chatAvatarIcon-user"]) {
    background: rgba(59,130,246,0.2);
    border: 1px solid rgba(59,130,246,0.5);
}

/* Assistant bubble */
[data-testid="stChatMessage"]:has(div[data-testid="chatAvatarIcon-assistant"]) {
    background: rgba(100,116,139,0.2);
    border: 1px solid rgba(100,116,139,0.4);
}

/* ============================= */
/* CHAT INPUT */
/* ============================= */

textarea {
    background: #0f172a !important;
    color: white !important;
    border-radius: 20px !important;
    border: 1px solid #334155 !important;
    padding: 12px !important;
    font-size: 15px !important;
    caret-color: #3b82f6;
}

/* Focus glow */
textarea:focus {
    border: 1px solid #3b82f6 !important;
    box-shadow: 0 0 15px rgba(59,130,246,0.5);
}

/* Floating chat input container */
[data-testid="stChatInput"] {
    position: sticky;
    bottom: 20px;
    background: rgba(15,23,42,0.9);
    padding: 10px;
    border-radius: 20px;
    backdrop-filter: blur(10px);
}

/* ============================= */
/* BUTTON STYLE */
/* ============================= */

button[kind="primary"] {
    background: linear-gradient(90deg, #3b82f6, #6366f1);
    border: none;
    border-radius: 20px;
    transition: 0.2s ease-in-out;
}

button[kind="primary"]:hover {
    transform: scale(1.05);
    box-shadow: 0 0 10px rgba(59,130,246,0.6);
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
    border-radius: 10px;
}

::-webkit-scrollbar-thumb:hover {
    background: #475569;
}

/* ============================= */
/* FADE ANIMATION */
/* ============================= */

@keyframes fadeIn {
    from {opacity: 0; transform: translateY(5px);}
    to {opacity: 1; transform: translateY(0);}
}

</style>
"""
