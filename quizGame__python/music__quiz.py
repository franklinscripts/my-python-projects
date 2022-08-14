import sys, runpy

score = 0



def music(guess, answer):
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
    print("""
    Do you want to continue or quit
    (y)es or (n)o
    """)
    deci = input("> ").lower()
    if deci == 'y':
        runpy._run_code(music(guess, answer))
    elif deci == 'n':
        sys.exit()




# qust8 = input("Which is the laergest animal? \n(a) Elephant\n(b) Blue Whale\n(c) Lion\n(d) Golden Eagle\n > ")
# check_answe(qust8, "b")
# qust9 = input("Which is the laergest animal? \n(a) Elephant\n(b) Blue Whale\n(c) Lion\n(d) Golden Eagle\n > ")
# check_answe(qust9, "b")
# qust10 = input("Which is the laergest animal? \n(a) Elephant\n(b) Blue Whale\n(c) Lion\n(d) Golden Eagle\n > ")
# check_answe(qust10, "b")
