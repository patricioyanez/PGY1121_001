try:  
    a = 5
    b = 0
    c = a / b
    print("El resultado es:", c)
except ZeroDivisionError:
    print("ERROR: Se ha dividido por cero")
except:
    print("Error global")
else:
    print("holi")
finally:
    print("Bloque ejecutado con exito")
    
print("Fin de la app")