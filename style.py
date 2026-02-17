
style = """<style>

/* Center main container */
.block-container {
    max-width: 800px;
    margin: auto;
    padding-top: 2rem;
}

/* Chat input area glow */
textarea {
    background: #0f172a !important;
    color: white !important;
    border-radius: 20px !important;
    border: 1px solid #334155 !important;
    padding: 12px !important;
}

/* Chat input focus glow */
textarea:focus {
    border: 1px solid #3b82f6 !important;
    box-shadow: 0 0 15px rgba(59,130,246,0.5);
}

/* Smooth chat bubbles */
[data-testid="stChatMessage"] {
    border-radius: 20px;
    padding: 14px 18px;
    animation: fadeIn 0.3s ease-in-out;
}

/* Fade animation */
@keyframes fadeIn {
    from {opacity: 0; transform: translateY(5px);}
    to {opacity: 1; transform: translateY(0);}
}

</style>
"""