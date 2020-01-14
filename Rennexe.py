from random import randint
from random import random

help = """
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


if __name__== "__main__":
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
