import requests

def get_heat_risk():
    try:
        url = "https://api.open-meteo.com/v1/forecast?latitude=21.4225&longitude=39.8262&current_weather=true"

        res = requests.get(url, timeout=5)
        data = res.json()

        temp = data["current_weather"]["temperature"]

        # ✅ Risk levels
        if temp >= 45:
            alert = "🔴 High Risk"
            actions = [
                "Avoid sunlight immediately",
                "Drink water continuously",
                "Rest in shaded area",
                "Seek medical help"
            ]

        elif temp >= 38:
            alert = "🟡 Moderate Risk"
            actions = [
                "Limit sun exposure",
                "Drink water frequently",
                "Wear light clothes",
                "Take rest breaks"
            ]

        else:
            alert = "🟢 Low Risk"
            actions = [
                "Stay hydrated",
                "Wear comfortable clothes",
                "Avoid long exposure"
            ]

        return (
            f"🌡 Temperature: {temp}°C\n"
            f"🚨 Heat Alert: {alert}\n\n"
            + "\n".join(actions)
        )

    except:
        return "Health data unavailable"