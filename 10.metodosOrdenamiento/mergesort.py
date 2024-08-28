def mergeSort(arr):
  if len(arr) > 1:
    mitad = len(arr) // 2
    izquierda = arr[:mitad]
    derecha = arr[mitad:]

    mergeSort(izquierda)
    mergeSort(derecha)

    i = j = k = 0

    while i < len(izquierda) and j < len(derecha):
      if izquierda[i] < derecha[j]:
        arr[k] = izquierda[i]
        i += 1
      else:
        arr[k] = derecha[j]
        j += 1
      k += 1

    while i < len(izquierda):
      arr[k] = izquierda[i]
      i += 1
      k += 1

    while j < len(derecha):
      arr[k] = derecha[j]
      j += 1
      k += 1

  return arr

lista = [5,8,2,1,4,7,3,6,9]
print(f"Lista Original: {lista}")
listaOrdenada = mergeSort(lista)
print(f"Lista Ordenada con el metodo mergeSort: {listaOrdenada}")
