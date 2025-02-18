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

weatherAlert = weather()

def vehicleResponseSystem():
    if weatherAlert == "snowing":
        print("\nThe National Weather Service has Updated your alarm by 30 minutes because"
        " it is", weatherAlert, "outside.")
    elif weatherAlert == "blizzard":
        print("\nThe National Weather Service has updated your alarm by 60 minutes because"
              " it is a", weatherAlert, "outside!")
    elif weatherAlert == "icy":
        print("\nThe National Weather Service has updated your alarm by 90 minutes because"
              " it is", weatherAlert, "outside!")

vehicleResponseSystem()