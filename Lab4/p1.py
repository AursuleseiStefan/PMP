import numpy as np


if __name__ == '__main__':
    md = 1
    standardev = 0.5
    tclient = np.random.poisson(20, 60)
    t = np.random.normal(md, standardev, 60)
    pregatire_comanda = np.random.exponential(scale=1, size=60)
    print("trafic  ", tclient, "\n timp ", t, "\n comenzi ", pregatire_comanda)