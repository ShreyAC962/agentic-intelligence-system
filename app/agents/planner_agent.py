from langchain.chat_models import ChatOpenAI
from app.config import OPENAI_API_KEY

llm = ChatOpenAI(
    model = "gpt-4o",
    openai_api_key = OPENAI_API_KEY
)

def plan_task(query):
    prompt = f"""
    You are a planning agent.
    User Query:
    {query}
    Decide:
    1. What data is needed
    2. What should be retrived
    3. How to summarize

    Return structured plan.
    """
    return llm.predict(prompt)