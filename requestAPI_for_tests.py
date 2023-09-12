import requests
import dotenv
import os


dotenv.load_dotenv("api.env")
api_key = str(os.getenv("api_key"))

user_input = input("cidade: ")

weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}&lang=pt_br")

weather = weather_data.json()

print(weather)