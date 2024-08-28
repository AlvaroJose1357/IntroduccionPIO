def quickSort(lista):
  if len(lista) <= 1:
    return lista
  else:
    pivote = lista[0]
    # el 1: es para que no tome el pivote, o sea que no tome el primer elemento
    menores = [x for x in lista[1:] if x <= pivote]
    mayores = [x for x in lista[1:] if x > pivote]
    return quickSort(menores) + [pivote] + quickSort(mayores)

lista = [5,8,2,1,4,7,3,6,9]
print(f"Lista Original: {lista}")
listaOrdenada = quickSort(lista)
print(f"Lista Ordenada con el metodo quick sort: {listaOrdenada}")
