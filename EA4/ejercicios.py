from numpy import random

arreglos = random.randint(100, size = 10)
print(arreglos)
arreglo = arreglos.copy()

print("Suma :", arreglo.sum())
print("Mayor:", arreglo.max())
print("Menor:", arreglo.min())
print("Prom :", arreglo.mean())