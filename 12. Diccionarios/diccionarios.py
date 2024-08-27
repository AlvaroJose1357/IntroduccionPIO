#Definir
miDiccionario = {
  "Nombre": "Juan",
  "Edad": 30,
  "Cuidad": "Ibagué",
  "Cursos": ["Python", "Django", "JavaScript"]
}

#Acceder a los elementos
print(miDiccionario["Nombre"]) #Juan

#Añaadir elementos
miDiccionario["Email"] = "ejemplo@ejemplo.com"
miDiccionario["Nombre"] = "Juan David"

#Eliminar elementos
del miDiccionario["Email"] #Elimina el email
miDiccionario.pop("Nombre") #Elimina el nombre

# Iterar sobre un diccionario
for key, value in miDiccionario.items():
  print(key, value) 

print(miDiccionario)
