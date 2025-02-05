print("\n********************************************\n")

print("Weather Branch - Developer: Olivia Strombeck\n")

#Import Libraries Here!
import random
from time import sleep

#Weather Function to determine the Weather
def weather():
    weatherForecastList = ["snowing", "blizzard", "icy", "rainy", "windy", "sunny"]
    weatherCondition = random.choice(weatherForecastList)
    return weatherCondition

print (weather())