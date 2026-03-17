import requests
from database import create_table, insert_weather, show_data

API_KEY = "8b999ddc3ae58aa1439e1ddd765ee10b"

create_table()

city = input("Enter city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()

print(data)   # This will show the real error from the API

if response.status_code == 200:

    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]

    print("\nCity:", city)
    print("Temperature:", temp, "°C")
    print("Humidity:", humidity, "%")

    insert_weather(city, temp, humidity)

else:
    print("Weather data not received")

print("\nDatabase data:")
show_data()