import numpy
arreglo = numpy.array([3,4,7,8,2,4,68,90,3,6])
print(arreglo)

# propiedades del arreglo
print("Cantidad de dimensiones:", arreglo.ndim)
print("Cantidad de elementos  :", arreglo.shape)
print("Cantidad de elementos  :", len(arreglo))

# acceder a los valores del arreglo
print("Valor del primer elemento:", arreglo[0])
print("Valor del 2do elemento:", arreglo[1])
print("Valor del último elemento:", arreglo[-1])
print("Valor del penúltimo elemento:", arreglo[-2])
print("Valor del antepenúltimo elemento:", arreglo[-3])

# permite extraer una porción de valores de un arreglo
print("Valores obtenidos:", arreglo[3:7])
print("Valores obtenidos:", arreglo[:7])
print("Valores obtenidos:", arreglo[3:])
print("Valores obtenidos:", arreglo[3:7:2])
print("Valores obtenidos:", arreglo[::3])
print("Valores obtenidos:", arreglo[2::3])
print("Valores obtenidos:", arreglo[:6:2])