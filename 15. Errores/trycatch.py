try:
  numero1 = int(input("Ingrese un numero:\n"))
  numero2 = int(input("Ingrese otro numero:\n"))

  suma = numero1 + numero2
except ValueError:
  print("Error: Dato ingresado no Válido") # Error: Dato ingresado no Válido