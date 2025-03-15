# Ask the user to guess the random word from a list filled with computer-related words, the user is given the length of of the word, and is then prompted to guess which
# letters, the user has 3 fewer guesses than there are letters in the word with a minimum of 3

#TODO: Import random module
import random 
#TODO: Define a list of possible words to be chosen at random.
word_options = ["programmer", "code", "processor", "network", "graphics", "memory", "motherboard", "software", "hardware", "storage"]

#TODO: Define the main game loop
#while True:

#TODO: have the program choose a random word, get its length, and print out a out that number through a series of "_"
random_word = random.choice(word_options)
random_word_length = len(random_word)
#TODO: Define a counter for the number of guesses the player has left based on the number of letters in the randomly chosen word
if random_word_length >= 6:
    num_of_guesses = random_word_length - 3
else:
    num_of_guesses = 3
print(f"You have {num_of_guesses} lives. Use them wisely.")
#TODO: print the number of blank lines equal to the count of characters in the randomly chosen word.
blank_lines = "_ " * random_word_length
print(blank_lines)

print("\n")

#TODO: Prompt the user to input a letter, to learn basic error-handling, see if you can impliment a try=except block to validate that the letter is a valid input
user_guess = input("Enter a letter and press enter: ")
user_guess_lower = user_guess.lower()
valid_guesses = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

if user_guess_lower in valid_guesses:
    if user_guess in random_word:
#TODO: If the letter exists within the random word, the coresponding empty "_" should be replaced with that letter. i.e. if the word in question is "code" if the letter "o" is guessed, the output should be "_o__" and so on
        random_word_index = random_word.index(user_guess)
        
#TODO: Propmt the user to guess until the word is complete, or they run out of lives


