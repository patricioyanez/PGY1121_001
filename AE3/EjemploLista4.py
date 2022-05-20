lista = [1,2,3]
print(lista)
# elimina el ultimo item de la lista
eliminado = lista.pop()
print(lista)
print("El valor eliminado es:", eliminado)

lista.append(3)

print(lista)
eliminado = lista.pop(1)
print("El valor eliminado pop indice es:", eliminado)