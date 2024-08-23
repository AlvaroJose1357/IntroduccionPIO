
# !Funcion Simple
def saludar():
  print("Hola Mundo con funciones")
  
saludar()

#!funcion con parametros 
def saludar2(nombre):
  print(f"Hola, {nombre}, BIENVENIDO")
  
saludar2("Juan")
#! funcion con parametros estrictos
def saludar3(nombre: str):
  print(f"Hola, {nombre}, BIENVENIDO")
  
saludar3("Juan")
#!Funcion con valor de retorno 
def suma(num1, num2):
  return num1 + num2

resultado = suma(3,4)
print(resultado)