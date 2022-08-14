import sys, runpy

score = 0



def check_answer(guess, answer):
    print("""
     ||        ||    ||=========    ||                 ||==========      ||===========||    ||\\       /||      ||=========
     ||        ||    ||             ||                 ||                ||           ||    ||  \\    / ||      ||
     ||        ||    ||========     ||                 ||                ||           ||    ||    \\/   ||      ||======== 
     ||    /\\  ||    ||             ||                 ||                ||           ||    ||         ||      ||
     ||  /   \\ ||    ||             ||                 ||        //      ||           ||    ||         ||      ||
     ||/      \\||    ||=========    ||==========       =========//       ||===========||    ||         ||      ||=========

    """)
    print("Guess the Animal")
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:


        if guess.lower() == answer.lower():
            score = score + 3 - attempt
            still_guessing = False
            print(f"Correct! You just earned {score} point")
        else:
            if attempt < 2:
                guess = input("Sorry, Please try again. > ")
            attempt += 1
        if guess == None:
            print("""
                   DO YOU WISH TO CONTINUE
                   (Y)es OR (N)o
                   """)
            decision = input("> ")
            if decision.lower() == 'y':
                continue
            elif decision.lower() == 'n':
                sys.exit()

    if attempt == 3:
        print(f"The answer was {answer}")





# qust1 = input("Which animal lives at the North Pole?\n(a) Polar bear\n(b) bear\n(c) Lion\n(d) Mammals\n > ")
# check_answer(qust1, "a")
# qust2 = input("Which is the fastest animal?\n(a) Usain bolt\n(b) Dolphin\n(c) Cheetah\n(d) Python\n > ")
# check_answer(qust2, "c")
# qust3 = input("Which is the largest animal? \n(a) Elephant\n(b) Blue Whale\n(c) Lion\n(d) Golden Eagle\n > ")
# check_answer(qust3, "b")
# qust4 = input("Which is animal has many heart? \n(a) Octopus\n(b) Blue Whale\n(c) Frog\n(d) Chicken\n > ")
# check_answer(qust4, "a")
# qust5 = input("What animal takes an hour climbing Trees? \n(a) Slut\n(b) Tortoise\n(c) Monkey\n(d) Bat\n > ")
# check_answer(qust5, "b")
# qust6 = input("Which animal has long trunk? \n(a) Giraffe\n(b) Whale\n(c) Elephant\n(d) Duck\n > ")
# check_answer(qust6, "c")
# qust7 = input("What kind of mammal can fly? \n(a) Man\n(b) Blue Whale\n(c) Lion\n(d) Bat\n > ")
# check_answer(qust7, "d")
# qust8 = input("Which is the laergest animal? \n(a) Elephant\n(b) Blue Whale\n(c) Lion\n(d) Golden Eagle\n > ")
# check_answe(qust8, "b")
# qust9 = input("Which is the laergest animal? \n(a) Elephant\n(b) Blue Whale\n(c) Lion\n(d) Golden Eagle\n > ")
# check_answe(qust9, "b")
# qust10 = input("Which is the laergest animal? \n(a) Elephant\n(b) Blue Whale\n(c) Lion\n(d) Golden Eagle\n > ")
# check_answe(qust10, "b")
