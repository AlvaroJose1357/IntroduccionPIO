"""Crea un programa que pida número a1 usuario y los sume.
EI programa termina cuando el usuario ingrese un 0' ' '
"""

suma = 0
num = int(input("ingrese un num (0 para salir)"))

while num != 0: # ejecuta la verdad
  suma += num
  num = int(input("ingresa otro numero "))

print(f"la suma de los numeros ingresados es {suma}")