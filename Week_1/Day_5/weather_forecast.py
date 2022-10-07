def weather_forecast(city):
    date_tomorrow =str(datetime.date.today() + datetime.timedelta(days=1)) + " 06:00:00"
    city_name = city.get('city').get('name')
    predictions = city.get('list')
    
    for i in range(0, len(predictions)):
        date = predictions[i].get('dt_txt')
        if date_tomorrow == date:
            forecast = predictions[i].get('weather')[0].get('main')
            
    return f"The weather in {city_name.title()} tomorrow is {forecast.title()}"
