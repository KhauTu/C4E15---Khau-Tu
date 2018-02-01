string = '''ThiS is String with Upper and lower case Letters'''
alphabet = 'abcdefghijklmnopqrstuvwxyz'
stringtext = string.lower()

letter_count= {}

for letter in stringtext:
    letter_count[letter] = letter_count.get(letter, 0) + 1
for i in alphabet:
    if i in letter_count:
        print (i, letter_count[i])
