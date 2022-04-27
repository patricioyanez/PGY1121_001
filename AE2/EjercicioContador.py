print("**** Ingreso de numeros ****")
n1 = input("Ingrese nro 1: ")
n2 = input("Ingrese nro 2: ")
n3 = input("Ingrese nro 3: ")
acumulador= 0
contador = 0
if n1 > 0 and n1 % 2 == 0:
    acumulador += int(n1)
else:
    contador += 1 # contador = contado + 1
if n2 > 0 and n2 % 2 == 0:
    acumulador += int(n2)
else:
    contador += 1 # contador = contado + 1

if n3 > 0 and n3 % 2 == 0:
    acumulador += int(n3)
else:
    contador += 1 # contador = contado + 1
