"""Creat a simple number gussing game
The user get 10 chances to guess a number
If the user guesses the numebr wuithin 10 chances , stop the game and sey congrats
if the user cant guess the number within 10 times .. print you r out of chances and end the game"""

print("Welcome to the number gussing game.You have 10 chances.")
print("Predicted number is within 1 to 100")

secret_number=88
num=1
chances=10
is_guess_correct=False

while num<=10:
    user_number=int(input("Enter your predicted number:"))
    print("You have",chances,"chances left")
    num+=1
    chances-=1
    if user_number==secret_number:
        print("Congrats!! You guessed the right number")
        is_guess_correct==True
        break
    else:
        if user_number<secret_number:
            higher_lower="Try higher"
        else:
            higher_lower="Try lower"
        print(higher_lower,",Good luck")
   

if is_guess_correct==False:
    print("Bad luck, You have exhausted all you chances")
    
        