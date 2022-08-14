from music__quiz import music
from animal__quiz import check_answer
from  rps_game.rps_lv1 import rock

import runpy
print("""
 ||        ||    ||=========    ||                 ||==========      ||===========||    ||\\       /||      ||=========
 ||        ||    ||             ||                 ||                ||           ||    ||  \\    / ||      ||
 ||        ||    ||========     ||                 ||                ||           ||    ||    \\/   ||      ||======== 
 ||    /\\  ||    ||             ||                 ||                ||           ||    ||         ||      ||
 ||  /   \\ ||    ||             ||                 ||        //      ||           ||    ||         ||      ||
 ||/      \\||    ||=========    ||==========       =========//       ||===========||    ||         ||      ||=========

""")
print("""
    help --- For more info about the game 
    Choose your categories of game
""")

def select():
    info = input("> ").lower()
    if info == 'help':
        print("""
        You have quizzes and fun games to play with my collection
        General Studies --> Type (gs)
        Programming Quiz --> Type (p)
        Sports Quiz --> Type (sq)
        Music Quiz --> Type (mq)
        Animal Quiz --> Type (aq)
        Rock Paper Scissors --> Type (rps)
        """)
        inf = input("> ").lower()
        if inf == 'mq':
            qust1 = input("Which animal lives at the North Pole?\n(a) Polar bear\n(b) bear\n(c) Lion\n(d) Mammals\n > ")
            music(qust1, "a")
            qust2 = input("Which is the fastest animal?\n(a) Usain bolt\n(b) Dolphin\n(c) Cheetah\n(d) Python\n > ")
            music(qust2, "c")
            qust3 = input("Which is the largest animal? \n(a) Elephant\n(b) Blue Whale\n(c) Lion\n(d) Golden Eagle\n > ")
            music(qust3, "b")
            qust4 = input("Which is animal has many heart? \n(a) Octopus\n(b) Blue Whale\n(c) Frog\n(d) Chicken\n > ")
            music(qust4, "a")
            qust5 = input("What animal takes an hour climbing Trees? \n(a) Slut\n(b) Tortoise\n(c) Monkey\n(d) Bat\n > ")
            music(qust5, "b")
            qust6 = input("Which animal has long trunk? \n(a) Giraffe\n(b) Whale\n(c) Elephant\n(d) Duck\n > ")
            music(qust6, "c")
            qust7 = input("What kind of mammal can fly? \n(a) Man\n(b) Blue Whale\n(c) Lion\n(d) Bat\n > ")
            music(qust7, "d")
        elif inf == 'aq':
            qust1 = input("Which animal lives at the North Pole?\n(a) Polar bear\n(b) bear\n(c) Lion\n(d) Mammals\n > ")
            check_answer(qust1, "a")
            qust2 = input("Which is the fastest animal?\n(a) Usain bolt\n(b) Dolphin\n(c) Cheetah\n(d) Python\n > ")
            check_answer(qust2, "c")
            qust3 = input("Which is the largest animal? \n(a) Elephant\n(b) Blue Whale\n(c) Lion\n(d) Golden Eagle\n > ")
            check_answer(qust3, "b")
            qust4 = input("Which is animal has many heart? \n(a) Octopus\n(b) Blue Whale\n(c) Frog\n(d) Chicken\n > ")
            check_answer(qust4, "a")
            qust5 = input("What animal takes an hour climbing Trees? \n(a) Slut\n(b) Tortoise\n(c) Monkey\n(d) Bat\n > ")
            check_answer(qust5, "b")
            qust6 = input("Which animal has long trunk? \n(a) Giraffe\n(b) Whale\n(c) Elephant\n(d) Duck\n > ")
            check_answer(qust6, "c")
            qust7 = input("What kind of mammal can fly? \n(a) Man\n(b) Blue Whale\n(c) Lion\n(d) Bat\n > ")
            check_answer(qust7, "d")

        elif inf == 'rps':
            runpy._run_code(rock())

    else:
        print("Type a valid command")
        runpy._run_code(select())


select()