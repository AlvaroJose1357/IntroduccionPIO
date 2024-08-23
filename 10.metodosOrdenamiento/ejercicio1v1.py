A = 0
B = 0
temp = 0
while A == B:
  print("Digite dos numeros diferentes")
  A = float(input("Ingrese el valor de A: "))
  B = float(input("Ingrese el valor de B: "))
  if A < B:
    temp = B
    B = A 
    A = temp

print(f"El valor de A es: {A} y el valor de B es: {B}")