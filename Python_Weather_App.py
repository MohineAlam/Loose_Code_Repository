import requests
import os
from dotenv import load_dotenv
import tkinter as tk

# function to retrieve weather information for city using API
def get_weather():
	# city input
	city_name = city_entry.get()
	# api key - retrieve key
	load_dotenv()
	api_key = os.getenv("API_KEY")
	base_url = "https://api.openweathermap.org/data/2.5/weather"
	params = {
		"q": city_name,
		"appid": api_key,
		"units": "metric"
		}

	# retrieve data from API
	response = requests.get(base_url,params)

	# check if response file is in json format
#	if response.headers['Content-Type'].startswith('application/json'):
#		print("in JSON response.")
#	else:
#		print("not a JSON response.")

	# print data
	if response.status_code == 200:
			# convert json response into python dictionary/list
			data = response.json()
			# retrieve data
			city = data['name']
			country = data['sys']['country']
			temperature = data['main']['temp']
			condition = data['weather'][0]['description'].capitalize()
			humidity = data['main']['humidity']
			wind_speed = data['wind']['speed']
			# print as label in gui
			results_label.config(text = f"Weather in {city}, {country}\nTemperature: {temperature}*C\nCondition: {condition}\nHumidity: {humidity}%\nWind Speed: {wind_speed} m/s")
			# print to terminal as well
			print(f"Weather in {data['name']}, {data['sys']['country']}")
			print(f"	Temperature: {data['main']['temp']}*C")
			print(f"	Condition: {data['weather'][0]['description'].capitalize()}")
			print(f"	Humidity: {data['main']['humidity']}%")
			print(f"	Wind Speed: {data['wind']['speed']} m/s")

	# if there is an error
	else:
		print("Failed to retrieve weather data:", response.json().get('message','Unknown error'))

# message to user
print("Find out the weather of the city you want.")

# GUI
root = tk.Tk()
root.title("Weather App")

# city input
tk.Label(root, text="Enter city name").pack(pady=5)
city_entry = tk.Entry(root)
city_entry.pack(pady=5)

# call function with button
tk.Button(root, text="Retrieve Weather info", command=get_weather).pack(pady=10)

# print results in label
results_label = tk.Label(root, text="", font=("Helvetica", 14))
results_label.pack(pady=20)

# call gui
root.mainloop()
