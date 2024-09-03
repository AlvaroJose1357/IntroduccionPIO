# Sistema de gestion de libros de una biblioteca

# Importamos las librerias necesarias

# Definimos la lista de libros
libros = [
    {
        "titulo": "Cien Años de Soledad",
        "autor": "Gabriel García Márquez",
        "isbn": "978-3-16-148410-0",
        "genero": "Ficción",
        "cantidad": 5
    },
    {
        "titulo": "Don Quijote de la Mancha",
        "autor": "Miguel de Cervantes",
        "isbn": "978-1-23-456789-7",
        "genero": "Clásico",
        "cantidad": 3
    },
    {
        "titulo": "La Odisea",
        "autor": "Homero",
        "isbn": "978-0-12-345678-9",
        "genero": "Épico",
        "cantidad": 4
    }
]

# Lista de usuarios
usuarios = []

# funcion para agregar un libro al inventario
def agregar_libro():
  print("------------------------------------ Agregar libro ------------------------------------")
  titulo = input("Ingrese el titulo del libro: ")
  autor = input("Ingrese el autor del libro: ")
  isbn = input("Ingrese el ISBN del libro: ")
  genero = input("Ingrese el genero del libro: ")
  cantidad = int(input("Ingrese la cantidad de libros: "))
  
  libro = {
    "titulo": titulo,
    "autor": autor,
    "isbn": isbn,
    "genero": genero,
    "cantidad": cantidad
  }
  libros.append(libro)
  print(f"Libro {titulo} agregado con éxito")
  

# funcion para editar un libro del inventario
def editar_libro():
  mostrarlibros()
  print("------------------------------------ Editar libro ------------------------------------")
  isbn = input("Ingrese el ISBN del libro que desea editar: ")
  libro = next((libro for libro in libros if libro['isbn'] == isbn), None)
  if not libro:
    print("Libro no encontrado")
    return
  else: 
    print(f"Libro encontrado: {libro['titulo']} - {libro['autor']} - {libro['isbn']} - {libro['genero']} - {libro['cantidad']}")
    titulo = input("Ingrese el nuevo titulo del libro: ")
    autor = input("Ingrese el nuevo autor del libro: ")
    genero = input("Ingrese el nuevo genero del libro: ")
    cantidad = int(input("Ingrese la nueva cantidad de libros: "))
    libro["titulo"] = titulo
    libro["autor"] = autor
    libro["genero"] = genero
    libro["cantidad"] = cantidad
    print(f"Libro {titulo} editado con éxito")
    print(f"Nuevo libro: {libro['titulo']} - {libro['autor']} - {libro['isbn']} - {libro['genero']} - {libro['cantidad']}")
# funcion para eliminar un libro del inventario
def eliminar_libro():
  mostrarlibros()
  print("------------------------------------ Eliminar libro ------------------------------------")
  isbn = input("Ingrese el ISBN del libro que desea eliminar: ")
  """v1 
    # se coloca la variable global para que se pueda modificar la variable libros
    isbn = input("Ingrese el ISBN del libro que desea eliminar: ")
    global libros
    libros = [libro for libro in libros if libro['isbn'] != isbn]
    print(f"El libro con el ISBN: {isbn} ha sido eliminado")
  """
  libro = next((libro for libro in libros if libro['isbn'] == isbn), None)
  if not libro:
    print("Libro no encontrado")
    return
  else: 
    print(f"Libro encontrado: {libro['titulo']} - {libro['autor']} - {libro['isbn']} - {libro['genero']} - {libro['cantidad']}")
    confirm = input("¿Está seguro que desea eliminar este libro? (s/n): ").lower()
    if confirm == "s":
      libros.remove(libro)
      print(f"Libro {libro['titulo']} eliminado con éxito")
    else:
      print("Operación cancelada")

def mostrarlibros():
  if not libros:
    print("------------------------------------ No hay libros disponibles ------------------------------------")
  else:
    print("------------------------------------ Libros disponibles ------------------------------------")
    print(f"{'ID':<3} {'Título':<25} {'Autor':<25} {'ISBN':<25} {'Género':<25} {'Cantidad'}")
    print("\n".join(f"{i + 1:<3} {libro['titulo']:<25} {libro['autor']:<25} {libro['isbn']:<25} {libro['genero']:<25} {libro['cantidad']}" for i, libro in enumerate(libros)))

# funcion para agregar un usuario
def agregarUsuario():
  print("------------------------------------ Agregar usuario ------------------------------------")
  nombre = input("Ingrese el nombre del usuario: ")
  usuarioID = input("Ingrese el usuarioID del usuario: ")
  
  usuario = {
    "nombre": nombre,
    "usuarioID": usuarioID,
    "prestamo": [],
  }
  usuarios.append(usuario)
  print(f"Libro {nombre} agregado con éxito")
# funcion para editar un libro del inventario
def editarUsuario():
  mostrarUsuario()
  print("------------------------------------ Editar usuario ------------------------------------")
  usuarioID = input("Ingrese el ID del usuario que desea editar: ")
  usuario = next((user for user in libros if user['isbn'] == usuarioID), None)
  if not usuario:
    print("Usuario no encontrado")
    return
  else: 
    print(f"Usuario encontrado: {usuario['nombre']} - {usuario['usuarioID']}")
    nombre = input("Ingrese el nuevo nombre del usuario: ")
    usuario["nombre"] = nombre
    print(f"Usuario {usuario} editado con éxito")
    print(f"Nuevo usuario: {usuario['nombre']} - {usuario['usuarioID']}")

