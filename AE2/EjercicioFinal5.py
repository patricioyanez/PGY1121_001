# 1.- Definir variables
total = 0

# 2.- Solicitar la info
print("\n****  Ventas de artículos ****")
churrasco  = int(input("Ingrese cantidad de Churrasco  : "))
completo     = int(input("Ingrese cantidad de Completo   : "))
vegetariano    = int(input("Ingrese cantidad de Vegetariano: "))
barros      = int(input("Ingrese cantidad de Barros Luco: "))
codigo = input("Tiene codigo de descuento: 1.-Si 2.-No")

# 3.- procesar la info

total += churrasco * 1000 # total = total + mascarilla * 1000
total += completo * 1000
total += vegetariano * 2000
total += barros * 3000

if codigo == "1":
    total -= 10 * total / 100

# 4.- mostrar los resultados
print("El total a pagar es:", str(format(int(total), ",d")).replace(",","."))