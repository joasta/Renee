from random import randint
from random import random

#This scenario is a random number generator - from a given range and for a given quantity of numbers.
def scenario_one():
    #notice that there is an indent in front of the line now - indents mean that we're getting deeper!
    #we are now inside a function scenario_one - we take a step inside a block of code, we get an indent

    proceed = 1 #we set a variable proceed - as long as it's equal to 1, the scenario will be repeated on and on
    #(a useful thing about Python - we don't need to say what is the type of the variable; is it a number? is it text?
    #doesn't matter, it will figure it out on its own)
    
    while proceed: #this is called a loop - the block of code inside will be repeated as long as proceed is non-zero
        #we take a step inside the loop - we get enother indent

        #this line will do two thing: print the message for the user with instructions, and get input from the user
        message = input("Choose a range and a quantity. / [from] [to] [quantity] / q for quit\n")
        #notice that the message is in quotation marks - it means it's text that it mostly won't try to understand
        #it ends with "\n" - this is important! \n means a new line, and it's one of the few things inside "" that
        #the program will understand

        #now, what the user wrote is inside "message", let's see if the user wanted to quit the scenario
        if message is 'q':
            proceed = 0 #here we make sure the loop won't be repeated again
            break #break ends a current repetition of a loop, so nothing below will be executed - a new repetition
            #will start from the beginning of the loop
        
        #and now the indentation's gone - we're out of the if-condition

        args = message.split() #variable.split() will divide text into words, cutting at white spaces, it will give us a list
        #of words: [word1, word2, word3 etc.] - useful! now we can refer to the whole list of words by one name, args.

        #len(something) is a useful function - we can check the length of pretty much everything. length of a list -> number
        #of its elements. length of a word -> number of letters.
        if len(args) is not 3: #so if the user gave us too few or too many words...
            print("Wrong input!") #...we will warn them! "print" means "show the user"
            break #and start the loop from the beginning, giving him one more chance to input correct message

        try: #"see if you can do that:" in short - for now bear with me, explanation later
            for i in range(len(args)): #it will go through all numbers in the range, and the range starts
                #                       from 0 to length_of_the_list_minus_one
                #                       why minus one? we start counting words from one: one, two three
                #                       but the computer starts from 0! zero, one, two - so if we have three elements,
                #                       the comupter will start from zero and count to three-minus-one

                args[i] = int(args[i]) #up to this point, the words were text - and for calculations, we'll need numbers
                #so we say that this variable (word_0, word_1 etc.) needs to have a number ('integer') that was written as text

        #but what if the word wasn't a number at all? what if the user wrote "asdfgg" by accident?
        #normally we'd get an error and the program would crash - but we want it to react to a mistake instead, not crush!
        #that's why we had "try:" and now we have "except"
        except ValueError: #so if the word wasn't a number:
            print('Please enter numbers.') #ask the user to pay attention
            break #and start the loop again from the top

        #this is a final message for the user - we will need to add contents to it
        response = ""

        for elem in range(args[2]): #again - it goes through all the numbers from zero to the third number given by the user - 1,
            #                       and repeat the instructions inside the for-loop until it runs out of numbers
            
            value = randint(args[0], args[1]+1) #randint is another nifty function - it will give us a natural number from a range
            #from the first number given by the user to the second one. mind the +1!
            #i.e. randint(1,10) will give us a random number from 1 to 9 (the second argument is excluded)

            response = response + str(value) + ", " #now the response should have what it had by now (response), but now it gets
            #new content too - a number (translated from a number to text - text is called 'string' in coding) and a separator ","
        
        #if we add a comma after every number, we have a comma after the last number - that's not very aesthetic
        #so we subtract last two signs from our message:
        response = response[:-2]

        #now we show the user what we have!
        print("Your numbers:") #we can print text
        print(response) #or a variable
        print("\n") #and we add a separate line for clarity

#how do we know we're done with the scenario? all the indentation's gone, we're back to the beginning of the line

#This scenario randomly gives you success or failure, with a set success rate
def scenario_two():
    proceed = 1
    while proceed: #the loop should look familiar! it's the same as it was in scenario_one - and most of the code is, too
        message = input("Choose a success rate. / [number from 0 to 100] / q for quit\n")

        if message is 'q':
            proceed = 0
            break

        #we don't split the message into words here - we should only get one word containing a number...
        try:
            rate = int(message) / 100
        except ValueError:
            print('Please enter a number.')
            break #...and if not, we'll patently start the loop again
        #dividing by 100 converts a percentage to a fraction, and now we will refer to that fraction as 'rate'

        #random() gives us a random fraction between 0 and 1
        if random() > rate: #if the random fraction is higher than our success cut-off, it's not successful
            print("Failure...\n")
        else: #else is a follow-up to if: you can't use "else" on its own, it always is the alternative in case 'if' isn't true
            print("Success!\n")

#This scenario generates one place out of the available ones and says if you got an award.
def scenario_three():
    proceed = 1
    while proceed:
        message = input("Choose a number of places and the awarded places. / [places] [awarded places] / q for quit\n")

        if message is 'q':
            proceed = 0
            break

        args = message.split()
        if len(args) is not 2: #now we have only two expected words - places & awarded places
            print("Wrong input!")
            break

        try:
            for i in range(len(args)):
                args[i] = int(args[i])
        except ValueError:
            print('Please enter numbers.')
            break

        rank = randint(1, args[0]+1)
        #we know all the code here, don't we? it's all repeated from the previous scenarios!
        #rank is a random natural number from 1 (first place) to the first word given by the user (places available)

        if rank <= args[1]: #if the rank is among the awarded places:
            print(f"Success! You placed {value} out of {args[0]}.\n") #a new way of printing things - mind the f before "!
            #it means that we will mix text and other variables, i.e. numbers. then, inside the text, we have {variables} - 
            #the program is smart and will insert values of the variables in there

        else: #the alternative
            print(f"You placed {value} out of {args[0]} - better luck next time.\n")

