#14 verficar si una contraseña es ingresada correctamente
contrasenaPredeterminada = "1234"
contrasena = input("Ingrese la contraseña: ")

if(contrasena == contrasenaPredeterminada):
  print("Bienvenido al sistema")
else:
  print("Error, Credenciales incorreects, intenta nuevamente")
  