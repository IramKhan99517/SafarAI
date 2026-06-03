from sopengine import read_file
from healthapi import get_heat_risk
from locationapi import find_place

def agent_flow(question):
    q = question.lower()

    # ✅ Ritual SOP
    if "tawaf" in q:
        return read_file("Tawaf_rituals.txt")

    elif "sai" in q:
        return read_file("sai_rituals.txt")

    # ✅ Health API + SOP ✅
    elif "heat" in q or "temperature" in q or "weather" in q or "exhaustion" in q:

        api_response = get_heat_risk()
        sop_response = read_file("health_precautions.txt")

        return f"""{api_response}

📘 General Health Guidance:
{sop_response}
"""

    # ✅ Location API (NOW FIXED ✅)
    elif "hospital" in q or "hotel" in q or "police" in q:
        return find_place(question)

    # ✅ fallback
    return "❗ No relevant information found. Try asking about Tawaf, Sai, health, or hospitals."
