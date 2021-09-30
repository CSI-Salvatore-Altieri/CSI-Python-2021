planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
g_ms2 = [3.7, 8.87, 9.81, 3.711, 24.79, 10.44, 8.69, 11.15]

print("Different Planet Human Weight Calculator")
myWeight = int(input("What is your wight (pounds)?"))

myPlanet = input(f"Select a planet from the list: {planets}\n")
def calculateWeight(planet, mass):
    print(f"Earth mass in pounds is: {mass}")

    w_kg = mass / 2.2046
    print(f"Mass in kg: {w_kg}")

    n_lb = 4.45

    planet_index = planets.index(planet)
    print(f"Your weight in {planets[planet_index]} is {(w_kg * g_ms2[planet_index]) / n_lb} lb. ")

calculateWeight(myPlanet, myWeight)