#This scenario does the same as the previous one - but includes advantage of a set number of places.
def scenario_four():
    proceed = 1

    while proceed:
        message = input("Choose an advantage (in number of places). / [advantage] / q for quit\n")

        if message is 'q':
            proceed = 0
            break

        try:
            advantage = int(message) #we save the value under the name 'advantage'
        except ValueError:
            print('Please enter a number.')
            break

        #look! here we repeat the part of the code to ask the user for another thing.
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

        value = randint(1, args[0]+1)
        
        #the next three lines of code are what's new here: we adjust the random number by our advantage 
        value -= advantage #minus - because we want a higher place (of a lower #)
        if value < 1: #we shouldn't get a place -3, should we? if we got the first place, advantage will not get us any higher
            value = 1
        elif value > args[0]: #same for the disadvantage - we can't get a place further than the number of places available
            value = args[0]
        #have you noticed 'elif' instead of 'else'? it's an if that wil only be considered when the first if isn't true.
        #it's different from 'else' in that it won't always be executed, only if another condition was fulfilled
        #it's used to "stack" if-s, you'll see a good example later

        if value <= args[1]:
            print(f"Success! You placed {value} out of {args[0]}.\n")
        else:
            print(f"You placed {value} out of {args[0]} - better luck next time.\n")

#This scenario helps you decide between the two things.
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
        if random() >= 0.5: #again, random() gives us a random fraction from 0 to 1, there's equal probability that it'll be
            #               lower or higher than half.
            print(option1)
        else:
            print(option2)
        print("\n")

#This scenario is a magic 8-ball: give it options to choose from, it'll choose one.
def scenario_six():
    proceed = 1
    while proceed:
        message = input("Choose your options, divided by a |. / [option1 | option2 | ...] / q for quit\n")

        if message is 'q':
            proceed = 0
            break

        options = message.split("|") #remember the .split() thing? it can be modified - if you put a symbol inside the brackets
        #and in "", it'll use the symbol instead of white spaces to find the places to cut

        chosen = randint(1, len(options)+1) #choose one of the options

        print("Your answer:")
        print(options[chosen-1].lsplit() + "\n") #thing.lsplit() removed white spaces from the beginning of the text,
        #here: for aesthetics purposes

#Similar to scenario #4, but remembers how high is the advantage and if you got it the last round
def scenario_seven():
    proceed = 1
    proceed2 = 1 #a second 'proceed'! there will be two loops in this scenario, we need independent proceeds for that
    advantage = 0 
    #a new variable - we will save a new information in it, it's value will be saved for all the repetitions of the loop
    if_advantage = False
    #new type of a variable! it can be True or False, and it will tell us if we got awarded in the previous round

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

        proceed = 0 #if it successfully gets here - without hitting a break first - we're done with this loop,
        #the advantage is set

    #and this loop is already familiar!
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

        value = randint(1, args[0]+1)
        
        if if_advantage is True: #advantage is included only if you won last time
            value -= advantage
            if value < 1:
                value = 1
            elif value > args[0]:
                value = args[0]

        if value <= args[1]:
            print(f"Success! You placed {value} out of {args[0]}.\n")
            if_advantage = True #set the advantage
        else:
            print(f"You placed {value} out of {args[0]} - better luck next time.\n")
            if_advantage = False #set the advantage

#brilliant, now we have all the scenarios! but... how does the computer know what to do when we start the program?
#where is the menu? how do we choose scenarios?

#the next line means: if this file is opened as a program, treat this function as a main, executable function
#main function is what the computer looks for to run a program
#can this file be used not as a program? yes, but it's more complicated
#if __name__== "__main__":
#    print("Welcome!") #this line will show up just once when we run the code

#    repetition = 1 #oh? could it be...? a while loop?

#    while repetition: #ya bet!

#        choice = input("""Choose a scenario to start.
#1. Random number generator
#2. Success or failure
#3. Place in the tournament
#4. Tournament with an advantage
#5. One of the two
#6. Help me choose
#7. Multiple tournaments
#q. [Quit program]
#Choose a number and press 'enter'.
#""") #you should recognise 'input' by now - it shows a message and gets input from the user, saving the input in 'choice'

#        #Here we have stacked if-s, like I mentioned before! the profit of stacking them instead of writing independent if-s
#        #is that once it finds an if that is true, it won't check the rest of them. which tracks - if choice is '1', it surely
#        #isn't equal '2' at the same time!
#        if choice is '1':
#            scenario_one() #this is how we tell the computer: remember that def scenario_one()? run it now
#            #important: order matters. you can't tell the computer to run a function that is below this line of code.
#            #it hasn't read the code below yet, it cannot remember and recall it
#        elif choice is '2':
#            scenario_two()
#        elif choice is '3':
#            scenario_three()
#        elif choice is '4':
#            scenario_four()
#        elif choice is '5':
#            scenario_five()
#        elif choice is '6':
#            scenario_six()
#        elif choice is '7':
#            scenario_seven()

#        elif choice is 'q':
#            repetition = 0 #don't repeat the loop again
#        else:
#            print("Choose again, and choose wisely!")
#            #the stack of if-s ends with a catch-everything-else 'else'

#        if repetition is 0:
#            print("This message will autodestruct in 3... 2... 1...")
#            #that's what gets printed before the program ends, as we know that repetition is 0, the loop won't repeat again
