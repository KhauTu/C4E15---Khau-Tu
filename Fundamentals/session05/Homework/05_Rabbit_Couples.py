total = [1, 1]

m = 7 # numbers of month

for k, v in enumerate(total):
    if k < m:
        x = total[k] + total[k + 1]
        total.append(x)
        n = k - 1
        if n < 0:
            pass
        else:
            print("Month", n,":", total[k], "pair(s) of rabbit")
    else:
        break

# print(total)
