from builtins import print
from weather import Weather
weather = Weather()

loc = input ("Enter the location":)
location = weather.lookup_by_location('halifax')
condition = location.condition()
print ("The current weayher is "+ (condition['text'])

a =[]
i=0

for forecasts in location.forecast():
    if i<5:
    b = []
    b.append(forecast['text']
    b.append(forecast['date'])
    b.append(forecast['high'])
    b.append(forecast['low'])
    i+=1
    a.append(b)
print (a)
max = 0

for lists in a
    if int(lists[2] > max:
	max = int(lists[2])
	s = lists[1]
print(s)




