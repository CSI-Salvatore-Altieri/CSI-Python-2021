print("Welcome to Bad Bunny P KFN R")
print("The cost of each seat is as follow: Arena Standing = $125, Reserved Seating 1 = $50, Reserved Seating 2 = $40, Reserved Seating 3 = $30")

Arena_Standing = int(input("How many tickets where sold for Arena Standing"))
Reserved_Seating_1 = int(input("How many tickets where sold for Reserved Seating 1"))
Reserved_Seating_2 = int(input("How many tickets where sold for Reserved Seating 2"))
Reserved_Seating_3 = int(input("How many tickets where sold for Reserved Seating 3"))

def SectionsSales(Arena_Standing, Reserved_Seating_1, Reserved_Seating_2, Reserved_Seating_3):
    print(f"The cost for Arena Standing is: {int(Arena_Standing) * 125}")
    print(f"The cost for reserved Seating 1 is: {int(Reserved_Seating_1) * 50}")
    print(f"The cost for Reserved Seating 2 is: {int(Reserved_Seating_2) * 40}")
    print(f"The cost for Reserved Seating 3 is: {int(Reserved_Seating_3) * 30}")
print()
SectionsSales(Arena_Standing, Reserved_Seating_1, Reserved_Seating_2, Reserved_Seating_3)
Sales_AS = Arena_Standing * 125
Sales_RS1 = Reserved_Seating_1 * 50
Sales_RS2 = Reserved_Seating_2 * 40
Sales_RS3 = Reserved_Seating_3 * 30
def TicketsTotal(Sales_AS, Sales_RS1, Sales_RS2, Sales_RS3):
    print(f"The total of ticket sales is: ${int(Sales_AS) + int(Sales_RS1) + int(Sales_RS2) + int(Sales_RS3)}")
print()
TicketsTotal(Sales_AS, Sales_RS1, Sales_RS2, Sales_RS3)