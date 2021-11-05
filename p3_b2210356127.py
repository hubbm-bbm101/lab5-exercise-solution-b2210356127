import random
number=random.randint(1,100)
while True:
    guess=int(input("enter a number between 1 and 100 please: "))
    if guess<number:
        print("increase your number and guess again please")
    elif guess>number:
        print("decrease your number and guess again please")
    else:
        print("You got it! Well done!")
        break