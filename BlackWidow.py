print ("\n************************************************\n")
print ("Gasoline Branch - Developer: Olivia Strombeck")

import random
from time import sleep

def gasLevelGauge():
    gasLevelList = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"]
    return random.choice(gasLevelList)

def gasStations():
    gasStationsList = ["Shell", "Marathon", "Speedway", "Circle K", "Wesco", "Meijer", "Buc-ees", "Costco"]
    return random.choice (gasStationsList)

def gasLevelAlert():
    milesToGasStationLow = round(random.uniform(1,25),1)
    milesToGasStationQuarterTank = round(random.uniform(25.1,50), 1)
    gasLevelIndicator = gasLevelGauge()
    if gasLevelIndicator == "Empty":
        print("******wARNING - YOU ARE OUT OF GAS******\n")
        sleep(1)
        print("Calling AAA")
    elif gasLevelIndicator == "Low":
        print("Your gas tank is really low, checking GPS for closest gas station.")
        sleep(1)
        print("The closest gas station is", gasStations(), "which is", milesToGasStationLow, "miles away.")
    elif gasLevelIndicator == "Quarter Tank":
        print("Your gas tank is on a Quarter Tank, checking GPS for closest gas station.")
        sleep(1)
        print("The closest gas station is", gasStations(), "which is", milesToGasStationQuarterTank, "miles away.")
    elif gasLevelIndicator == "Half Tank":
        print("Your gas tank is on a Half of a Tank, which is plenty to get to your destination!")
    elif gasLevelIndicator == "Three Quarter Tank":
        print("Your gas tank is Three Quarter of a Tank full!")
    else:
        print("Your gas tank is FULL.")

gasLevelAlert()
