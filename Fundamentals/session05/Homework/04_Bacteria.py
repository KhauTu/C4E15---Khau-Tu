b = int(input("How many B bacterias are there? ")) # number of bacterias
m = int(input("How much time in minutes will we wait? ")) # time in minute, with 2 minutes each time for B to replicate itself
total = b * 2 ** (m // 2)

print("After", m, "minutes, we would have", total, "bacterias")
