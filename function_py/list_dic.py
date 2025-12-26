data = []

n = int(input("Enter number of days: "))

for i in range(n):
    date = input("Enter date (YYYY-MM-DD): ")
    temp = int(input("Enter temperature: "))
    rain = int(input("Enter rainfall: "))

    day_data = {
        "date": date,
        "temp": temp,
        "rain": rain
    }

    data.append(day_data)

print(data)
