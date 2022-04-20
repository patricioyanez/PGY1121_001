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
            print("Su promedio es:", "{0:.1f}".format(promedio) )
            if promedio >= 4:
                print("Aprobado")
            else:
                print("nos vimos")
        else:
            print("nota 3 esta fuera del rango")
    else:
        print("nota 2 esta fuera del rango")
else:
    print("nota 1 esta fuera del rango")
print("*********** CIERRE DE SEMESTRE")