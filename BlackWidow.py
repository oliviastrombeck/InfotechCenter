# Import necessary libraries
import sys  # sys module provides access to system-specific parameters and functions
import time  # time module allows time-related functions such as sleep
import random  # used to randomly select weather conditions
from time import sleep  # Imported but not used in the code

# ANSI Escape Sequences for Colors
RESET = "\033[0m"  # Reset color to default, to ensure colors don't bleed into the next text
GREEN = "\033[32m"  # ANSI escape code for green text
CYAN = "\033[36m"  # ANSI escape code for cyan text
YELLOW = "\033[33m"  # ANSI escape code for yellow text

# Display a welcome message with developer's name in green
# The green color will be applied to this message using ANSI escape sequence
print(GREEN + "\nWelcome Branch - Developer: Olivia Strombeck" + RESET)

# Display the software version message in cyan
# This message is displayed in cyan to give it a distinct, informative look
print(CYAN + "\nWelcome to InfoTechCenter V1.0\n" + RESET)

# Initialize variables
x = 0  # Variable for counting loop iterations, simulating the booting process
ellipsis = 0  # Variable to control the number of periods in the booting message

# Loop to simulate system boot process
while x != 20:  # The loop runs 20 times to simulate the system boot process
    x += 1  # Increment the loop counter by 1 with each iteration to track the boot progress
    message = ("Infotech Center System Booting" + "." * ellipsis)  # Create the message with increasing ellipses for a loading effect
    ellipsis += 1  # Increase the number of periods (dots) in the message to simulate progress
    sys.stdout.write("\r" + YELLOW + message + RESET)  # Overwrite the current line with a new booting message in yellow
    time.sleep(1)  # Pause for 1 second before displaying the next booting message
    if ellipsis == 4:  # Once the number of periods reaches 4, reset the ellipsis count to restart the pattern
        ellipsis = 0  # Reset the ellipsis counter
    if x == 20:  # After 20 iterations, the booting process is complete
        # Display the final success message in green, indicating the system has successfully booted
        print(GREEN + "\n\nOperating System Booted Up - Retina Scanned - Access Granted\n" + RESET)


# print a decorative header
print("\n********************************************\n")
print("Weather Branch - Developer: Olivia Strombeck")


# Function to determine the weather condition
def weather():
    # List of possible weather conditions
    weatherForecastList = ["snowing", "blizzard", "icy", "rainy", "windy", "sunny"]
    # Randomly select one condition from the list
    return random.choice(weatherForecastList)

# Weather condition to response mappings
weather_responses = {
    "snowing": {"time": 30, "speed": 55},
    "blizzard": {"time": 60, "speed": 45},
    "icy": {"time": 90, "speed": 35},
    "rainy": {"time": 10, "speed": 65},
    "windy": {"time": 5, "speed": 70},
    "sunny": {"time": 0, "speed": None},
}

# Get the current weather alert
weatherAlert = weather()

# Function to adjust alarm based on weather conditions
def vehicleResponseSystem():
    response = weather_responses.get(weatherAlert)

    # If the weather is sunny, no alarm adjustment is needed
    if response:
        if weatherAlert == "sunny":
            print(f"\nThe National Weather Service is calling for {weatherAlert} skies outside.")
            print("VRS has been disengaged, drive safe!")
        else:
            print(f"\nThe National Weather Service has updated your alarm by {response['time']} minutes because"
                  f" it is {weatherAlert} outside!")
            print(f"VRS has been engaged only allowing us to drive {response['speed']}MPH.")
    sleep(1)

# Call the function to display the appropriate message
vehicleResponseSystem()



