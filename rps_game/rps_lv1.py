import random
import runpy
import sys

from rps_game.rps_lv2 import main


def rock():
    print("""
     ||        ||    ||=========    ||                 ||==========      ||===========||    ||\\       /||      ||=========
     ||        ||    ||             ||                 ||                ||           ||    ||  \\    / ||      ||
     ||        ||    ||========     ||                 ||                ||           ||    ||    \\/   ||      ||======== 
     ||    /\\  ||    ||             ||                 ||                ||           ||    ||         ||      ||
     ||  /   \\ ||    ||             ||                 ||        //      ||           ||    ||         ||      ||
     ||/      \\||    ||=========    ||==========       =========//       ||===========||    ||         ||      ||=========

    """)
    print("ROCK, PAPPER, SCISSORS")
    print("LEVEL ONE")

    wins = 0
    losses = 0
    ties = 0
    lives = 5
    while True:  # The main game Loop
        print("%s Wins, %s Losses, %s Ties and %s lives" % (wins, losses, ties, lives))
        while True:  # The player input Loop
            print("Enter your move: (r)ock, (p)aper, (s)cissors or (q)uit\n")
            playerMove = input("> ")
            if playerMove == 'q':
                print("Are you sure you want to quit (y)es or (n)o")
                inp = input(">")
                if inp == 'y':
                    sys.exit()
                elif inp == 'n':
                    continue
            if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
                break  # breaks out of the loop and continues the game
            print('Type one of these r,p,s, or q')

        # Displays what the player chooses
        if playerMove == 'r':
            print("ROCK Versus...")
        elif playerMove == 'p':
            print('PAPER Versus...')
        elif playerMove == 's':
            print('SCISSORS Versus...')

        # Displays what the computer choses
        rand = random.randint(1, 3)
        if rand == 1:
            computerMove = 'r'
            print('ROCK')
        elif rand == 2:
            computerMove = 'p'
            print('PAPER')
        elif rand == 3:
            computerMove = 's'
            print('SCISSORS')

        # Calculate and displays the result
        if playerMove == computerMove:
            print("It's a tie")
            ties = ties + 1
        elif playerMove == 'r' and computerMove == 's':
            print("You Win!")
            wins = wins + 1
        elif playerMove == 'p' and computerMove == 'r':
            print('You Win!')
            wins = wins + 1
        elif playerMove == 's' and computerMove == 'p':
            print("You Win!")
            wins = wins + 1
        elif playerMove == 'r' and computerMove == 'p':
            print("You Loose!")
            losses = losses + 1
            lives = lives -1
        elif playerMove == 'p' and computerMove == 's':
            print("You Loose!")
            losses = losses + 1
            lives -= 1
        elif playerMove == 's' and computerMove == 'r':
            print("You Loose!")
            losses = losses + 1
            lives -= 1

        if ties == 20:
            print(f"GAME ENDED...\nyou have taken {ties} ties")
            sys.exit()
        if losses == 5:
            print(f'GAME ENDED...\nDo You Want To Restart (y)es or (n)o')
            inst = input()
            if inst == 'y':
                runpy._run_code(rock())
            elif inst == 'n':
                sys.exit()
        if lives == 0:
            sys.exit()
        if wins == 5:
            print("Your just finihed Level one\nDo you wish to continue level two (y)es or (n)o ===::> ")
            levels = input()
            if levels == 'n':
               continue
            elif levels == 'y':
                break
    print('Are yoou ready (y)es or (n)o?')
    level2 = input(">>")
    if level2 == 'y':
        runpy._run_code(main())


    elif level2 == 'n':
        sys.exit()


