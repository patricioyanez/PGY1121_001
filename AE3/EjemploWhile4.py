# 1.- definir variables
flag = True
# 2.- Solicitar datos
print("\n*********  Invertir numeros **********")
while flag:
    nro = int(input("Ingrese el nro a invertir:"))

    if nro >= 103 and nro <= 987:
        flag = False
# 3.- Procesar la info
unidad  = int(nro / 100) # 3
decena  =  int(nro / 10) - unidad * 10 #32 
centena = nro - (unidad * 100 + decena *10 )
total = int(unidad) + int(decena) * 10 + int(centena) * 100
# 4.- mostrar resultado 
print("El total ", total)

nroString = str(nro)
nroString1 = ''.join(reversed(nroString))

print(int(nroString1))
print(int(nroString[::-1]))