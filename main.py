#!/usr/bin/python3 

import requests

API_Key = "ecb11ad2c188b060940c9bd7bcfde144"

town = input("Enter town in New Zealand here: ")
Base_url = "http://api.openweathermap.org/data/2.5/weather"

# Creating the full URL
request_url = f"{Base_url}?appid={API_Key}&q={town}"

get_weather = requests.get(request_url)

# extract information
if get_weather.status_code == 200:
  data = get_weather.json()
  weather_unscripted = data
  print(weather_unscripted)
