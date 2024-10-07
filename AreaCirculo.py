import numpy

r = float(input("Introduzca el radio:"))

while r<0:
    r = float(input("Número erróneo, inténtelo de nuevo:"))

area = numpy.pi*r**2

print(f"El área es {area}.")