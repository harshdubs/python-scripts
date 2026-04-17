import requests


latitude = float(input("Enter latitude :")) 
longitude = float(input("Enter longitude :"))

url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"

try:
    response = requests.get(url)
    print(response.status_code)

    data = response.json()

    current_temp = data["current_weather"]["temperature"]
    current_windspeed = data["current_weather"]["windspeed"]

    if(current_temp > 35):
        print(f"Too hot, stay indoors")
    elif(current_temp > 25 and current_temp < 35):
        print(f"Decent Weather")
    else:
        print("Cool day")

    if(data["current_weather"]["is_day"]!= 0):
        print("Its day")
    else:
        print("its night")
   


except requests.exceptions.ConnectionError :
    print("Network error - check your connection")