# 1.- definir variables
total = 1
contador = 1
# 2.- Solicitar datos
print("\n*********  Factorial **********")
numero = int(input("Escriba el numero para el factorial: "))
# 3.- Procesar la info
while contador <= numero:
    total *= contador #total = total * contador
    contador += 1
# 4.- mostrar resultado
print("EL factorial de {} es {}".format(numero, total))