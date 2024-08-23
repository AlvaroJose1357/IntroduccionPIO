'''Mini Proyecto: Gestor de Tareas
Objetivo:
Crear una aplicación de consola que permita al usuario gestionar una lista de tareas. 
El usuario podrá añadir tareas, ver la lista de tareas, ordenarlas por prioridad, y eliminar tareas completadas.
Funcionalidades:
Añadir Tarea: Permite al usuario añadir una nueva tarea con una descripción y una prioridad.
Mostrar Tareas: Muestra todas las tareas actuales.
Ordenar Tareas: Ordena las tareas por su prioridad.
Eliminar Tarea: Permite al usuario eliminar una tarea completada.
Estructura del Proyecto:
La lista de tareas será una lista de diccionarios, donde cada diccionario representará una tarea con una descripción 
y una prioridad.
'''
def addTask(tareas):
  print("------------------ Añadir Tarea -------------------")
  titulo = input("Ingrese el titulo de la tarea:\n")
  descripcion = input("Ingrese la descripcion de la tarea:\n")
  prioridad = input("Ingrese la prioridad de la tarea:\n")
  tarea = {"titulo": titulo,"descripcion": descripcion, "prioridad": prioridad}
  tareas.append(tarea)
  print("Tarea Agregada con exito!!!")

def showTasks(tareas):
  print("------------------ Mostrar Tareas -------------------")
  if not tareas:
    print("No hay tareas")
  else:
    # los <20 son para que haya un espacio entre cada título
    print(f"{'Numero':<10} {'Titulo':<20} {'Descripcion':<20} {'Prioridad':<20}")
    for i, tarea in enumerate(tareas):
      print(f"{i+1:<10}{tarea['titulo']:<20} {tarea['descripcion']:<20} {tarea['prioridad']:<20}")

def sortTasks(tareas):
  # se agrega la función lambda toma X como argumento para que al momento de pedirlo se
  tareas.sort(key=lambda x: x['prioridad'])
  print("tareas ordenadas por prioridad")
  showTasks(tareas)

def deleteTask(tareas):
  print("------------------ Eliminar Tarea -------------------")
  if not tareas:
    print("No hay tareas")
  else:
    tarea = input("Ingrese el titulo de la tarea a eliminar:\n")
    for title in tareas:
      if title['titulo'] == tarea:
        tareas.remove(title)
        print("Tarea eliminada con exito!!!")
        break

def updateTask(tareas):
  print("------------------ Actualizar Tarea -------------------")
  if not tareas:
    print("No hay tareas")
  else:
    tarea = input("Ingrese el titulo de la tarea a actualizar:\n")
    for title in tareas:
      if title['titulo'] == tarea:
        title['titulo'] = input("Ingrese el nuevo titulo de la tarea:\n")
        title['descripcion'] = input("Ingrese la nueva descripcion de la tarea:\n")
        title['prioridad'] = input("Ingrese la nueva prioridad de la tarea:\n")
        print("Tarea actualizada con exito!!!")
        break

def menu():
  print("1. Añadir Tarea")
  print("2. Mostrar Tareas")
  print("3. Actualizar Tarea")
  print("4. Eliminar Tarea")
  print("5. Ordenar Tareas")
  print("6. Salir")

def main():
  tareas = [
        {"titulo": "Ciclo", "descripcion": "Programar ciclos", "prioridad": 5},
        {"titulo": "Condicionales", "descripcion": "Programar condicionales", "prioridad": 10},
        {"titulo": "Variables", "descripcion": "Programar variables", "prioridad": 8}
    ]
  print("------------Bienvenidos al Gestor de Tareas-------------")
  menu()
  while True:
    opcion = int(input("Ingrese la opcion:\n"))
    if 0 < opcion < 7 :
      if opcion == 1:
        addTask(tareas)
      elif opcion == 2:
        showTasks(tareas)
      elif opcion == 3:
        updateTask(tareas)
      elif opcion == 4:
        deleteTask(tareas)
      elif opcion == 5:
        sortTasks(tareas)
      elif opcion == 6:
        print("Hasta luego!!!")
        break
    else:
      print("Opcion invalida")

main()
