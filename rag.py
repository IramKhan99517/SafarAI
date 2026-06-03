import os
from healthapi import get_heat_risk

# ✅ Store documents
documents = {
    "health": [],
    "sai": [],
    "tawaf": []
}


# ✅ Load documents
def load_documents():
    global documents

    folder_path = os.path.join(os.path.dirname(__file__), "data")
    print("📁 Loading from:", folder_path)

    if not os.path.exists(folder_path):
        print("❌ data folder NOT FOUND")
        return

    for file in os.listdir(folder_path):
        print("📄 Found file:", file)

        if file.endswith(".txt"):
            with open(os.path.join(folder_path, file), "r", encoding="utf-8") as f:
                content = f.read()

                if "SAI_RITUAL" in content:
                    documents["sai"].append(content)

                elif "TAWAF_RITUAL" in content:
                    documents["tawaf"].append(content)

                else:
                    documents["health"].append(content)

    print("✅ Documents loaded:", {k: len(v) for k, v in documents.items()})


# ✅ Extract section
def get_section(section_name, topic):
    docs = documents.get(topic, [])

    for doc in docs:
        lines = doc.split("\n")
        capture = False
        output = []

        for line in lines:
            if section_name.upper() in line:
                capture = True
                continue

            if capture and line.strip().endswith(":") and section_name.upper() not in line:
                break

            if capture:
                output.append(line)

        if output:
            return "\n".join(output).strip()

    return "Section not found."


# ✅ MAIN AI ENGINE
def ask_rag(query):
    q = query.lower()

    # ✅ HEALTH / HEAT
    if any(word in q for word in ["heat", "temperature", "sun", "hot", "health"]):
        data = get_heat_risk()

        if data:
            temp = data["temperature"]
            risk = data["risk"]
            alert = data["alert"]

            section_map = {
                "high": "HEALTH_HIGH",
                "moderate": "HEALTH_MODERATE",
                "low": "HEALTH_LOW"
            }

            general = get_section("HEALTH_GENERAL", "health")
            actions = get_section(section_map[risk], "health")

            return (
                "🌞 Health Precautions:\n\n"
                + general
                + f"\n\n🌡 Temperature: {temp}°C"
                + f"\n🚨 Heat Alert: {alert}"
                + "\n\n📋 Recommended Actions:\n"
                + actions
            )

    # ✅ SAI
    if any(word in q for word in ["sai", "safa", "marwa"]):
        return "🕋 Sa’i Ritual:\n\n" + get_section("SAI_RITUAL", "sai")

    # ✅ TAWAF
    if any(word in q for word in ["tawaf", "kaaba"]):
        return "🕋 Tawaf Ritual:\n\n" + get_section("TAWAF_RITUAL", "tawaf")

    return None  # ✅ important for agent fallback
