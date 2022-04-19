nota1 = input("Ingrese nota 1:")
nota2 = input("Ingrese nota 2:")
nota3 = input("Ingrese nota 3:")

nota1 = float(nota1)
nota2 = float(nota2)
nota3 = float(nota3)

if nota1 >= 1 and nota1 <= 7:
    if nota2 >= 1 and nota2 <= 7:
        if nota3 >= 1 and nota3 <= 7:
            promedio = (nota1 + nota2 + nota3) / 3
            
            if promedio >= 4:
                print("Aprobado")
            else:
                print("nos vimos")

print("*********** CIERRE DE SEMESTRE")