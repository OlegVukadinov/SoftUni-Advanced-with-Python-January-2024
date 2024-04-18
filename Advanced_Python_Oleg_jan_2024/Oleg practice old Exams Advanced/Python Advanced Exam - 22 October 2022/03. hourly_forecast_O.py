def  forecast(*weather_info):
    # location_name = weather_info[0] - Appear runtime error
    # weather = weather_info[1]
    weather_dict = {}
    for data in weather_info:
        if data[0] not in weather_dict:
            weather_dict[data[0]] = data[1]
    # for location_name, weather in weather_info:  - Appear runtime error
    #     if location_name not in weather_dict:
    #         weather_dict[location_name] = weather

    sunny = ""
    cloudy = ""
    rainy = ""
    sorted_locations = sorted(weather_dict.items(), key=lambda x: (x[0], x[-1]))
    for location, weather in sorted_locations:
        if weather == "Sunny":
            sunny += (f"{location} - {weather}\n")
        if weather == "Cloudy":
            cloudy += (f"{location} - {weather}\n")
        if weather == "Rainy":
            rainy += (f"{location} - {weather}\n")

    return sunny + cloudy + rainy


print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))

print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))

print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))

