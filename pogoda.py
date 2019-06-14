#pogoda

import pyowm
import datetime
import time

owm = pyowm.OWM('7215c81c62b322b41e0aa0eb1843c5d4', language = 'ru') 

place = 'Sochi'#input('Введите город : ')

observation = owm.weather_at_place(place)
w = observation.get_weather()

temp = w.get_temperature('celsius')['temp']
speed = w.get_wind()['speed']
humidity = w.get_humidity()
city_time = w.get_reference_time()

print( 'Температура в городе ' + place + ' сейчас ' + str( temp ) + ' цельсия' )
print('Влажность воздуха ' + str( humidity ) + "%")  
print( 'Скорость ветра в городе ' + place + ' сейчас ' + str( speed ) + " м/с" )
print( 'На небе ' + w.get_detailed_status() )
print(w)
print( time.ctime( city_time ) )


# Weather details
#w.get_wind()                  # {'speed': 4.6, 'deg': 330}
#w.get_humidity()              # 87
#w.get_temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}



# Search current weather observations in the surroundings of
# lat=22.57W, lon=43.12S (Rio de Janeiro, BR)
#observation_list = owm.weather_around_coords(-22.57, -43.12)

#


