from http.client import CannotSendHeader


print("********* Zapatería Duoc Uc *********")
cantidad = input("Ingrese la cantidad de zapatos a vender: ")
cantidad = int(cantidad)
valor = 0
if cantidad == 1:
    valor = 23000
else:
    valor = cantidad * 20000

print("El total a pagar es:", valor)