"""definir varios tipos de diferentes datos"""
miLista = ["María", 5, True, 78.35]

print(miLista) #imprime toda la lista

#!Operacioes con listas 
#?Agregar elementos a la final de la lista
miLista.append("Juan")

print(miLista[-1]) #imprime el último elemento de la lista

#? modificar un elemento de la lista]
miLista[3] = False

#?Añadir elementos en posicion especifica
miLista.insert(0, "María Jose") #agrega un elemento en la posición 0

#? Eliminar elementos de la lista en especifico
# si hay elementos duplicados, solo elimina el primero que encuentre
miLista.remove("María Jose") #elimina el elemento "María" de la lista
miLista.remove(miLista[4]) #elimina el elemento 5 de la lista

#? Recorrer la lista
for elemento in miLista:
    print(elemento)

#? Ordenar la lista
# solo se puede ordenar si todos los elementos son del mismo tipo
#miLista.sort() 

numeros = [5,2,8,4,8,41,6,45,1,53,5,9,4]
numSort = numeros.sort() #ordena la lista de menor a mayor
print(numSort)
numSorted = numeros.sort(reverse=True) #ordena la lista de mayor a menor

nombres = ["Juan", "Ana", "Zacarias", "Maria", "Jose"]
nomSort = nombres.sort() #ordena la lista de menor a mayor
print(nomSort)
nomSorted = nombres.sort(reverse=True) #ordena la lista de mayor a menor
print(nomSorted)
