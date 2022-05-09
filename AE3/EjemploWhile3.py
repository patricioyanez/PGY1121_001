# 1.- definir variables
total = 0
contador = 1
# 2.- Solicitar datos
# 3.- Procesar la info
print("\n*********  Suma de 5 números positivos **********")

while contador <= 5:
    numero = int(input("Escriba el numero a sumar: "))

    if numero > 0: ## validar: que el número sea positivo
        total += numero #total = total * contador
        contador += 1
# 4.- mostrar resultado
print("el total de los nros positivos es:", total)