"""programa que pida un numero y lo muestre el programa parara cuando ingrese un numero negativo"""

num = int(input("ingrese un numero(ingresa un numero negativo para salir) "))
while num >= 0:
  print(f"El numero es {num}")
  num = int(input("ingresa otro numero "))
else:
  print("HELLO WORLD")