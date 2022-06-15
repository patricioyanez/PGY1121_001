# definición de funciones
def sumar(num1, num2):
    return num1 + num2
def restar(num1, num2):
    return num1 - num2
def multiplicar(num1, num2):
    return num1 * num2
def dividir(num1, num2):
    if num2 == 0:
        return "No se puede dividir por cero"
    return num1 / num2



# programa
num1 = 0
num2 = 0
opcion = "0"
listaDeOpciones = ["1","2","3","4","5"]
while opcion != "5":
    print("====== Menú Principal ======")
    print("1.- Sumar")
    print("2.- Restar")
    print("3.- Dividir")
    print("4.- Multiplicar")
    print("5.- Salir")
    opcion = input("ingrese opción:")

    if opcion not in listaDeOpciones:
        print("La opción no es válida")
        input("Presione enter para continuar...")
        continue

    if opcion == "5":
        print("Adiós...")
    else:
        try:
            num1 = int(input("Ingrese numero1:"))
            num2 = int(input("Ingrese numero2:"))
        except:
            print("Número no válido")
            input("Presione enter para continuar...")
            continue

        if opcion == "1":
            resultado = sumar(num1, num2)
        elif opcion == "2":
            resultado = restar(num1, num2)
        elif opcion == "3":
            resultado = dividir(num1, num2)
        elif opcion == "4":
            resultado = multiplicar(num1, num2)
    
    print("El resultado es:", resultado)
    input("Presione enter para continuar...")