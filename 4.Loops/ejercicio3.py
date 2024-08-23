# Escribir un programa que cuente cuantas vocales hay en una palabra ingresada por el usuario
# v1
# palabra = input("ingresa las palabra a verificar: ").lower()
# vocales = "aeiou"
# contador = 0

# for letra in palabra:
#   if letra in vocales:
#     print(f"Vocal: {letra}")
#     contador+=1
# print(f"El numero de vocales de la palabra {palabra}, es {contador}")

#v2
palabra = input("Ingrese una palabra:").lower()
vocales = "aeiou"
numeros = "1234567890"
carateres = "°!#$%&/()=?¡¨[]:_;*+-"
contador = 0
esValido = False

for letra in palabra:

    if (letra in numeros or letra in carateres):
        esValido = True
        break

    if letra in vocales:
        print(f"Vocal: {letra}")
        contador += 1

if esValido: # lo mismo que poner (esValido == True)
    print("Error, la palabra no es valida por que tiene números o caraterestes")
else:
    print(f"El número de vocales en la palabra {palabra}, es {contador}")