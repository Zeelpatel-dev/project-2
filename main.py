import requests
import json

api_key = "aa61b4d76fb385b24fd90d4daa38f0f6"
city = input('Enter the city name: ')
url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

response = requests.get(url)
data = json.loads(response.text)

if 'message' in data and data['message'] == 'city not found':
    print("error:"+" "+"City not found")
else:
    temperature_kelvin = data['main']['temp']
    temperature_celsius = temperature_kelvin - 273.15
    print(f"The temperature in {city} is {temperature_celsius:.2f}\u00B0C")
