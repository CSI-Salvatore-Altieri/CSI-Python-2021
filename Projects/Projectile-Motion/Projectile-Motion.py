import math
import os
from pathlib import Path
from ExperimentalData import ExperimentalData
import json

# gun = "Sword International Mk-18.338 LM Marksman Rifle"
# caliber = ".338"
# ammunition = "Lapua Magnum TAC-X"
# velocity_ms = 880

# building = "Shanghai World Financial Center"
# buildingHeight = 1614

# gravity_ms = 9.81

#Convert your variables into parameters

def projectileFunction(experimentalData: ExperimentalData):
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    g_ms2 = [3.7, 8.87, 9.81, 3.711, 24.79, 10.44, 8.69, 11.15]

    planet = planets.index(experimentalData.planet)

    time_s = math.sqrt((2 * experimentalData.buildingHeight) / g_ms2[planet])

    distance_m = (experimentalData.velocity_ms * time_s)
    # distance_m = (experimentalData[velocity_ms] * time_s)

    print(f"The gun selected for the expirement is the {experimentalData.gun}. The caliber of the {experimentalData.gun} is a {experimentalData.caliber} {experimentalData.ammunition}. The velocity of the bullet is {experimentalData.velocity_ms}. An i will fire from the {experimentalData.building} thats height is {experimentalData.buildingHeight} with the {experimentalData.gun} at the street to kill the CFO and his bodyguards so Shanghai financial empire will crumble")

#Convert your script parameters into a single JSON Object
# experimentalData = {

# "gun": "Sword International Mk-18.338 LM Marksman Rifle",
# "caliber": ".338",
# "ammunition": "Lapua Magnum TAC-X",
# "velocity_ms": 880,
# "building": "Shanghai World Financial Center",
# "buildingHeight": 1614,
# "gravity_ms": 9.81

# }

# experimentalData = ExperimentalData("Sword International Mk-18.338 LM Marksman Rifle", ".338", "Lapua Magnum TAC-X", 880, "Shanghai World Financial Center", 1614, 9.81)


myDataSet = [
ExperimentalData("Sword International Mk-18.338 LM Marksman Rifle", ".338", "Lapua Magnum TAC-X", 880, "Shanghai World Financial Center", 1614, "Earth"),
ExperimentalData("Sword International Mk-18.338 LM Marksman Rifle", ".338", "Lapua Magnum TAC-X", 880, "Central Park Tower", 1550, "Uranus"),
ExperimentalData("Sword International Mk-18.338 LM Marksman Rifle", ".338", "Lapua Magnum TAC-X", 880, "Petronas Twin Towers", 1483, "Neptune"),
ExperimentalData("Sword International Mk-18.338 LM Marksman Rifle", ".338", "Lapua Magnum TAC-X", 880, "KK100", 1449, "Saturn"),
ExperimentalData("Sword International Mk-18.338 LM Marksman Rifle", ".338", "Lapua Magnum TAC-X", 880, "Empire State Building", 1250, "Mars")
]

for data in myDataSet:
    print("\n-----------------------------------------------\n")
    projectileFunction(data)

#Serialization
myOutputPath = Path(__file__). parents[0]
myOutputFilePath = os.path.join(myOutputPath, 'Projectile-Motion.json')

print(myOutputFilePath)

with open(myOutputFilePath, 'w') as outfile:
    json.dump([data.__dict__ for data in myDataSet], outfile)

#Deserialization
deserialize = open(myOutputFilePath)
experimentJson = json.load(deserialize)

for e in experimentJson:
    print("n\----------------------------------------------\n")
    projectileFunction(ExperimentalData(**e))

# projectileFunction(experimentalData)