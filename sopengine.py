import os

def read_file(filename):
    try:
        base_path = os.path.dirname(__file__)

        # ✅ FIXED PATH (data folder added)
        file_path = os.path.join(base_path, "data", filename)

        if not os.path.exists(file_path):
            return "❌ Information not found."

        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

        return content.strip()

    except Exception as e:
        print("❌ SOP Engine Error:", e)
        return "⚠️ Error reading SOP data"