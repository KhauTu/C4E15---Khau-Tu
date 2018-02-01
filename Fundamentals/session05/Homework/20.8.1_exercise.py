sentence = "ThiS is String with Upper and lower case Letters"
wds = sentence.split()
abc_order = "".join(wds)
letter_counts = {}

for letter in abc_order.lower():
    letter_counts[letter] = letter_counts.get(letter, 0) + 1
letter_items = list(letter_counts.items())
letter_items.sort()

for k, v in enumerate(letter_items):
    print(letter_items[k][0], letter_items[k][1])
