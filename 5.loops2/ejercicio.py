"""Programa que defina un numero del 1 al 100. el jugador debe intentar adivinar y el programa le indicara si esta caliente o frio (caliente 10 unidades o menos del numero)"""
import random

numeroSecreto = random.randint(1, 100)
print("Adivinar el numero del 1 al 100")
intentos = int(input("Ingrese su intento "))
# vidas 


while intentos != numeroSecreto:
  if(intentos > numeroSecreto):
    diferencia = intentos - numeroSecreto
  else:
    diferencia = numeroSecreto - intentos
  
  if(diferencia <= 10):
    print("Estas Caliente")
  else:
    print("Estas Frio")
  
  if(intentos < numeroSecreto):
    print("El numero Secreto es mayor")
  else:
    print("El numero Secreto es menor")
  intentos = int(input("Ingrese su intento "))
print("ganaste")