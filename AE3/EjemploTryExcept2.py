try:  
    a = 5
    b = 0
    c = a / b
    print("El resultado es:", c)
except ZeroDivisionError:
    print("ERROR: Se ha dividido por cero")
except:
    print("Error en la división")
    
print("Fin de la app")