# Determinar si un carácter ingresado es una vocal o una consonante.
letra = input("ingresa la letra: ")
letras = letra.lower()

if(letras=="a" or letras=="e" or letras=="i" or letras=="o" or letras=="u" ):
  print("Es vocal")
else:
  print("Es consonante")