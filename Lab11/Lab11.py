import numpy as np
from matplotlib import pyplot as plt
from scipy import stats


# functie ex 1
def posterior_grid(grid_points=50, heads=6, tails=9):
    grid = np.linspace(0, 1, grid_points)
    prior = grid ** 2 + grid / 3
    likelihood = stats.binom.pmf(heads, heads+tails, grid)
    posterior = likelihood * prior
    posterior /= posterior.sum()
    return grid, posterior


# functie ex 2
def error_mean(N):
    error_sum = 0
    x_list = []
    y_list = []
    for i in range(10):
        x, y = np.random.uniform(-1, 1, size=(2, n))
        for j in x:
            x_list.append(j)
        for j in y:
            y_list.append(j)
        inside = (x ** 2 + y ** 2) <= 1
        pi = inside.sum() * 4 / n
        error = abs((pi - np.pi) / pi) * 100
        error_sum += error
        outside = np.invert(inside)
    return x_list, y_list, error_sum / 10*N


# functie ex 3
def metropolis(func, draws=10000):
    trace = np.zeros(draws)
    old_x = 0.5
    old_prob = func.pdf(old_x)
    delta = np.random.normal(0, 0.5, draws)
    for i in range(draws):
        new_x = old_x + delta[i]
        new_prob = func.pdf(new_x)
        acceptance = new_prob / old_prob
        if acceptance >= np.random.random():
            trace[i] = new_x
            old_x = new_x
            old_prob = new_prob
    else:
        trace[i] = old_x
    return trace


if __name__ == '__main__':
    # Ex 1
    data = np.repeat([0, 1], (50, 30))
    points = 10
    h = data.sum()
    t = len(data) - h
    grid, posterior = posterior_grid(points, h, t)
    plt.plot(grid, posterior, 'o-')
    plt.title(f'heads = {h}, tails = {t}')
    plt.yticks([])
    plt.xlabel('θ')
    plt.show()

    # Ex 2
    N = [100, 1000, 10000]
    for n in N:
        x_list, y_list, em = error_mean(n)
        plt.errorbar(x_list, y_list, xerr=em)
        plt.show()

    # Ex 3
    func = [stats.beta(1, 1), stats.beta(20, 20), stats.beta(1, 4)]
    for f in func:
        trace = metropolis(func=f)
        x = np.linspace(0.01, .99, 100)
        y = f.pdf(x)
        plt.xlim(0, 1)
        plt.plot(x, y, 'C1-', lw=3, label='True distribution')
        plt.hist(trace[trace > 0], bins=25, density=True, label='Estimated distribution')
        plt.xlabel('x')
        plt.ylabel('pdf(x)')
        plt.yticks([])
        plt.legend()
        plt.show()
