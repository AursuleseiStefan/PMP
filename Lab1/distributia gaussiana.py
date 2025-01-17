import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

u = 5
std = 1
snd = stats.norm(u, std)

x = np.linspace(1, 10, 100)

plt.figure(figsize=(8,8))
plt.plot(x, snd.pdf(x))
plt.xlim(1, 10)
plt.title('Distributia Gaussiana', fontsize='15')
plt.xlabel('Notele', fontsize='15')
plt.ylabel('Probabilitatea', fontsize='15')
plt.show()