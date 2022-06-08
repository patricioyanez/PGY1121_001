import numpy as num
arreglo = num.array([1,2,3,4])
print(arreglo)
arreglo = arreglo + 1
print(arreglo)
arreglo += 1
print(arreglo)
arreglo **= 3
print(arreglo)
arreglo -= 2
print(arreglo)

arreglo1 = num.ones(10)
print("crea arreglo de 10 elementos con valor 1", arreglo1)
arreglo1 += 2
print("crea arreglo de 10 elementos con valor 1", arreglo1)

arreglo2 = num.ones(10)
print(arreglo2)
print("Suma de 2 arreglos:" , arreglo1 + arreglo2)
print("restar de 2 arreglos:" , arreglo1 - arreglo2)
arreglo2 +=2
print("restar de 2 arreglos:" , arreglo1 * arreglo2)
print("restar de 2 arreglos:" , arreglo1 ** arreglo2)