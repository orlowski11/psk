def middle_square(seed):
    s = str(seed ** 2)
    while len(s) != 8:
        s = "0" + s
    seed = int(s[2:6])
    return seed

def von_neumann(seed,iteration):
    random_numbers = [seed]
    for i in range(0,iteration):
        seed = middle_square(seed)
        random_numbers.append(seed)

    return random_numbers