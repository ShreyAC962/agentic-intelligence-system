from app.db import SessionLocal
from app.models import Document

from openai import OpenAI

# For working with vectors in PostgreSQL (pgvector)
from sqlalchemy import text

client = OpenAI()

def get_embedding(text):
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input = text
    )
    return response.data[0].embedding


def retrieve_documents(query):
    session = SessionLocal()
    query_embedding = get_embedding(query)
    # SQL query using pqvector similarity search
    # <=> operator = cosine distance in pgvector
    sql = text("""
            SELECT id, content
            FROM documents
            ORDER BY embedding <=> :query_embedding
            LIMIT 5;
        """)
    results = session.execute(sql, {
        "query_embedding" : query_embedding
    }).fetchall()

    return [row.content for row in results]
        