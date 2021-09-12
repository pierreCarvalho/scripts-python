import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('API_KEY_WEATHER')
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = input("Enter the city name: ")
complete_url = base_url + "appid=" + api_key + "&q=" + city_name + "&units=metric&lang=pt_br"
response = requests.get(complete_url)
x = response.json()
if x["cod"] != "404":
    y = x["main"]
    current_temperature = y["temp"]
    current_pressure = y["pressure"]
    current_humidity = y["humidity"]
    z = x["weather"]
    weather_description = z[0]["description"]
    print(f" Temperature (in celsius unit) = {str(current_temperature)} \n "+
    f"\n atmospheric pressure (in hPa unit) = {str(current_pressure)} \n"+
    f"\n atmospheric humidity (in hPa unit) = {str(current_humidity)} \n"+
    f"\n description = {str(weather_description)}") #mudar para celsius
else:
    print("City not found")