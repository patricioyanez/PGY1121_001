def calculo(precio , descuento):
    return precio - (precio * descuento / 100)

# calculo() da error
datos = [10000, 15]
print("Total a pagar es:", calculo(*datos))
datos = [50000, 20]
print("Total a pagar es:", calculo(*datos))
datos = [20000, 20]
print("Total a pagar es:", calculo(*datos))
datos = [10000, 20]
print("Total a pagar es:", calculo(*datos))
