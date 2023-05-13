import random

print("Welcome to the World's Greatest Dice Roller")
print("-------------------------------------------")

print("How many dice would you like to roll?")
###Validate input
while True:
    try:
        numberPicked=int (input("Type an integer between 1 and 6: "))
        if(numberPicked > 0 and numberPicked < 7):
            break
        else:
            print("Invaild input. Try again")
    except:
        print("Please provide an integer")

def rollDice(amountOfDice):
    possibleFaces=[1,2,3,4,5,6]
    for die in range(amountOfDice):
        roll=random.choice(possibleFaces)
        print("Die ", die + 1, ": ", roll)


rollDice(numberPicked)