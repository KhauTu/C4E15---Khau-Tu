from random import randint

x = randint(0, 100)
print("The Mood score: ", x)

if x < 30:
    print('''(\(\\
( – -)
((‘) (’)
''')
elif x < 60:
    print('''(\ /)
(•.•)
c(")(“) ''')
else:
    print('''(\__/) ||
(•ㅅ•) ||
/ 　 づ  ''')
