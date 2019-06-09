from gnewsclient import gnewsclient
from database import update_records
import os,requests,json

client = gnewsclient.NewsClient(max_results=3)


def get_news(parameters,session_id):
	top = parameters.get('news_type')
	loc = parameters.get('geo-country')
	client.topic, client.location, temp = update_records(session_id, top, loc, '')
	return client.get_news()

def get_weather(parameters,session_id):
	city = parameters.get('geo-city')
	t1, t2, city = update_records(session_id, '', '', city)
	url1 = 'https://www.metaweather.com/api/location/search/?query='+city
	response = requests.get(url1)
	data = json.loads(response.content.decode('utf-8'))
	url2 = 'https://www.metaweather.com/api/location/{}/'.format(data[0]['woeid'])
	response = requests.get(url2)
	data = json.loads(response.content.decode('utf-8'))
	wea = data['consolidated_weather'][0]
	str = "Here is your weather report for {}.".format(city)
	str += "\nThe weather is '{}'. \nCurrent temp : {}°C\nMinimum temp : {}°C\nMaximum temp : {}°C. \n\nThe air pressure is {} mbar, with the humidity being {}% and the visibility being {} miles.".format(wea['weather_state_name'], round(wea['the_temp'],1), round(wea['min_temp'],1), round(wea['max_temp'],1), round(wea['air_pressure'],1), round(wea['humidity'],1), round(wea['visibility'],1))
	img_url = "https://www.metaweather.com/static/img/weather/png/{}.png".format(wea['weather_state_abbr'])
	return (str,img_url)
