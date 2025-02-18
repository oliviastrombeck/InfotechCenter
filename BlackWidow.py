import random
from time import sleep


def gasLevelGauge():
    """Return a random gas level from a predefined list."""
    gasLevelList = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"]
    return random.choice(gasLevelList)


def gasStations():
    """Return a random gas station name from a predefined list."""
    gasStationsList = ["Shell", "Marathon", "Speedway", "Circle K", "Wesco", "Meijer", "Buc-ees", "Costco"]
    return random.choice(gasStationsList)


def milesToGasStation(gasLevelIndicator):
    """Return miles to nearest gas station based on the current fuel level."""
    if gasLevelIndicator in ["Empty", "Low"]:
        return round(random.uniform(1, 25), 1)
    elif gasLevelIndicator == "Quarter Tank":
        return round(random.uniform(25.1, 50), 1)
    return 0  # No need for miles for higher fuel levels


def gasLevelAlert():
    """Generate a gas level alert based on current gas level and distance to station."""
    gasLevelIndicator = gasLevelGauge()
    station = gasStations()
    miles = milesToGasStation(gasLevelIndicator)

    print("\n************************************************\n")
    print("Gasoline Branch - Developer: Olivia Strombeck")

    sleep(0.5)  # Sleep just once for the title display

    if gasLevelIndicator == "Empty":
        print("****** WARNING - YOU ARE OUT OF GAS ******\n")
        sleep(1)
        print("Calling AAA")
    elif gasLevelIndicator == "Low":
        print(f"\nYour gas tank is really low, checking GPS for closest gas station.\n")
        sleep(1)
        print(f"The closest gas station is {station} which is {miles} miles away.")
    elif gasLevelIndicator == "Quarter Tank":
        print(f"\nYour gas tank is at a Quarter Tank, checking GPS for closest gas station.\n")
        sleep(1)
        print(f"The closest gas station is {station} which is {miles} miles away.")
    elif gasLevelIndicator == "Half Tank":
        print("\nYour gas tank is half full, which is plenty to get to your destination!\n")
    elif gasLevelIndicator == "Three Quarter Tank":
        print("\nYour gas tank is three-quarters full!\n")
    else:  # Full Tank
        print("\nYour gas tank is FULL.\n")


gasLevelAlert()