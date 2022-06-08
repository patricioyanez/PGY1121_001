import numpy as num

## comparamos los elementos de 2 arreglos 
a1 = num.array([1,2,3,4,5])
a2 = num.array([1,2,3,4,5])
a3 = num.array([6,2,7,8,0])

print("Igualdad :", a1 == a2)
print("Igualdad :", a1 == a3)
print("Mayores  :", a1 > a3)
print("Menores  :", a1 < a3)
print("Distintos:", a1 != a3)


# métodos estadísticos
print(a1)
print("Suma     : ", a1.sum())
print("Suma     : ", sum(a1))
print("Mayor    : ", a1.max())
print("Mayor    : ", max(a1))
print("Menor    : ", a1.min())
print("Menor    : ", min(a1))
print("promedio : ", a1.mean()) # average AVG