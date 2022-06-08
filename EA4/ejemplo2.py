import numpy as num
# uso de metodos de numpy

arreglo = num.arange(10) # 0 al 9
print(arreglo)
arreglo = num.arange(10.0) # 0 al 9
print(arreglo)
arreglo = num.arange(4,8) # 4 al 7
print(arreglo)
arreglo = num.arange(2,11,2) # 2 al 10
print(arreglo)
arreglo = num.arange(1,11,2) # 2 al 10
print(arreglo)
arreglo = num.arange(0,101,5) # 2 al 10
print(arreglo)
## comprobamos que tipo de datos es
print(type(arreglo)) 

## cambia tambien el contenido de la variable arreglo
arr = arreglo
arr[0] = 1
print(arreglo[0])

## copia identica de un arreglo 
## NO AFECTA AL ARREGLO "ORIGINAL"
arreglo = num.arange(2,11,2) # 2 al 10
print(arreglo)
arr= arreglo.copy()
arr[0] = 1
print(arreglo)
print(arr)
