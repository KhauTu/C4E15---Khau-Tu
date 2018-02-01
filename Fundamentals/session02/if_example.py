yob = int(input("Your year of birth? "))
age = 2018 - yob
print("Your age: ", age)

if age < 10:
    print("Baby")
elif age < 18:
    marriage = input("working or school? ")
    if marriage == "school":
        print("Pupil")
    else:
        print("Teen labor")
else:
    print("Adult")
