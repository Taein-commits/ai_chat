import mysql.connector
import json
import numpy as np
from typing import List
from numpy.typing import NDArray

__all__ = ["MySQLMemory"]


class MySQLMemory:

    def __init__(
        self,
        host: str,
        user: str,
        password: str,
        database: str
    ) -> None:

        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS memory (
                id INT AUTO_INCREMENT PRIMARY KEY,
                user_id VARCHAR(255),
                content TEXT,
                embedding LONGTEXT
            )
        """)
        self.conn.commit()

    def save_memory(
        self,
        user_id: str,
        content: str,
        embedding: List[float]
    ) -> None:

        emb_json: str = json.dumps(embedding)

        self.cursor.execute(
            "INSERT INTO memory (user_id, content, embedding) VALUES (%s, %s, %s)",
            (user_id, content, emb_json)
        )
        self.conn.commit()

    def retrieve_memory(
        self,
        user_id: str,
        query_embedding: List[float],
        top_k: int = 3
    ) -> List[str]:

        self.cursor.execute(
            "SELECT content, embedding FROM memory WHERE user_id=%s",
            (user_id,)
        )

        rows = self.cursor.fetchall()
        results: List[tuple[str, float]] = []

        query_vec: NDArray[np.float64] = np.array(query_embedding)

        for row in rows:
            if len(row) != 2:
                continue

            content_raw, emb_json = row

            if not isinstance(content_raw, str):
                continue

            if not isinstance(emb_json, str):
                continue

            content: str = content_raw

            emb_vec: NDArray[np.float64] = np.array(json.loads(emb_json))
            score: float = self.cosine_similarity(query_vec, emb_vec)

            results.append((content, score))

        results.sort(key=lambda x: x[1], reverse=True)

        return results[:top_k]

    def cosine_similarity(
        self,
        a: NDArray[np.float64],
        b: NDArray[np.float64]
    ) -> float:

        return float(
            np.dot(a, b) /
            (np.linalg.norm(a) * np.linalg.norm(b))
        )

    def close(self) -> None:
        self.cursor.close()
        self.conn.close()
