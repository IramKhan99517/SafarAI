from rag import retrieve_context
from healthapi import get_heat_risk
from locationapi import find_place
from rag import load_documents, retrieve_context

load_documents() 

def agent_flow(query):
    q = query.lower()

    # ✅ HEALTH
    if "heat" in q or "health" in q:
        return get_heat_risk()

    # ✅ LOCATION
    elif "hospital" in q or "police" in q or "hotel" in q:
        return find_place(query)

    # ✅ RAG (rituals)
    else:
        context = retrieve_context(query)

        if not context:
            return "No relevant information found."

        return context