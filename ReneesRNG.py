from random import randint
from random import random

help = """There are 7 scenarios of the program.

1. The first scenario is the most simple one. It will ask you for a range in which it'll generate random numbers for you, and the quantity of numbers you want (i.e. "1 100 5" for 5 numbers from 1 to 100). It's your own private random number generator!

2. Next you have a scenario in which you can randomly generate success or failure for a set percentage of success. (I.e. typing in "75" will give you 75% chance of success - and the program will only print out if you were successful.)

3. Third scenario is very similar to the previous one, but it might be more useful for the application you showed me one time - if you have a set number of places in a tournament and only the first n places are successful.
If you type in "20 5", it will place you on a random of 20 places, and print out your success or failure and a place you got.

4. The next scenario enables the advantage! If you want a pony to get a bonus in its next tournament, use this scenario. The program will first ask you for the advantage in this round, and then will proceed to the third scenario (so you'd type in "10" first to give the pony 10 places of advantage, and then "20 5" to specify the places it can get). Negative numbers give the pony disadvantage!

5. It's a twist on a success/failure scenario: this one is your pseudo-magic 8-ball! It'll ask you for two options, one by one, and will pick one of them randomly.

6. Another 8-ball scenario, this time you can feed it more options! Write them all in one line, without using enter key - divide the options by "|" sign. The program will choose a random answer out of them.

7. This is an evolution of scenario four: it will allow you to generate results of a few tournaments in a row. It will ask you for an advantage first - and it will use it for all the tournaments (except for the first one!). Then it will proceed to ask for a tournament details ("20 5" for 20 places, 5 of them get advantage in the next round).
The difference between this scenario and #4 is that it will save the result of the previous tournament and determine if the pony gets an advantage in the next round. It will last until you quit the scenario.
"""

def scenario_one():
    proceed = 1
    while proceed:

        message = input("Choose a range and a quantity. / [from] [to] [quantity] / q for quit\n")

        if message is 'q':
            proceed = 0
            break

        args = message.split()
        if len(args) is not 3:
            print("Wrong input!")
            break

        try:
            for i in range(len(args)):
                args[i] = int(args[i])
        except ValueError:
            #Handle the exception
            print('Please enter numbers.')
            break

        response = ""

        for elem in range(args[2]):
            value = randint(args[0], args[1])
            response = response + str(value) + ", "
        response = response[:-2]

        print("Your numbers:")
        print(response)
        print("\n")

def scenario_two():
    proceed = 1
    while proceed:
        message = input("Choose a success rate. / [number from 0 to 100] / q for quit\n")

        if message is 'q':
            proceed = 0
            break

        try:
            rate = int(message) / 100
        except ValueError:
            print('Please enter a number.')
            break

        if random() > rate:
            print("Failure...\n")
        else:
            print("Success!\n")

def scenario_three():
    proceed = 1
    while proceed:
        message = input("Choose a number of places and the awarded places. / [places] [awarded places] / q for quit\n")

        if message is 'q':
            proceed = 0
            break

        args = message.split()
        if len(args) is not 2:
            print("Wrong input!")
            break

        try:
            for i in range(len(args)):
                args[i] = int(args[i])
        except ValueError:
            print('Please enter numbers.')
            break

        value = randint(1, args[0])

        if value <= args[1]:
            print(f"Success! You placed {value} out of {args[0]}.\n")
        else:
            print(f"You placed {value} out of {args[0]} - better luck next time.\n")

def scenario_four():
    proceed = 1
    advantage = 0

    while proceed:
        message = input("Choose an advantage (in number of places). / [advantage] / q for quit\n")

        if message is 'q':
            proceed = 0
            break

        try:
            advantage = int(message)
        except ValueError:
            print('Please enter a number.')
            break

        message = input("Choose a number of places and the awarded places. / [places] [awarded places] / q for quit\n")

        if message is 'q':
            proceed2 = 0
            break

        args = message.split()
        if len(args) is not 2:
            print("Wrong input!")
            break

        try:
            for i in range(len(args)):
                args[i] = int(args[i])
        except ValueError:
            print('Please enter numbers.')
            break

        value = randint(1, args[0])
        
        value -= advantage
        if value < 1: value = 1
        elif value > args[0]: value = args[0]

        if value <= args[1]:
            print(f"Success! You placed {value} out of {args[0]}.\n")
        else:
            print(f"You placed {value} out of {args[0]} - better luck next time.\n")

def scenario_five():
    proceed = 1
    while proceed:
        message = input("Choose the first option. / [option - can have multiple words] / q for quit\n")

        if message is 'q':
            proceed = 0
            break

        option1 = message

        message = input("Choose the second option. / [option - can have multiple words] / q for quit\n")

        if message is 'q':
            proceed = 0
            break

        option2 = message

        print("Your answer:")
        if random() >= 0.5:
            print(option1)
        else:
            print(option2)
        print("\n")

def scenario_six():
    proceed = 1
    while proceed:
        message = input("Choose your options, divided by a |. / [option1 | option2 | ...] / q for quit\n")

        if message is 'q':
            proceed = 0
            break

        options = message.split("|")
        chosen = randint(1, len(options))

        print("Your answer:")
        print(options[chosen-1].lsplit() + "\n")

def scenario_seven():
    proceed = 1
    proceed2 = 1
    advantage = 0
    if_advantage = False

    while proceed:
        message = input("Choose an advantage (in number of places). / [advantage] / q for quit\n")

        if message is 'q':
            proceed = 0
            proceed2 = 0
            break

        try:
            advantage = int(message)
        except ValueError:
            print('Please enter a number.')
            break

        proceed = 0

    while proceed2:
        message = input("Choose a number of places and the awarded places. / [places] [awarded places] / q for quit\n")

        if message is 'q':
            proceed2 = 0
            break

        args = message.split()
        if len(args) is not 2:
            print("Wrong input!")
            break

        try:
            for i in range(len(args)):
                args[i] = int(args[i])
        except ValueError:
            print('Please enter numbers.')
            break

        value = randint(1, args[0])
        
        if if_advantage is True: #advantage is included only if you won last time
            value -= advantage
            if value < 1:
                value = 1
            elif value > args[0]:
                value = args[0]

        if value <= args[1]:
            print(f"Success! You placed {value} out of {args[0]}.\n")
        else:
            print(f"You placed {value} out of {args[0]} - better luck next time.\n")


if __name__ == "__main__":
    print("Welcome!")
    repetition = 1

    while repetition:

        choice = input("""Choose a scenario to start.
1. Random number generator
2. Success or failure
3. Place in the tournament
4. Tournament with an advantage
5. One of the two
6. Help me choose
7. Multiple tournaments
h. [Help]
q. [Quit program]
Choose a number and press 'enter'.
""")

        if choice is '1':
            scenario_one()
        elif choice is '2':
            scenario_two()
        elif choice is '3':
            scenario_three()
        elif choice is '4':
            scenario_four()
        elif choice is '5':
            scenario_five()
        elif choice is '6':
            scenario_six()
        elif choice is '7':
            scenario_seven()

        elif choice is 'q':
            repetition = 0
        elif choice is 'h':
            print(help)
        else:
            print("Choose again, and choose wisely!")

        if repetition is 0:
            print("This message will autodestruct in 3... 2... 1...")
