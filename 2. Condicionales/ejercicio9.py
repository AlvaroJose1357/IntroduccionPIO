# 9 determine si un numero es divisible por 3 y 5
num = int(input("Ingrese un número: "))
if(num % 3 == 0 and num % 5 == 0):
  print (f"El número {num} es divisible por 3 y 5.")
else: 
  print (f"El número {num} no es divisible por 3 y 5.")