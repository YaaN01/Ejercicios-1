import matplotlib.pyplot as plt
import numpy as np

a = float(input("Valor de a:"))
b = float(input("Valor de b:"))
c = float(input("Valor de c:"))

x = np.linspace(0, 10, 100)
y = a*x**2 + b*x + c

plt.plot(x, y)
plt.show()