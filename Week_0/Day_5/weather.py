import os 
import request 
import datetime #check la doc /!\


def weather_forecast(res):
	city = res['city']['name']
	tomorrow = str(datetime.date.today() + datetime.timedelta(days=1)) + " 06:00:00"

	for day in res['list']:
		if day.get('dt_txt', 'Not Found') == tomorrow:
			forecast = day['weather'][0]['main']

	return f"The weather {city} tomorrow is {forecast}"