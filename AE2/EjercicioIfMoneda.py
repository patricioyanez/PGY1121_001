print("Convertidor de moneda a pesos chilenos de Chile")
print("*** Menú de monedas ***")
print("1.- Dolar Autraliano")
print("2.- Pesos Argentinos")
print("3.- Yen")
opcion = input("Seleccione moneda a convertir:")
cantidad = input("Ingrese cantidad de la moneda:")
cantidad = int(cantidad)
total = 0
if opcion == "1":
    total = cantidad * 607
elif opcion == "2":
    total = cantidad * 7.37
else:
    total = cantidad * 6.59

print("El total en pesos chilenos es:", total)


