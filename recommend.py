from data import vehicles

def recommend(user_query):
    user_query = user_query.lower()
    results = []

    for v in vehicles:
        if "towing" in user_query and "towing" in v["features"]:
            results.append(v)
        elif "sport" in user_query or "performance" in user_query:
            if "performance" in v["features"]:
                results.append(v)

    return results[:2]