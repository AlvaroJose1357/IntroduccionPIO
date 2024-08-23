"""Calculadora con funciones anidadas"""
def calculadora(operador,x,y):
  def suma(a,b):
    return a+b
  def resta(a,b):
    return a-b
  def multiplicacion(a,b):
    return a*b
  def dividir(a,b):
    if(b != 0):
      return a/b
    else:
      return "Error"
  if operador == "sumar" or operador == "+":
    return suma(x,y)
  elif operador == "restar" or operador == "-":
    return resta(x,y)
  elif operador == "multiplicar" or operador == "*":
    return multiplicacion(x,y)
  elif operador == "dividir" or operador == "/":
    return dividir(x,y)
  else:
    return "Operador invalido"
def main():
  while True:
    print("-------------------------Bienvenidos a la calculadora-------------------------")
    operador = input("Ingrese el operador:\n").lower()
    num1 = int(input("Ingrese el primer numero:\n"))
    num2 = int(input("Ingrese el segundo numero:\n"))
    print(f"El resultado es {calculadora(operador,num1,num2)}")
    print("----------Desea continuar? (s: para continuar): ------------")
    continuar = input()
    if continuar == 's':
      continue
    else:
      print("Espero verte pronto!!!")
      break
main()
