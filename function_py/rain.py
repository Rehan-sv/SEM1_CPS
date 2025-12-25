def avg_temp(data):
    total = 0
    for d in data:
        total += d["temp"]
    return total / len(data)

def most_rain(data):
    max_rain = 0
    day = ""
    for d in data:
        if d["rain"] > max_rain:
            max_rain = d["rain"]
            day = d["date"]
    return day
