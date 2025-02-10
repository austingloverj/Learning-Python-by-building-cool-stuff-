"""
Ask the user to guess a number between 1 and 100. If they guess correctly, display a congratulatory message. If they guess incorrectly, display a message indicating whether their guess was too high or too low. Give the user the option to play again.
"""
#import random module
import random

#Define the main function
def main():
    #Welcome the user
    print("Welcome to the Number Guessing Game!")
    
    running = True

    while running:
        #Generate a random number between 1 and 100
        number = random.randint(1,100)
        user_guess = int(input("Guess a number between 1 and 100: "))
        #Check if the user's guess is correct
        if user_guess == number:
            print("Congratulations! You guessed the number!")
        elif user_guess < number:
            print("Your guess is too low. The number was", number)
        elif user_guess > number:
            print("Your guess is too high. The number was", number)
        else:
            print("Invalid input. Please enter a number between 1 and 100.")
        #Ask the user if they want to play again
        play_again = input("Do you want to play again? (y/n) ")
        if play_again.lower() == "y":
            continue
        elif play_again.lower() == "n":
            running = False
            print("Thanks for playing!")
        else:
            print("Invalid input. Please enter y or n.")


#Call the main function
main()