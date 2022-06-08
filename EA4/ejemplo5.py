import numpy as nu

arreglo2D = nu.array([ [1,2,3] , [4,5,6]])
print("Cantidad de dimensiones:", arreglo2D.ndim)
print("Cantidad de elementos  :", arreglo2D.shape)
print("Cantidad de elementos  :", len(arreglo2D[0]))
print("Cantidad de elementos  :", len(arreglo2D[1]))

print("valor coord 1,0:", arreglo2D[1,0])
print("valor coord 1,1:", arreglo2D[1,1])
print("valor coord 1,3:", arreglo2D[1,-1]) # indice 3, el ultimo

print("Suma     : ", arreglo2D.sum())
print("Mayor    : ", arreglo2D.max())
print("Menor    : ", arreglo2D.min())
print("promedio : ", arreglo2D.mean()) # average AVG
print("Valores obtenidos:", arreglo2D[0])
print("Valores obtenidos:", arreglo2D[0][1:2])
print("Valores obtenidos:", arreglo2D[0,1:2])


arreglo2D = nu.array([ [1,2,3,4,5,6,7,8] , [4,5,6,7,8,9,10,11]])
print("Valores obtenidos:", arreglo2D[0,1:7:2])