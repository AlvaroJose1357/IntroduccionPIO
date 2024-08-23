"""Escriba un programa que invierta la palabra"""

def invertirCadena(cadena):
  invertida = ""
  for letra in cadena:
    invertida = letra + invertida
  return invertida

print(invertirCadena("hola"))