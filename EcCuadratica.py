import matplotlib.pyplot as plt
import numpy as np

a = 1
b = 0
c = -4

raiz = np.roots([a, b, c])


x = np.linspace(raiz[0]-5, raiz[1]+5, 100)
y = a*x**2 + b*x + c

plt.plot(x, y)
plt.grid(linestyle='dashed')
plt.show()