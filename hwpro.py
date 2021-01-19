number=6
guess=int(input("Guess a number between 1 to 10"))
if(guess==number):
    print("You Guessed The Right Number")
elif(guess>number):
    print("Try a bit lower number")
    guess=int(input("Guess a number between 1 to 10"))
else :
    print("Try a bit higher number")
    guess=int(input("Guess a number between 1 to 10"))
    
    