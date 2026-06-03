import os

documents = []

# ✅ Load documents
def load_documents():
    global documents
    documents = []

    folder_path = os.path.join(os.path.dirname(__file__), "data")

    print("📁 Loading from:", folder_path)

    if not os.path.exists(folder_path):
        print("❌ data folder NOT FOUND")
        return

    for file in os.listdir(folder_path):
        print("📄 Found file:", file)

        if file.endswith(".txt"):
            with open(os.path.join(folder_path, file), "r", encoding="utf-8") as f:
                documents.append(f.read().lower())

    print("✅ Total documents:", len(documents))


# ✅ Retrieve context
def retrieve_context(query):
    query_words = query.lower().split()
    results = []

    for doc in documents:
        for line in doc.split("\n"):

            line_lower = line.lower()
            score = 0

            for word in query_words:
                if word in line_lower:
                    score += 1

            if score > 0 and len(line.strip()) > 10:
                results.append((score, line.strip()))

    # ✅ sort results
    results.sort(reverse=True, key=lambda x: x[0])

    # ✅ format top results
    top_lines = [line for score, line in results[:5]]

    formatted = []
    for i, line in enumerate(top_lines, start=1):
        formatted.append(f"{i}. {line}")

    return "\n".join(formatted)
