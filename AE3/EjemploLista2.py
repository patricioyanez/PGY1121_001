lista = [1,2]

# agregar
lista.append(3)

for nro in lista:
    print("El nro es ", nro)

lista2 = [4,5,6]
lista.extend(lista2)
lista3 = [7,8,9,10]
lista += lista3
print(lista)
print(lista2)
print(lista3)