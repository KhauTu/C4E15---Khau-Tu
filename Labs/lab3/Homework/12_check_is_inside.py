def is_inside(P, r):
    area_r = r[2] * r[3] # S(ABCD)
# P = (P[0], P[1])
# A = (r[0], r[1])
# B = (r[0] + r[2], r[1])
# C = (r[0] + r[2], r[1] + r[3])
# D = (r[0], r[1] + r[3])
# vector PA = (r[0] - P[0], r[1] - P[1])
# vector PB = (r[0] + r[2] - P[0], r[1] - P[1])
# vector PC = (r[0] + r[2] - P[0], r[1] + r[3] - P[1])
# vector PD = (r[0] - P[0], r[1] + r[3]- P[1])
    area_PAB = 0.5 * abs((r[0] - P[0]) * (r[1] - P[1]) - (r[1] - P[1]) * (r[0] + r[2] - P[0]))
    area_PBC = 0.5 * abs((r[0] + r[2] - P[0]) * (r[1] + r[3] - P[1]) - (r[1] - P[1]) * (r[0] + r[2] - P[0]))
    area_PCD = 0.5 * abs((r[0] + r[2] - P[0]) * (r[1] + r[3] - P[1]) - (r[1] + r[3] - P[1]) * (r[0] - P[0]))
    area_PDA = 0.5 * abs((r[0] - P[0]) * (r[1] + r[3] - P[1]) - (r[1] - P[1]) * (r[0] - P[0]))

    return area_r == (area_PAB + area_PBC + area_PCD + area_PDA)
if is_inside([100, 120], [140, 60, 100, 200]) == False and is_inside([200, 120], [140, 60, 100, 200]) == True:
    print("Your function is correct")
else:
    print("Oops, bugs detected")
