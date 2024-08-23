# crea una app que nos preguntara la edad del usuario, en caso de que sea mayor y cuente con licencia de conducir le va a mostrar que le informe que puede conducir, en el caso de que sea mayor deedad pero no tenga licensia le mostrara que no puede conducir por que tiene licencia y en el caso de que sea menor de edad le informara que no puede conducir por este motivo

edad = int(input("ingrese su edad: "))

if(edad >= 18):
  tieneLicencia = int(input("Tiene licencia de conducir? (1 para si, 0 para no): "))
  if(tieneLicencia == 1):
    print("puedes conducir")
  elif(tieneLicencia == 0):
    print("no puedes conducir por que no tienes licencia")
  else:
    print("digitalizacion numero erronea de licencia")
else:
  print("eres menor de edad")
