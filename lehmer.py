def generate_random_numbers(x0, a, m, n):
    random_numbers = [x0]

    for _ in range(1, n):
        xn = (a * random_numbers[-1]) % m
        random_numbers.append(xn)

    return random_numbers