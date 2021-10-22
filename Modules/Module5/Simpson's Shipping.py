print("Welcome to Simpson's Shipping")
weight:float = float(input("What is the weight of your package:"))

#Ground Shipping
if(weight == 2 or weight < 2):
    cost_ground = weight * 1.75 + 20.00
    print("Ground Shipping: $", float(cost_ground))
elif(weight > 2 or weight <= 6):
    cost_ground = weight * 3.50 + 20.00
    print("Ground Shipping: $", float(cost_ground))
elif(weight > 6 or weight <= 10):
    cost_ground = weight * 4.50 + 20.00
    print("Ground Shipping: $", float(cost_ground))
else:
    cost_ground = weight * 5.25 + 20.00
    print("Ground Shipping: $", float(cost_ground))

#Courier Shipping
if(weight == 2 or weight < 2):
    cost_ground = weight * 3.50 + 5.00
    print("Courier Shipping: $", float(cost_ground))
elif(weight > 2 or weight <= 6):
    cost_ground = weight * 7.00 + 8.00
    print("Courier Shipping: $", float(cost_ground))
elif(weight > 6 or weight <= 10):
    cost_ground = weight * 9.00 + 12.00
    print("Courier Shipping: $", float(cost_ground))
else:
    cost_ground = weight * 10.50 + 15.00
    print("Courier Shipping: $", float(cost_ground))

#Drone Shipping
if(weight == 2 or weight < 2):
    cost_ground = weight * 5.25 + 0.00
    print("Courier Shipping: $", float(cost_ground))
elif(weight > 2 or weight <= 6):
    cost_ground = weight * 10.50 + 0.00
    print("Courier Shipping: $", float(cost_ground))
elif(weight > 6 or weight <= 10):
    cost_ground = weight * 13.50 + 0.00
    print("Courier Shipping: $", float(cost_ground))
else:
    cost_ground = weight * 15.75 + 0.00
    print("Courier Shipping: $", float(cost_ground))

print("Ground Shipping Premium Charge $150")