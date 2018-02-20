def get_even_list(l):
    # new_l = []
    # for k in l:
    #     if k % 2 == 0:
    #         new_l.append(k)
    #     else:
    #         pass
    # return new_l
    new_l = [k for k in l if k % 2 == 0] # list comprehension
    return new_l

l = [1, 4, 5, -1, 10, -3, -1]

new_l = get_even_list(l)

print(new_l)
