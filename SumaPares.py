n = int(input("Introduzca un número entero positivo:"))
sum = 0
N = n

while n <= 0:
    n = int(input("Valor erróneo, introdúzcalo de nuevo:"))

while n > 0:
    sum += 2*n
    n -= 1

print(f"La suma de los primeros {N} números pares es {sum}.")