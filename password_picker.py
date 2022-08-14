import random, string

print("""
 ||        ||    ||=========    ||                 ||==========      ||===========||    ||\\       /||      ||=========
 ||        ||    ||             ||                 ||                ||           ||    ||  \\    / ||      ||
 ||        ||    ||========     ||                 ||                ||           ||    ||    \\/   ||      ||======== 
 ||    /\\  ||    ||             ||                 ||                ||           ||    ||         ||      ||
 ||  /   \\ ||    ||             ||                 ||        //      ||           ||    ||         ||      ||
 ||/      \\||    ||=========    ||==========       =========//       ||===========||    ||         ||      ||=========

""")
adjectives = [
    'sleepy','slow','smally',
    'wet','fat','red','orange',
    'blue','purple','fluffy',
    'white','proud','brave','dark','moon'
]
nouns = [
    'apple','dinosuar','goat',
    'dragon','baby','panda',
    'hammer','duck','toaster',
    'ball','kid','mum','boy','girl'
]
color = ['blue','red','orange','green','purple','pink','yellow','black','white']
print("This is a Random Password Picker Program")

while True:
    for num in range(3):

        adjective = random.choice(adjectives)
        noun = random.choice(nouns)
        number = random.randrange(0, 1000)
        punctuation = random.choice(string.punctuation)
        col = random.choice(color)

        password = adjective + punctuation + noun + str(number) + col
        print(f"This is your new password ===> {password}")

    print('Do you want another password? Type y or n')
    response = input('> ').lower()
    if response == 'n':
        break
    elif response == 'y':
        continue

    else:
        print("Type in a correct command")
        break