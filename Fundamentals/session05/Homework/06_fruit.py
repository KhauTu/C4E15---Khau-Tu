prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

total = 0
for key, value in prices.items():
    print()
    print(key)
    print("price:", value)
    if key in stock:
        print("stock:", stock[key])
        x = prices[key] * stock[key]
        print(x)
        total = total + x
print(total)


# print(list(prices.values()))
# print(list(stock.values()))
# print(list(prices.keys()))
