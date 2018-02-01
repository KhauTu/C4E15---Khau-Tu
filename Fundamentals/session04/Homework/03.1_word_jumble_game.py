import random
from getpass import getpass

word = getpass("python word_jumble.py")

correct = word
jumble = ""

while word:
    position = random.randrange(len(word))
    # print(position)
    jumble += word[position]
    word = word[:position] + word[(position + 1):]
    # print(jumble)
    # print(word)
print(jumble)
guess = input("Your answer: ")
while guess != correct and guess != "":
    print("Sorry :(")
    guess = input("Your answer: ")
if guess == correct:
    print("Hura")
