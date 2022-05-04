# 1.- Definir variables
total = 0

# 2.- Solicitar la info
print("\n****  Ventas de artículos ****")
mascarilla = int(input("Ingrese cantidad de mascarillas         : "))
guantes = int(input("Ingrese cantidad de Guantes             : "))
delantal = int(input("Ingrese cantidad de Delantal            : "))
amonio = int(input("Ingrese cantidad de Amonio cuaternario  : "))
descuento = int(input("Ingrese % de descuento:"))

# 3.- procesar la info

total += mascarilla * 1000 # total = total + mascarilla * 1000
total += guantes * 1000
total += delantal * 2000
total += amonio * 3000

if descuento> 0:
    total -= descuento * total / 100

# 4.- mostrar los resultados
print("El total a pagar es:", str(format(int(total), ",d")).replace(",","."))