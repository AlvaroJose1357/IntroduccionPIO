

def ordenamiento(a,b):
  temp = b
  b = a 
  a = temp
  mostrar(a, b)

def mostrar(a,b):
  print(f"El valor de A es: {a} y el valor de B es: {b}")

def main():
  a = 0
  b = 0
  while a == b:
    print("Digite dos numeros diferentes")
    a = float(input("Ingrese el valor de A: "))
    b = float(input("Ingrese el valor de B: "))
    ordenamiento(a,b)

main()