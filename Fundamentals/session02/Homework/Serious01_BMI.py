n = int(input("Your Height: ")) #import in "cm"
H = n / 100 #convert to "m"
print(H, "m")
W = int(input("Your Weight: "))
print(W, "kg")
BMI = W / (H * H)

if BMI < 16:
    print("severely underweight")
elif BMI < 18.5:
    print("underweight")
elif BMI < 25:
    print("Normal")
elif BMI < 30:
    print("Overweight")
else:
    print("Obese")
