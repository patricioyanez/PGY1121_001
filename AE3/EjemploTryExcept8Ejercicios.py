## Ejercicios:

## Agregar al menu try except para validar el 
## correcto ingreso de la opcion de el menu

# 1.- Definir variables
opcion  = 0
subTotal= 0
# 2.- Solicitar la info al usuario
# 3.- Procesar info
# 4.- Mostrar resultados
print("\n ***** Panadería DUOC UC *****")

while opcion != 6:
    print("\n======== M E N Ú =========")
    print("1.- Pan Amasado")
    print("2.- Pan Molde")
    print("3.- Pan Baguette")
    print("4.- Pan Integral")
    print("5.- Total de la venta")
    print("6.- Salir")
    try:
        opcion = int(input("Ingrese opción: "))
    except:
        print("Error: valor incorrecto")
        continue
    
    if opcion < 1 or opcion > 6:
        input("======> ERROR: Opción no es válida. Presione enter para continuar")
    elif opcion == 5:
        if subTotal < 5000:
            subTotal *= 1.1
        else:
            print("El envio es gratis")
        print("El total a pagar es: {}".format(int(subTotal)))
        input("Presione enter para continuar")
        subTotal = 0
    elif opcion == 6:
        print("Nos vimos!")
    else:
        cantidad = int(input("Ingrese cantidad a comprar: "))
        if opcion == 1:
            subTotal += cantidad * 1500
        elif opcion == 2:
            subTotal += cantidad * 1000
        elif opcion == 3:
            subTotal += cantidad * 2000
        elif opcion == 4:
            subTotal += cantidad * 3000
        
