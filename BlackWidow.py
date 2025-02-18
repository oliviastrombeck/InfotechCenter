# print a decorative header
print("\n********************************************\n")

print("Weather Branch - Developer: Olivia Strombeck\n")

#Import necessary libraries
import random  # used to randomly select weather conditions
from time import sleep # Imported but not used in the code

# Function to determine the weather condition
def weather():
    # List of possible weather conditions
    weatherForecastList = ["snowing", "blizzard", "icy", "rainy", "windy", "sunny"]
    # Randomly select one condition from the list
    weatherCondition = random.choice(weatherForecastList)
    return weatherCondition

# Get the current weather alert
weatherAlert = weather()

# Function to adjust alarm based on weather conditions
def vehicleResponseSystem():
    if weatherAlert == "snowing":
        print("\nThe National Weather Service has Updated your alarm by 30 minutes because"
        " it is", weatherAlert, "outside!")
        sleep(1)
        print("VRS has been engaged only allowing us to drive 55MPH.")
    elif weatherAlert == "blizzard":
        print("\nThe National Weather Service has updated your alarm by 60 minutes because"
              " it is a", weatherAlert, "outside!")
        sleep(1)
        print("VRS has been engaged only allowing us to drive 45MPH.")
    elif weatherAlert == "icy":
        print("\nThe National Weather Service has updated your alarm by 90 minutes because"
              " it is", weatherAlert, "outside!")
        sleep(1)
        print("VRS has been engaged only allowing us to drive 35MPH.")
        elif weatherAlert == "rainy":
        print("\nThe National Weather Service has updated your alarm by 10 minutes because"
              " it is", weatherAlert, "outside!")
        sleep(1)
        print("VRS has been engaged only allowing us to drive 65MPH.")
    elif weatherAlert == "windy":
        print("\nThe National Weather Service has updated your alarm by 5 minutes because"
              " it is", weatherAlert, "outside!")
        sleep(1)
        print("VRS has been engaged only allowing us to drive 70MPH.")
    # If the weather is sunny, no alarm adjustment is needed
    else:
        print("\nThe National Weather Service is calling for", weatherAlert, "skys outside, drive safe!")
        sleep(1)
        print("VRS has been disengaged, drive safe!")
        
# Call the function to display the appropriate message
vehicleResponseSystem()