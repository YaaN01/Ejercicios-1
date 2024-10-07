n = input("Escribe un número entero positivo:")

while n<=0:
    n = int(input("Número erróneo, inténtelo de nuevo:"))

for num in range(1, n+1):
    print(num)