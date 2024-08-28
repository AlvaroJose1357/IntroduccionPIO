def busquedaBinaria(lista, x):
  inicio = 0
  fin = len(lista)-1
  while inicio <= fin:
    # el // es para que el resultado sea un entero
    mitad = inicio + (fin - inicio) // 2
    if lista[mitad] == x:
      return mitad
    elif lista[mitad] < x:
      inicio = mitad + 1
    else:
      fin = mitad - 1
  return "Elemento no encontrado"

lista = [1,2,3,4,5,6,7,8,9]
x = 1
resultado = busquedaBinaria(lista, x)
print(f"El elemento {x} se encuentra en la posicion {resultado}")