a = 0
b = 0 

def comparador(a, b):
  if a == b:
    return True
  else:
    if a>b:
      print(f"El número {a} es mayor que {b}")
    else:
      print(f"El número {b} es mayor que {a}")
def main():
  while True:
    a = int(input("Ingrese el primer número: "))
    b = int(input("Ingrese el segundo número: "))
    
    if comparador(a,b):
      print("numeros invalidos, estos no pueden ser iguales")
    else:
      break

main()