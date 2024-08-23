# crea un programa que imprima todos los numeros impares del 1 al 10

# impares
# forma 1
# LIMITE = 10
# for i in range(1, LIMITE + 1, 2):
#   print(i)
LIMITE = 10
for i in range(1, LIMITE + 1):
  if(i % 2 != 0):
    print(i)
#pares
LIMITE2 = 10
for i in range(0, LIMITE2 + 1, 2):
  print(i)
for i in range(1, LIMITE2 + 1):
  if(i % 2 == 0):
    print(i)
