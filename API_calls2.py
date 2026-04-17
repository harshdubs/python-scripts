import requests

api_key = 'b1c64d9e67d126c84c7dcdb7d12f2019'
city_name = input("Enter city name:")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"

try:    
    response = requests.get(url)

    data = response.json()

    print(response.status_code)
    
    if response.status_code == 200:
        print(city_name)
        print(f"Temperature : {data['main']['temp']}")
        print(f"Weather : {data['weather'][0]['description']}")
        print(f"Humidity : {data['main']['humidity']}")
    else:
        exit()

except requests.exceptions.ConnectionError:
    print("Network error - check your connection")

