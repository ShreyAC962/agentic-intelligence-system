from app.db import SessionLocal
from app.models import Document

def load_document(file_path):
    with open(file_path, "r") as f:
        return f.read() # Read entire file content as a string and return it
    

def ingest_document(file_path):
    # Create a new database session - To perform db operations
    session = SessionLocal()
    content = load_document(file_path)
    # Create new document object(row)
    doc = Document(content=content, doc_metadata="sample")

    try:
        # Add document object to the session - inserted to database
        session.add(doc)
        # Save the data in PostgreSQL
        session.commit()
        print("Document ingested successfully")
    except Exception as e:
        session.rollback() # Undo all the changes made in the current transaction
        print("Error:", e)
    finally:
        session.close()

if __name__ == "__main__":
    ingest_document("data/sample_doc.txt")