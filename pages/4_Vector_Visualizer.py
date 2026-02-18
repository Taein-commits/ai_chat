import streamlit as st
import mysql.connector
import os
import json
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Vector Visualizer", page_icon="🧠")

st.title("🧠 Vector Memory Visualizer")

# Connect to DB
conn = mysql.connector.connect(
    host=os.getenv("MYSQL_HOST", "localhost"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    database=os.getenv("MYSQL_DATABASE", "aimemory"),
)

cursor = conn.cursor()
cursor.execute("SELECT content, embedding FROM memory LIMIT 200")
rows = cursor.fetchall()

cursor.close()
conn.close()

if not rows:
    st.warning("No memory stored yet.")
    st.stop()

embeddings = []
texts = []

for content, emb_json in rows:
    try:
        emb = np.array(json.loads(emb_json))
        embeddings.append(emb)
        texts.append(content[:80])
    except:
        continue

if len(embeddings) < 2:
    st.warning("Not enough vectors to visualize.")
    st.stop()

# PCA Reduction
pca = PCA(n_components=2)
reduced = pca.fit_transform(np.array(embeddings))

# Plot
fig, ax = plt.subplots(figsize=(8,6))
ax.scatter(reduced[:,0], reduced[:,1])

for i, txt in enumerate(texts):
    ax.annotate(str(i+1), (reduced[i,0], reduced[i,1]))

ax.set_title("Memory Vector Map (PCA)")
st.pyplot(fig)

st.subheader("Memory Index Reference")

for i, txt in enumerate(texts):
    st.write(f"{i+1}. {txt}")
