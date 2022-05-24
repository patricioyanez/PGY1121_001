clientes = []
rut = ""
nombre = ""
direccion = ""
comuna = ""
correo = ""
edad = -1
genero = ""
celular =""
tipo = ""
suscripcion = True

opcion = 0

while opcion != 4:
    print("====== M E N Ú ======")
    print("1.- Registrar")
    print("2.- Suscripción")
    print("3.- Consultar datos")
    print("4.- Salir")

    try:
        opcion = int(input("Ingrese un opción: "))
    except:
        print("\n***** Opción ingresada no es válida *****")
        input("Presione enter para continuar.....")
        continue

    if opcion < 1 or opcion > 4:
        print("\n***** Opción ingresada no existe *****")
        input("Presione enter para continuar.....")
        continue

    if opcion == 4:
        print("Adios!!!")
    elif opcion == 1:
        rut         = input("ingrese su rut         : ")
        nombre      = input("ingrese su nombre      : ")
        direccion   = input("ingrese su direccion   : ")
        comuna      = input("ingrese su comuna      : ")
        correo      = input("ingrese su correo      : ")
        edad        = input("ingrese su edad        : ")
        genero      = input("ingrese su genero      : ")
        celular     = input("ingrese su celular     : ")
        tipo        = input("ingrese su tipo: 1.-PREMIUM 2.-GOLD 3.-SILVER:")

        if tipo == "1":
            tipo = "PREMIUM"
        elif tipo == "2":
            tipo = "GOLD"
        elif tipo == "3":
            tipo = "SILVER"

        fila = [rut, nombre, direccion, comuna, correo, edad, genero, celular,tipo]
        clientes.append(fila)