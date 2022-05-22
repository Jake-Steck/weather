import geocoder # geocoder is a module that lets you get the lat and lon of a location
import requests # requests is a module that lets you make a request to a url
import math as m # math is a module that lets you do math, in this case it is used for its trunc() function


location = input('\nEnter your desired location: ') 
g = geocoder.location(location) # holds the coordinates of the location entered
apiKey = 'your key here' # api key for openweathermap.org
lat = g.lat # holds the lat of the location you entered
lon = g.lng # holds the lon of the location you entered

url = f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=imperial&appid={apiKey}'

response = requests.get(url) # makes a request to the url

# print(f'\n{response.json()}') # prints json response

high_weather = m.trunc(response.json()['main']['temp_max'])
low_weather = m.trunc(response.json()['main']['temp_min'])
current_weather = m.trunc(response.json()["main"]["temp"])

print(
    f'\nLow: {low_weather}°F\nHigh: {high_weather}°F\nCurrent: {current_weather}°F\n')
