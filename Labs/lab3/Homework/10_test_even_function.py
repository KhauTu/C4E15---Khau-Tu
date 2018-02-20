def get_even_list(l):
    new_l = []
    for k in l:
        if k % 2 == 0:
            new_l.append(k)
        else:
            pass
    return new_l

even_list = get_even_list([1, 2, 5, -10, 9, 6])

if set(even_list) == set([2, -10, 6]): # set is an unordered data structure, meaning set of (1, 2,3) equals set of (3, 1, 2)
    print("Your function is correct")
else:
    print("Ooops, bugs detected")
