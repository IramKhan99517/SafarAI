def find_place(query):
    query_lower = query.lower()

    # ✅ HOSPITALS
    if "hospital" in query_lower:
        return (
            "📍 Nearby Hospitals\n\n"
            "1. Mina Emergency Hospital\n"
            "   Area: Mina, Makkah\n\n"
            "2. King Abdullah Medical City\n"
            "   Area: Makkah\n\n"
            "3. Al Noor Specialist Hospital\n"
            "   Area: Makkah\n\n"
            "📌 Tip:\n"
            "Visit the nearest hospital immediately in case of emergency.\n"
            "Official Health Info: https://www.moh.gov.sa"
        )

    # ✅ HOTELS
    elif "hotel" in query_lower:
        return (
            "📍 Hotels in Makkah\n\n"
            "1. Swissotel Makkah\n"
            "   Area: Near Masjid al-Haram\n\n"
            "2. Fairmont Clock Tower Hotel\n"
            "   Area: Abraj Al Bait Complex\n\n"
            "3. Pullman ZamZam Makkah\n"
            "   Area: King Abdul Aziz Gate\n\n"
            "📌 Tip:\n"
            "Choose hotels close to Haram for easy access.\n"
            "Official Tourism Info: https://www.visitsaudi.com"
        )

    # ✅ POLICE
    elif "police" in query_lower:
        return (
            "📍 Police Stations in Makkah\n\n"
            "1. Makkah Central Police Station\n\n"
            "2. Al Haram Police Unit\n\n"
            "3. Mina Security Center\n\n"
            "📌 Tip:\n"
            "Contact nearest police station for emergency assistance.\n"
            "Official Support: https://www.moi.gov.sa"
        )

    # ✅ DEFAULT LOCATION
    else:
        return (
            "📍 Important Location\n\n"
            "Masjid al-Haram\n"
            "Central Makkah\n"
            "Saudi Arabia\n\n"
            "📌 Tip:\n"
            "Follow official Hajj guidelines for safe pilgrimage.\n"
            "Official Info: https://www.nusuk.sa"
        )
