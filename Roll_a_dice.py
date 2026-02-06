 #Roll a dice:
 
import random
print("Welcome to the dice game! ")
 
while True:
    choice=input("press 'ENTER' to start the game and press 'q' to quit")
    if choice=="q":
        print("Thanks")
        break
    elif choice=="":
        roll=random.randint(1,6)
        print("Your number is:",roll)
    else:
        print("You have entered invalid input")
     