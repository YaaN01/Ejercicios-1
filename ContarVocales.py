voc = ["a", "A", "i", "I", "u", "U", "e", "E", "o", "O"]
x = input("Escriba una palabra:")
n = 0

for letter in x:
    if letter in voc:
        n += 1

print(f"Tu palabra tiene {n} vocales.")