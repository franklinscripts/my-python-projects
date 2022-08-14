import random
secretNum = random.randint(1,100)
print("==================\n I am thinking of a number between 1 to 100 \n===================")
for i in range(1,11):
    print("============\n Take a guess\n============")
    guesss = int(input())
    if guesss < secretNum:
        print("Too low")
    elif guesss > secretNum:
        print("Too high")
    else:
        break
if guesss == secretNum:
    print(f"You guessed my number and took {i} guesses ")
else:
    print(f"Nope, the number I was thinking was {secretNum}")