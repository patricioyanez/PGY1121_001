# 1.- Definir variables
# 2.- Solicitar la info

print("\n****  Registro de persona ****")
nombre = input("Ingrese su nombre   : ")
edad = input("Ingrese su edad     : ")
celular = input("Ingrese su celular  : ")
genero = input("Ingrese su género 1.- varón 2.-mujer:")

# 3.- procesar la info
# 4.- mostrar los resultados
if genero == "1": # int(genero) == 1:
    print(f"Su nombre es {nombre} y su edad {edad}")
else:
    print(f"Su nombre es {nombre} y su celular {celular}")

