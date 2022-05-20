try:
    numero = int(input("Ingrese un opcion:"))
except ValueError:
    print("Error, el valor ingresado no es númerico.")
except:
    print("Error, en la solicitud de datos.")

print("Fin app")
