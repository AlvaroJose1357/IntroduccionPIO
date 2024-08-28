def busquedaLineal(lista, x):
  for i in range(len(lista)):
    if lista[i] == x:
      return i
  return "Elemento no encontrado"

lista = [5,8,2,1,4,7,3,6,9]
x = 4
resultado = busquedaLineal(lista, x)
print(f"El elemento {x} se encuentra en la posicion {resultado}")