# funcion para eliminar un libro del inventario
def eliminarUsuario():
  print("------------------------------------ Eliminar usuario ------------------------------------")
  mostrarUsuario()
  usuarioID = input("Ingrese el ID del usuario que desea eliminar: ")
  global usuarios
  usuarios = [user for user in usuarios if user['isbn'] != usuarioID]
  print(f"El Usuario con ID: {usuarioID} ha sido eliminado")

def mostrarUsuario():
  if not usuarios:
    print("------------------------------------ No hay usuarios disponibles ------------------------------------")
  else:
    print("------------------------------------ Usuarios disponibles ------------------------------------")
    print(f"{'Nombre':<25} {'UsuarioID':<25}")
    print("\n".join(f"{usuario['nombre']:<25} {usuario['usuarioID']:<25}" for usuario in (usuarios)))

# funcion para prestar un libro
def prestamoLibro():
  mostrarlibros()
  isbn = input("Ingrese el ISBN del libro que desea eliminar: ")
  libro = next((libro for libro in libros if libro['isbn'] == isbn), None)
  if not libro:
    print("Libro no encontrado")
    return
  if libro["cantidad"] == 0:
    print("No hay libros disponibles")
    return
  mostrarUsuario()
  usuarioID = input("Ingrese el ID del usuario que desea prestar el libro: ")
  usuario = next((user for user in usuarios if user['usuarioID'] == usuarioID), None)
  if not usuario:
    print("Usuario no encontrado")
    return
  libro["cantidad"] -= 1
  usuario["prestamo"].append(libro)
  print(f"Libro {libro['titulo']} prestado a {usuario['nombre']}")

# funcion para devolver un libro
def devolucionLibro():
  mostrarUsuario()
  usuarioID = input("Ingrese el ID del usuario que desea prestar el libro: ")
  usuario = next((user for user in usuarios if user['usuarioID'] == usuarioID), None)
  if not usuario:
    print("Usuario no encontrado")
    return
  if not usuario["prestamo"]:
    print("El usuario no tiene libros prestados")
    return
  print("Libros prestados por el usuario")
  print(f"{'ID':<3} {'Título':<25} {'Autor':<25} {'ISBN':<25} {'Género':<25} {'Cantidad'}")
  print("\n".join(f"{i + 1:<3} {libro['titulo']:<25} {libro['autor']:<25} {libro['isbn']:<25} {libro['genero']:<25} {libro['cantidad']}" for i, libro in enumerate(usuario["prestamo"])))
  opcion = int(input("Ingrese el ID del libro que desea devolver: "))
  if 1 <= opcion <= len(usuario["prestamo"]):
    libroDevuelto = usuario["prestamo"].pop(opcion - 1)
    libro = next((libro for libro in libros if libro['titulo'] == libroDevuelto), None)
    if libro:
      libro["cantidad"] += 1
    print(f"Libro {libro['titulo']} devuelto por {usuario['nombre']}")
  else:
    print("Opción inválida")

# funcion para mostrar los libros prestados
def informeLibros():
  print("------------------------------------ Informe de libros prestados ------------------------------------")
  for usuario in usuarios:
    if usuario["prestamo"]:
      print(f"Usuario: {usuario['nombre']}")
      print(f"{'Título':<25} {'Autor':<25} {'ISBN':<25} {'Género':<25} {'Cantidad'}")
      print("\n".join(f"{libro['titulo']:<25} {libro['autor']:<25} {libro['isbn']:<25} {libro['genero']:<25} {libro['cantidad']}" for libro in usuario["prestamo"]))
    else:
      print(f"Usuario: {usuario['nombre']} no tiene libros prestados")

def main():
  while True: 
    print("------------------------------------ Bienvenido al sistema de gestión de libros de la biblioteca ------------------------------------")
    print("1. Agregar libro")
    print("2. Editar libro")
    print("3. Eliminar libro")
    print("4. Mostrar libros")
    print("5. Agregar usuario")
    print("6. Editar usuario")
    print("7. Eliminar usuario")
    print("8. Mostrar usuarios")
    print("9. Prestamo de libro")
    print("10. Devolución de libro")
    print("11. Informe de libros prestados")
    print("0. Salir")
    
    seleccion = int(input("Seleccione una opción: "))
    
    if seleccion == 0:
      print("Gracias por usar el sistema de gestión de libros de la biblioteca")
      break
    elif seleccion == 1:
      agregar_libro()
    elif seleccion == 2:
      editar_libro()
    elif seleccion == 3:
      eliminar_libro()
    elif seleccion == 4:
      mostrarlibros()
    elif seleccion == 5:
      agregarUsuario()
    elif seleccion == 6:
      editarUsuario()   
    elif seleccion == 7:
      eliminarUsuario()
    elif seleccion == 8:
      mostrarUsuario()
    elif seleccion == 9:
      prestamoLibro()
    elif seleccion == 10:
      devolucionLibro()
    elif seleccion == 11:
      informeLibros()
    

main()