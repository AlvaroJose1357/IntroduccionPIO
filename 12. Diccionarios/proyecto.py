"""Desarrolla un programa en Python que gestione una agenda de contactos simple. El programa debe permitir al usuario realizar las siguientes acciones:
* Añadir un contacto: Se pedirá al usuario que ingrese el nombre, número de teléfono y correo electrónico del contacto. Esta información se guardará en un diccionario donde la clave será el nombre del contacto y el valor será otro diccionario que contendrá el teléfono y el email.
* Eliminar un contacto: El usuario podrá eliminar un contacto ingresando su nombre. Si el contacto existe, será eliminado; de lo contrario, se mostrará un mensaje indicando que el contacto no se encontró.
* Buscar un contacto: El usuario podrá buscar un contacto por su nombre. Si el contacto existe, se mostrará su información (nombre, teléfono y correo electrónico).
* Mostrar todos los contactos: El programa debe mostrar una lista de todos los contactos guardados en la agenda con sus respectivos datos.
Salir del programa: El programa finalizará su ejecución."""
from tabulate import tabulate

def mostrar_menu():
  print("1. Añadir Contacto")
  print("2. Actualizar Contacto")
  print("3. Eliminar Contacto")
  print("4. Buscar Contacto")
  print("5. Mostrar Contactos")
  print("6. Salir")

def Tabla(contactos):
  headers = ["ID","Nombre", "Teléfono", "Correo"]
    # rows = [[i + 1, nombre, contacto["telefono"], contacto["correo"]] for i, (nombre, contacto) in enumerate(sorted(contactos, key=lambda x: x[nombre]))]
    # al usar sorted puede ordenar listas, pero al intentar usar un diccionario
    # mejor se le pasa el .items() para que pueda Ordena los elementos del diccionario (pares clave-valor) por las claves, que son los nombres de los contactos.
  rows = [[i + 1, nombre, contacto["telefono"], contacto["correo"]] for i, (nombre, contacto) in enumerate(contactos.items())]
  print(tabulate(rows, headers, tablefmt="github"))

def anadir_contactos(contactos):
  print("------------------ Añadir Contacto -------------------")
  nombre = input("Ingrese el nombre del contacto:\n").lower()
  telefono = input("Ingrese el número de teléfono del contacto:\n")
  correo = input("Ingrese el correo electrónico del contacto:\n")
  contactos[nombre] = {"telefono": telefono, "correo": correo}
  print(f"Contacto {nombre} agregado con exito!!!")

def actualizar_contacto(contactos):
  print("------------------ Actualizar Contacto -------------------")
  nombre = input("Ingrese el nombre del contacto a actualizar:\n").lower()
  if nombre in contactos:
      contacto = contactos[nombre]
      telefono = input(f"Ingrese el nuevo número de teléfono para {nombre}:\n")
      contacto["telefono"] = telefono
      correo = input(f"Ingrese el nuevo correo electrónico para {nombre}:\n")
      contacto["correo"] = correo
      print("Contacto actualizado con exito!!!")
      mostrar_contactos(contactos)

def eliminar_contacto(contactos):
  print("------------------ Eliminar Contacto -------------------")
  nombre = input("Ingrese el nombre del contacto a eliminar:\n")
  if nombre in contactos:
    confirmacion = input(f"¿Está seguro que desea eliminar el contacto '{nombre}'? (s/n): ").lower()
    if confirmacion == 's':
      del contactos[nombre]
      print("Contacto eliminado con éxito!!!")
    else:
      print("Operación cancelada.")
  else:
      print("El contacto no se encontró.")

def buscar_contacto(contactos):
  print("------------------ Buscar Contacto -------------------")
  indicio = input("Ingrese el nombre del contacto a buscar:\n").lower()
  resultado = {nombre: contacto for nombre, contacto in contactos.items() if indicio in nombre}
  """# nombre = input("Ingrese el nombre del contacto a buscar:\n").lower()
  if nombre in contactos:
      contacto = contactos[nombre]
      # print(f"Nombre:{ nombre}")
      # print(f"Teléfono: {contacto['telefono']}")
      # print(f"Correo:{ contacto['correo']}")
      print("Contacto encontrado!!!")
      Tabla({nombre: contacto})"""
  if resultado:
    print(f"Se encontraron {len(resultado)} contactos.")
    Tabla(resultado)
  else:
    print("No se encontraron contactos.")

def mostrar_contactos(contactos):
  print("------------------ Mostrar Contactos -------------------")
  print(f"Tienes {len(contactos)} contactos.")
  Tabla(contactos)

def main():
  contactos = {
    'juan': {'telefono': '132', 'correo': '123'}, 
    'maria': {'telefono': '5551234567', 'correo': 'maria@example.com'},
    'carlos': {'telefono': '5552345678', 'correo': 'carlos@example.com'},
    'luisa': {'telefono': '5553456789', 'correo': 'luisa@example.com'},
    'pedro': {'telefono': '5551122334', 'correo': 'pedro@example.com'},
    'paola': {'telefono': '5552233445', 'correo': 'paola@example.com'},
    'pedrina': {'telefono': '5553344556', 'correo': 'pedrina@example.com'},
    'peter': {'telefono': '5554455667', 'correo': 'peter@example.com'},
    'marcos': {'telefono': '5555566778', 'correo': 'marcos@example.com'},
    'marcelo': {'telefono': '5556677889', 'correo': 'marcelo@example.com'},
    'marta': {'telefono': '5557788990', 'correo': 'marta@example.com'},
    'martin': {'telefono': '5558899001', 'correo': 'martin@example.com'},
    'julia': {'telefono': '5559900112', 'correo': 'julia@example.com'},
    'julian': {'telefono': '5551011223', 'correo': 'julian@example.com'},
    'lina': {'telefono': '5552122334', 'correo': 'lina@example.com'},
    'luis': {'telefono': '5553233445', 'correo': 'luis@example.com'},
    'luisa': {'telefono': '5554344556', 'correo': 'luisa@example.com'},
    'luan': {'telefono': '5555455667', 'correo': 'luan@example.com'},
    'sandra': {'telefono': '5556566778', 'correo': 'sandra@example.com'},
    'laura': {'telefono': '5553456782', 'correo': 'laura@example.com'},
    'julian': {'telefono': '5554567893', 'correo': 'julian@example.com'},
    'mariana': {'telefono': '5555678904', 'correo': 'mariana@example.com'}, 
    'jose': {'telefono': '159', 'correo': '753'}
    }
  while True:
    print("------------------ Agenda de Contactos -------------------")
    mostrar_menu()
    opcion = input("Ingrese una opción: ")
    if opcion != "1" and not contactos:
      print("No hay contactos existentes. Agregue un contacto primero.")
      continue
    if opcion == "1":
      anadir_contactos(contactos)
    elif opcion == "2":
      actualizar_contacto(contactos)
    elif opcion == "3":
      eliminar_contacto(contactos)
    elif opcion == "4":
      buscar_contacto(contactos)
    elif opcion == "5":
      mostrar_contactos(contactos)
    elif opcion == "6":
      print("Saliendo del programa...")
      break
    else:
      print("Opción no válida. Intente de nuevo.")
main()