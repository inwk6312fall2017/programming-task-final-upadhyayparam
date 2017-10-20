from builtins import print
from weather import Weather
weather = Weather()

loc = input ("Enter the location":)
location = weather.lookup_by_location('halifax')
condition = location.condition()
print ("The current weayher is "+ (condition['text'])
