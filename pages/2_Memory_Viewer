import streamlit as st
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Memory Viewer", page_icon="🧠")

st.title("🧠 Vector Memory Viewer")

# Connect to MySQL
conn = mysql.connector.connect(
    host=os.getenv("MYSQL_HOST", "localhost"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    database=os.getenv("MYSQL_DATABASE", "aimemory"),
)

cursor = conn.cursor()

cursor.execute("SELECT id, user_id, content, created_at FROM memory ORDER BY id DESC LIMIT 50")
rows = cursor.fetchall()

st.subheader("Stored Memories (Latest 50)")

for row in rows:
    memory_id, user_id, content, created_at = row

    with st.expander(f"Memory ID {memory_id} | User: {user_id}"):
        st.write("Created:", created_at)
        st.write(content[:1000])

cursor.close()
conn.close()
