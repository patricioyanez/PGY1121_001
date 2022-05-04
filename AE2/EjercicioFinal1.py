# 1.- Definir variables
# 2.- Solicitar la info

print("\n****  Comparador ****")
n1 = input("Ingrese 1er nro: ")
n2 = input("Ingrese 2do nro: ")
n3 = input("Ingrese 3er nro: ")


# 3.- procesar la info
# 4.- mostrar los resultados
n1 = int(n1)
n2 = int(n2)
n3 = int(n3)

if n1 > n2 and n1 > n3:
    print("El nro 1 es el mayor")
elif n2 > n3:
    print("El nro 2 es el mayor")
else:
    print("El nro 3 es el mayor")
