#  Escribir un programa que imprima la tabla de mulriplicar del 1 al 10

for i in range(1,11): 
  print(f"la tabla del multiplicar del {i}")
  for j in range (1,11):
    print(f"{i} X {j} = {i*j}")
  print()