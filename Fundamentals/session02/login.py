from getpass import getpass
print("Hello to the world of CODE!")
n = input("Username: ")
x = getpass("Password: ")
if n == "KhauTu":
    if x == "Tahy":
        print("successfully login!")
    else:
        print("Wrong password!")
else:
    print("Username not valid!")
