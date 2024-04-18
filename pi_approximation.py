def calculate_pi(n, random_numbers):
    inside_circle = 0
    for i in range(0, n, 2):
        x = random_numbers[i]
        y = random_numbers[i + 1]
        if x * x + y * y <= 1:
            inside_circle += 1
    pi_approximation = 4 * inside_circle / (n / 2)
    return pi_approximation


def offset(value):
    return round((abs(value - 3.141592)) / 3.141592 * 100, 2)
