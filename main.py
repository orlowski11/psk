import matplotlib.pyplot as plt
import von_neumann
import lehmer

if __name__ == '__main__':

    x0 = 0.2
    a = 32345
    m = 121
    n = 60

    random_numbers = lehmer.generate_random_numbers(x0, a, m, n)
    print("Wygenerowane liczby losowe:", random_numbers)
    avg = sum(random_numbers) / n / 100
    print("Średnia:", avg)

    max_size = len(random_numbers)
    last_index = max_size - 1
    x = random_numbers[1:last_index]
    y = random_numbers[0:last_index - 1]

    plt.plot(x, y, color='green', linestyle='none', linewidth=3,
             marker='o', markerfacecolor='blue', markersize=12)
    plt.show()

    seed = 1211
    n = 30

    random_numbers = von_neumann.von_neumann(seed, n)
    print("Wygenerowane liczby losowe:", random_numbers)
    avg = sum(random_numbers)/ n / 10000
    print("Średnia:", avg)

    max_size = len(random_numbers)
    last_index = max_size - 1
    x = random_numbers[1:last_index]
    y = random_numbers[0:last_index-1]

    plt.plot(x, y, color='green', linestyle='none', linewidth=3,
             marker='o', markerfacecolor='blue', markersize=12)
    plt.show()

    n = 1000000

    # Aproksymacja wartości π
    approx_pi = von_neumann.von_neumann_pi_approximation(n)
    print("Aproksymacja wartości π:", approx_pi)