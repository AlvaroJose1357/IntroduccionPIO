# Clasificar un triángulo según sus lados.
# Condiciones: Si los tres lados son iguales, es un triángulo equilátero. Si dos lados son iguales, es un triángulo isósceles. Si todos los lados son diferentes, es un triángulo escaleno.

lado1 = int(input("Ingrese el primer lado: "))
lado2 = int(input("Ingrese el segundo lado: "))
lado3 = int(input("Ingrese el tercer lado: "))

if(lado1 == lado2 == lado3):
  print("Es un triángulo Equilátero")
elif(lado1 == lado2 or lado1 == lado3 or lado2==lado3):
  print("Es un Triangulo Isosceles")
else:
  print("Es un triangulo Escaleno")