from app.rag.retriever import retrieve_documents
from app.agents.planner_agent import plan_task
from app.agents.synthesizer_agent import synthesize

def generate_report(query):
    plan = plan_task(query)
    docs = retrieve_documents(query)
    context = "\n".join(docs)
    report = synthesize(context, query)

    return{
        "plan" : plan,
        "report " : report 
    }