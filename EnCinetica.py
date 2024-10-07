masa = float(input("Introduzca la masa del objeto en kg:"))

while masa < 0:
    masa = float(input("Valor erróneo, inténtelo de nuevo:"))

vel = float(input("Introduzca la velocidad del objeto en m/s:"))

cin = 0.5 * masa * vel**2

print(f"La energía cinética de tu objeto es {cin} J.")