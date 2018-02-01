import random
print("python word_jumble.py")
wordlist = ["meticulous", "champion", "hexagon"]
word = random.choice(wordlist)

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
