name = input("What is your Name?")
print(f"Hello {name}! and Welcome to the Magic 8-Ball were dreams either die or come to life")
question = input("What do you want to ask me, the mighty 8-Ball!!!")
print(f"{name} asks: {question}")

import random

random_number = random.randint(1, 12)
if (random_number == 1):
    print("Yes - Definitely")
elif (random_number == 2):
    print("Its Decidedly So")
elif (random_number == 3):
    print("Without a Doubt")
elif (random_number == 4):
    print("Hell Yea")
elif (random_number == 5):
    print("Reply Hazy, Try Again")
elif (random_number == 6):
    print("Ask Again Later")
elif (random_number == 7):
    print("Better Not Tell You Now")
elif (random_number == 8):
    print("I Don't Know, Come Back Later")
elif (random_number == 9):
    print("My Sources Say No")
elif (random_number == 10):
    print("Outlook Not So Good")
elif (random_number == 11):
    print("Very Doubtful")
elif (random_number == 12):
    print("Hell No")
else: 
    print("There was an error, pls try again")