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
        try:
            rut         = int(input("ingrese su rut         : "))
        except:
            print("\n***** El rut no es válido *****")
            input("Presione enter para continuar.....")
            continue

        nombre      = input("ingrese su nombre      : ")
        direccion   = input("ingrese su direccion   : ")
        comuna      = input("ingrese su comuna      : ")

        correo      = input("ingrese su correo      : ")
        
        if correo.count("@") != 1:
            print("\n***** El correo no es válido *****")
            input("Presione enter para continuar.....")
            continue 
        
        
        edad        = input("ingrese su edad        : ")
        if edad < 0 or edad > 110:
            print("\n***** La edad no es válida *****")
            input("Presione enter para continuar.....")
            continue 

        genero      = input("ingrese su genero(F o M):")
        genero = genero.upper()
        if genero != 'F' or genero != 'M':
            print("\n***** El género no es válida *****")
            input("Presione enter para continuar.....")
            continue 


        celular     = input("ingrese su celular     : ")
        tipo        = input("ingrese su tipo: 1.-PREMIUM 2.-GOLD 3.-SILVER:")

        if tipo == "1":
            tipo = "PREMIUM"
        elif tipo == "2":
            tipo = "GOLD"
        elif tipo == "3":
            tipo = "SILVER"
        else:
            print("\n***** El Tipo no es válido *****")
            input("Presione enter para continuar.....")
            continue 
        
        fila = [rut, nombre, direccion, comuna, correo, edad, genero, celular,tipo]
        clientes.append(fila)