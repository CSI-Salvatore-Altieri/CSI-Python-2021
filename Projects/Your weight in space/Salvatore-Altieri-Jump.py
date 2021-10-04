planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
real_gravity = [2.65, 1.11, 1, 2.64, 0.40, 0.94, 1.13, 0.88]

print("Other Earth Gravimetric Jump Length Calculator")
myJump = float(input("What is the length of your jump on earth (meters)?"))

myPlanet = input(f"Select a planet from the list: {planets}\n")
def calculateJump(planet, meters):
    print(f"Your jump in Earth is {meters}")

    planet_index = planets.index(planet)
    print(f"Your jump in {planets[planet_index]} is {(meters * real_gravity[planet_index])} meters. ")

calculateJump(myPlanet, myJump)