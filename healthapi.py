import requests

def get_heat_risk():
    try:
        url = "https://api.open-meteo.com/v1/forecast?latitude=21.4225&longitude=39.8262&current_weather=true"

        res = requests.get(url, timeout=5)
        data = res.json()

        temp = data["current_weather"]["temperature"]

        # ✅ HIGH RISK
        if temp >= 45:
            return f"""🌡️ Temperature: {temp}°C  
🔴 HIGH RISK (Heat Exhaustion)

🚨 Immediate Actions:
1. Avoid going outside
2. Stay in air-conditioned areas
3. Drink water continuously
4. Use umbrella and cooling cloth
5. Seek medical help if dizziness occurs
"""

        # ✅ MODERATE RISK
        elif temp >= 38:
            return f"""🌡️ Temperature: {temp}°C  
🟡 MODERATE RISK

⚠️ Precautions:
1. Drink water frequently
2. Avoid peak afternoon heat
3. Wear light and loose clothing
4. Take rest in shaded areas
"""

        # ✅ LOW / GENERAL
        else:
            return f"""🌡️ Temperature: {temp}°C  
🟢 LOW RISK

✅ General Advice:
1. Stay hydrated
2. Follow normal safety measures
3. Keep water bottle with you
"""

    except Exception as e:
        print("❌ Error:", e)
        return "⚠️ Unable to fetch live weather data"
