import matplotlib.pyplot as plt
import numpy as np

vel = float(input("Velocidad del objeto (m/s):"))
an = float(input("Ángulo de lanzamiento (grados):"))

an = (an*2*np.pi)/360

t = np.linspace(0, 5, 100)
x = vel*np.cos(an)*t
y = vel*np.sin(an)*t - 0.5*9.81*t**2 

plt.plot(x, y)
plt.show()
