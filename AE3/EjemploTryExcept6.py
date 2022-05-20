try:
    numero = input("Ingrese un nro:")

    if not type(numero) is int:
        raise("Error: tipo de datos no coincide con lo solicitado")
except:
    print("Error en la solicitud de datos.")

print("Fin app")
