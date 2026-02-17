import mysql.connector
import json
import numpy as np

class MySQLMemory:

    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.conn.cursor()

    # ---------------------------
    # Save memory
    # ---------------------------
    def save_memory(self, user_id, content, embedding):
        query = """
        INSERT INTO ai_memory (user_id, content, embedding)
        VALUES (%s, %s, %s)
        """
        self.cursor.execute(query, (user_id, content, json.dumps(embedding)))
        self.conn.commit()

    # ---------------------------
    # Retrieve memory
    # ---------------------------
    def retrieve_memory(self, user_id, query_embedding, top_k=3):
        query = """
        SELECT content, embedding FROM ai_memory
        WHERE user_id = %s
        """
        self.cursor.execute(query, (user_id,))
        rows = self.cursor.fetchall()

        scored = []

        for content, emb_json in rows:
            emb = np.array(json.loads(emb_json))
            score = self.cosine_similarity(query_embedding, emb)
            scored.append((score, content))

        scored.sort(reverse=True)
        return [content for score, content in scored[:top_k]]

    # ---------------------------
    # Cosine similarity
    # ---------------------------
    def cosine_similarity(self, a, b):
        return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

    def close(self):
        self.cursor.close()
        self.conn.close()
