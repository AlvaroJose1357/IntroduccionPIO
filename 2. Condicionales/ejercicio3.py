#3 Comprobar si un año es bisiesto.
#Condiciones: Un año es bisiesto si es divisible por 4, pero no por 100, a menos que sea divisible por 400.
year = int(input("Ingrese el año: "))
if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
  print("El año es bisiesto")
  