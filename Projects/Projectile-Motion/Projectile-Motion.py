gun = "Sword International Mk-18.338 LM Marksman Rifle"
caliber = ".338"
ammunition = "Lapua Magnum TAC-X"
velocity_ms = 880

Building = "Shanghai World Financial Center"
BuildingHeight = 1614

gravity_ms = 9.81

import math

time_s = math.sqrt((2 * BuildingHeight) / gravity_ms)

print(f"The gun selected for the expirement is the {gun}. The caliber of the {gun} is a {caliber} {ammunition}. The velocity of the bullet is {velocity_ms}. An i will fire from the {Building} thats height is {BuildingHeight} with the {gun} at the street to kill the CFO and his bodyguards so Shanghai financial empire will crumble")