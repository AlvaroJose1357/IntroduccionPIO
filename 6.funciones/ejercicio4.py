'''Vamos a crear programa que simule el juego de adivinar'''
import random
#Lista de palabras para el juegos
palabras = ['python','scrum','programacion','metodologia']
def elegir_palabra(palabras:list):
    #Elegimos la palabra y el choise dice de donde 
    return random.choice(palabras)
  
def jugarAdivinar(palabra):
  intentos = 2
  print("Bienvenidos al juego")
  print(f"Tienes {intentos} intentos")
  while intentos > 0:
    intento = input("ingresa la palabra: ").lower()
    if intento == palabra:
      print("Adivinaste la palabra")
      break
    else:
      intentos -= 1
      if intentos > 0:
        print(f"Incorrecto, te quedan {intentos}")
      else:
        print(f"Te quedaste sin intentos, la palabra era {palabra}")

palabra = elegir_palabra(palabras)
jugarAdivinar(palabra)