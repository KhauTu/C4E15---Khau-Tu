# The Word Jumble Game
import random

WORDS = ["python", "jumble", "game", "word"]

word = random.choice(WORDS)

correct = word
jumble = ""

while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

# Start the game
print('''
        WELCOME TO WORD JUMBLE
        ----------------------

''')
print("The jumble is: ", jumble)

guess = input("Your guess: ")
while guess != correct and guess != "":
    print("Sorry, that's not it.")
    guess = input("Your guess: ")
if guess == correct:
    print("That's it! you guessed it")
print("Thanks for playing")
input("Press the ENTER key to exit")
