print("hello world")

# Variables enteras
numero1 = 5
print(type(numero1))
# Variables flotantes
numero2 = 5.5
numero2Round = round(numero2)
print(type(numero2))
print(numero2Round)

# Variables booleanas
verdadero = True
falso = False
print(type(verdadero))
print(type(falso))

# Variables de cadena 
caracter = "A"
codigo = ord(caracter)
print(codigo)

# Variables de texto
cadena = "Hola Mundo"
print(cadena)

# Variables de lista
# [] -> corchetes
cadenaL = "Hola"
print(cadenaL[0])
lista = [1, 2, 3, 4, 5]
print(lista[2])
lista2 = [1, "Hola", 3.5, True]
print(lista2[1])
usuario = ["Juan", 25, True]
print(usuario[0])
numerosASumar = [1,2,3,4,5]
suma = sum(numerosASumar)
print(suma)

# Variables de tupla 
# son inmutables
# () -> paréntesis
tupla = (1, 2, 3, 4, 5)
print(tupla[2])

# Variables de diccionario
# {} -> llaves
diccionario = {
    "nombre": "Juan",
    "edad": 25,
    "casado": True
}
print(diccionario["nombre"])