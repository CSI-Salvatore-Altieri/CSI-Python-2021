import math
from ExperimentalData import ExperimentalData
# gun = "Sword International Mk-18.338 LM Marksman Rifle"
# caliber = ".338"
# ammunition = "Lapua Magnum TAC-X"
# velocity_ms = 880

# building = "Shanghai World Financial Center"
# buildingHeight = 1614

# gravity_ms = 9.81

# import math

# time_s = math.sqrt((2 * BuildingHeight) / gravity_ms)

def ProjectileFunction(experimentalData: ExperimentalData):

    time_s = math.sqrt((2 * experimentalData.buildingHeight) / experimentalData.gravity_ms)

    distance_m = (experimentalData.velocity_ms * time_s)
    # distance_m = (experimentalData[velocity_ms] * time_s)

    print(f"The gun selected for the expirement is the {experimentalData.gun}. The caliber of the {experimentalData.gun} is a {experimentalData.caliber} {experimentalData.ammunition}. The velocity of the bullet is {experimentalData.velocity_ms}. An i will fire from the {experimentalData.building} thats height is {experimentalData.buildingHeight} with the {experimentalData.gun} at the street to kill the CFO and his bodyguards so Shanghai financial empire will crumble")
    
# experimentalData = {

# "gun": "Sword International Mk-18.338 LM Marksman Rifle",
# "caliber": ".338",
# "ammunition": "Lapua Magnum TAC-X",
# "velocity_ms": 880,
# "building": "Shanghai World Financial Center",
# "buildingHeight": 1614,
# "gravity_ms": 9.81

# }

experimentalData = ExperimentalData("Sword International Mk-18.338 LM Marksman Rifle", ".338", "Lapua Magnum TAC-X", 880, "Shanghai World Financial Center", 1614, 9.81)

ProjectileFunction