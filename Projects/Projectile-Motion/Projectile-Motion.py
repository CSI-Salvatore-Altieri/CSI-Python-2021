# gun = "Sword International Mk-18.338 LM Marksman Rifle"
# caliber = ".338"
# ammunition = "Lapua Magnum TAC-X"
# velocity_ms = 880

# Building = "Shanghai World Financial Center"
# BuildingHeight = 1614

# gravity_ms = 9.81

# import math

# time_s = math.sqrt((2 * BuildingHeight) / gravity_ms)

import math
def ProjectileFunction(gun:str, caliber:str, ammunition:str, velocity_ms: int, Building:str, BuildingHeight: int, gravity_ms: int):
    time_s = math.sqrt((2 * BuildingHeight) / gravity_ms)
    distance_m = (velocity_ms * time_s)

    print(f"The gun selected for the expirement is the {gun}. The caliber of the {gun} is a {caliber} {ammunition}. The velocity of the bullet is {velocity_ms}. An i will fire from the {Building} thats height is {BuildingHeight} with the {gun} at the street to kill the CFO and his bodyguards so Shanghai financial empire will crumble")
    
ProjectileFunction("Sword International Mk-18.338 LM Marksman Rifle", ".338", "Lapua Magnum TAC-X", 880, "Shanghai World Financial Center", 1614, 9.81)