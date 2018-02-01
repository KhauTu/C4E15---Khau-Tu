from getpass import getpass
print("Hello to the world of CODE!")

i = 0

while i < 3:
    n = input("Username: ")
    x = getpass("Password: ")
    if n == "KhauTu":
        if x == "Tahy":
            print("successfully login!")
        else:
            print("Wrong password!")
    else:
        print("Username not valid!")
    i += 1
print("You're failed to log in 3 times")
