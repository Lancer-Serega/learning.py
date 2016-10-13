# coding: utf-8
import random
# from random import randint
from math import *
# from math import sqrt, pi
# from math import sqrt as mySqrt
import pyowm

# STL == SPL(PHP)
# PyPi - packagist(PHP)

# exit()

print(random.randint(1, 100))
print(sqrt(9))
print(pi)

### PyOWM
owm = pyowm.OWM('c7aa092ff0581594ecc23edc15fddfe9')
observation = owm.weather_at_place('Губкин, Белгородская область')
weather = observation.get_weather()
print(weather.get_temperature('celsius'))
print(weather)
