try:  
    a = 5
    b = 10
    c = a / b
    print("El resultado es:", c)
except ZeroDivisionError:
    print("ERROR: Se ha dividido por cero")
else:
    print("El bloque TRY se ejecutó con éxito")
    
print("Fin de la app")