# importar numpy
import numpy as nu
casillero = nu.array([["","",""], ["","",""], ["","",""]], dtype=object)

# definir funciones
def arrendar(casillero):
    print("*** Arrendar casillero ****")
    print("Listado de casilleros")
    print("1.- Nivel 1 $ 10000")
    print("2.- Nivel 2 $ 5000")
    print("3.- Nivel 3 $ 2000")

    try:
        opcion = int(input("Seleccione opción: "))
        if opcion not in [1,2,3]:
            print("La opción no es válida")
            input("Presione enter para continuar...")
            return
        
        fila = opcion - 1
        mostrarColumnasDisponibles(casillero, fila)
        nroCasillero = int(input("ingrese número de casillero: "))
        columna = nroCasillero - 1

        nombre = input("Ingrese nombre del cliente: ")

        casillero[fila, columna] =  nombre
        print(casillero)
    except:        
        print("Error en el ingrese de la opción")
        input("Presione enter para continuar...")
        return


def mostrarColumnasDisponibles(casillero, fila):
    nroCasillero = 1
    print("Casilleros disponible de la fila: ", fila+1)
    for columna in casillero[fila]:
        if columna == "":
            print("Casillero nro:", nroCasillero)
        nroCasillero += 1


def mostrarUbicaciones(casillero):
    nroCasillero = 1
    valor = ""
    listado = ""
    print("Disponibilidad de casilleros")
    for fila in casillero: 
        for columna in fila:
            if columna == "":
                valor = str(nroCasillero)
            else:
                valor = "X"
            listado += valor + " "
            nroCasillero += 1
        listado += "\n"
    print(listado)
    input("Presione enter para continuar...")

def verListadoCliente(casillero):
    pass
def mostrarGanancias(casillero):
    pass


# iniciar programa
opcion = "0"
listaDeOpciones = ["1","2","3","4","5"]
while opcion != "5":
    print("====== Menú Principal Casilleros ======")
    print("1.- arrendar")
    print("2.- Mostrar ubicaciones disponibles")
    print("3.- Ver listado de clientes")
    print("4.- Mostrar ganancias")
    print("5.- Salir")
    opcion = input("ingrese opción:")

    if opcion not in listaDeOpciones:
        print("La opción no es válida")
        input("Presione enter para continuar...")
        continue
    if opcion == "5":
        print("Adiós...")
    else:
        if opcion == "1":
            arrendar(casillero)
        elif opcion == "2":
            mostrarUbicaciones(casillero)
        elif opcion == "3":
            verListadoCliente(casillero)
        elif opcion == "4":
            mostrarGanancias(casillero)