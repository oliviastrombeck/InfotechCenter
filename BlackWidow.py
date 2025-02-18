import random
from time import sleep


def gasLevelGauge():
    """Return a random gas level from a predefined list."""
    gasLevelList = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"]
    return random.choice(gasLevelList)  # Selects a random fuel level


def gasStations():
    """Return a random gas station name from a predefined list."""
    gasStationsList = ["Shell", "Marathon", "Speedway", "Circle K", "Wesco", "Meijer", "Buc-ees", "Costco"]
    return random.choice(gasStationsList)  # Selects a random gas station name


def milesToGasStation(gasLevelIndicator):
    """Return miles to the nearest gas station based on the current fuel level."""
    if gasLevelIndicator in ["Empty", "Low"]:  # If fuel level is Empty or Low, need a nearby station
        return round(random.uniform(1, 25), 1)  # Random distance between 1 and 25 miles
    elif gasLevelIndicator == "Quarter Tank":  # If fuel level is a Quarter Tank, need a station within 50 miles
        return round(random.uniform(25.1, 50), 1)  # Random distance between 25.1 and 50 miles
    return 0  # No need to display distance for higher fuel levels like Half, Three Quarter, or Full Tank


def gasLevelAlert():
    """Generate a gas level alert based on current gas level and distance to the nearest station."""
    gasLevelIndicator = gasLevelGauge()  # Get a random fuel level
    station = gasStations()  # Get a random gas station
    miles = milesToGasStation(gasLevelIndicator)  # Get the distance to the nearest gas station

    print("\n************************************************\n")
    print("Gasoline Branch - Developer: Olivia Strombeck")

    sleep(0.5)  # Brief sleep to simulate time for the title display

    # Checking fuel levels and printing appropriate alerts
    if gasLevelIndicator == "Empty":  # Out of gas condition
        print("****** WARNING - YOU ARE OUT OF GAS ******\n")
        sleep(1)  # Simulate time taken to call for help
        print("Calling AAA")  # Simulate calling roadside assistance
    elif gasLevelIndicator == "Low":  # Low fuel warning
        print(f"\nYour gas tank is really low, checking GPS for closest gas station.\n")
        sleep(1)  # Simulate time for GPS check
        print(f"The closest gas station is {station} which is {miles} miles away.")  # Show station and distance
    elif gasLevelIndicator == "Quarter Tank":  # Quarter tank warning
        print(f"\nYour gas tank is at a Quarter Tank, checking GPS for closest gas station.\n")
        sleep(1)  # Simulate time for GPS check
        print(f"The closest gas station is {station} which is {miles} miles away.")  # Show station and distance
    elif gasLevelIndicator == "Half Tank":  # Half tank is sufficient
        print("\nYour gas tank is half full, which is plenty to get to your destination!\n")
    elif gasLevelIndicator == "Three Quarter Tank":  # Three-quarters full
        print("\nYour gas tank is three-quarters full!\n")
    else:  # Full tank
        print("\nYour gas tank is FULL.\n")


# Call the gas level alert function to run the program
gasLevelAlert()
