import numpy as np

A = np.array([[2, 1], [1, 3]])
B = np.array([8, 10])

sol = np.linalg.solve(A, B)

print(f"La solución es: x={sol[0]}, y={sol[1]}")