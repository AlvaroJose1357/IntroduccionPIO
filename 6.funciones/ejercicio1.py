"""Escribe una funcion llamada esPar que reciba un numero y devuelva el mayor de los 2"""

def esPar(num: int):
  if num % 2 == 0:
    return(f"El numero {num} es par")
  else:
    return(f"El numero {num} es impar")

numero = int(input("Ingrese un numero: "))
print(esPar(numero))