'''Vamos crear un app que permita ingresar una nota y va evaluar si es aprobado(5 a 7), notable(8 a 9), sobresaliente(10) y todo menor a esto reprobado'''
nota = 7

if(5 <= nota <= 7):
  print("Aprovado")
elif(8 <= nota <= 9):
  print("Notable")
elif(nota == 10):
  print("sobresaliente")
elif(nota < 5):
  print("Deficiente")
else: 
  print("Nota ingresada erronea")