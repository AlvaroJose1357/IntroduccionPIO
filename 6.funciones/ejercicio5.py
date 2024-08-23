"""Programa Calculadora"""
def suma(x,y):
  return x+y
def resta(x,y):
  return x-y
def multiplicacion(x,y):
  return x*y
def dividir(x,y):
  if(y != 0):
    return x+y
  else:
    return "Error"
def opciones():
  print("1. Suma")
  print("2. Resta")
  print("3. Multiplicacion")
  print("4. Division")

def calculadora():
  print("-------------------------Bienvenidos a la calculadora-------------------------")
  opciones()
  while True:
    opcion = int(input("Ingrese la opcion:\n"))
    if 0 < opcion < 5 :
      num1 = int(input("Ingrese el primer numero:\n"))
      num2 = int(input("Ingrese el segundo numero:\n"))
      if opcion == 1:
        print(f"El resultado es {suma(num1,num2)}")
      elif opcion == 2:
        print(f"El resultado es {resta(num1,num2)}")
      elif opcion == 3:
        print(f"El resultado es {multiplicacion(num1,num2)}")
      elif opcion == 4:
        print(f"El resultado es {dividir(num1,num2)}")
      
      continuar = input("----------Desea continuar? s/n: ------------\n")
      if continuar == 's':
        opciones()
      else:
        print("Espero vernos pronto!!!")
        break
    else:
      print("Opcion invalida")
calculadora()