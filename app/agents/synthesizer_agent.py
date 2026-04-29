from langchain.chat_models import ChatOpenAI
from app.config import OPENAI_API_KEY

llm = ChatOpenAI(model="gpt-4o", openai_api_key=OPENAI_API_KEY)

def synthesize(context, query):
    prompt = f"""
    You are an enterprise AI analyst.

    Context:
    {context}

    Query:
    {query}

    Create an executive-level technical brief:
    - Summary
    - Key insights
    - Risks
    - Recommendations
    """

    return llm.predict(prompt)