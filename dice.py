"""
Dice rolling game. Asks the user to roll a die and displays the result. Gives them the option to roll again or quit
"""
#Import the random module
import random

#Define the main function 

def main():
    #Ask the user if they want to roll a die
    print("Welcome to the Dice Rolling Game!")
    roll = input("Do you want to roll a die? (y/n) ")
    
    if roll.lower() == "y":
            running = True
    elif roll.lower() == "n":
            running = False
            print("Thanks for playing!")


    while running:
        #Generate a random number between 1 and 6
            result = random.randint(1, 6)
        #Display the result
            print("You rolled a", result)
        #Ask the user if they want to roll again
            roll = input("Do you want to roll again? (y/n) ")
            if roll.lower() == "n":
                running = False
            elif roll.lower() == "y":
                continue
    else:
        print("Thanks for playing!")

#Call the main function
main()




