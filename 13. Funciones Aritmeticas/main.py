import os
# productos disponibles
productos = [{
  "nombre": "Laptop",
  "precio": 3000000.00,
  "stock": 5
}, {
  "nombre": "Mouse",
  "precio": 200000.00,
  "stock": 10
}, {
  "nombre": "Teclado",
  "precio": 500000.00,
  "stock": 15
}, {
  "nombre": "Monitor",
  "precio": 1500000.00,
  "stock": 3
}, {
  "nombre": "Parlantes",
  "precio": 500000.00,
  "stock": 5
}, {
  "nombre": "Audifonos",
  "precio": 150000.00,
  "stock": 10
}]

#Carrito de compras
carrito = []

#cupones de descuento
cupones = [{
  "codigo": "10OFF",
  "descuento": 10,
  "min": 3000000,
  "limiteDeUso": 3
}, {
  "codigo": "20OFF",
  "descuento": 20,
  "min": 5000000,
  "limiteDeUso": 5
}, {
  "codigo": "30OFF",
  "descuento": 30,
  "min": 10000000,
  "limiteDeUso": 10
}]
#administradores
admins = [{
  "usuario": "admin",
  "contrasena": "admin"
}, {
  "usuario": "alvaro",
  "contrasena": "xd123"
}, {
  "usuario": "juant",
  "contrasena": "juanprofe123"
}]

#Funciones
def limpiarTerminal():
    if os.name == 'nt': os.system('cls') #Windows
    else: os.system('clear') #Linux o Mac

def mostrar_productos():
    pass

def clienteFuncion(nombre):
  def carrito():
    def mostrar():
      print("Mostar carrito")
    def agregar():
      print("Agregar al carrito")
    def eliminar():
      print("Eliminar del carrito")
    def actualizar():
      print("Actualizar carrito")
    def vaciar():
      print("Vaciar carrito")

  def calcular_total():
    print("Calcular total")

  def procesar_compra():
    print("Procesar compra")

def administradorFuncion(elemento,peticion):
  # Funciones de productos 
  def productos():
    def agregar():
      print("Agregar producto")
    def eliminar():
      print("Eliminar producto")

    def actualizar():
      print("Actualizar producto")
    
    if (peticion == "agregar"):
      agregar()
    elif (peticion == "eliminar"):
      eliminar()
    elif (peticion == "actualizar"):
      actualizar()

    def cupones():
      def agregar():
        print("Agregar cupon")

      def eliminar():
        print("Eliminar cupon")

      def actualizar():
        print("Actualizar cupon")
        
      if (peticion == "agregar"):
        agregar()
      elif (peticion == "eliminar"):
        eliminar()
      elif (peticion == "actualizar"):
        actualizar()

    if (elemento == "productos"):
      productos()
    elif (elemento == "cupones"):
      cupones()
  

def acceso(usuario, contrasena):  # función para acceder al sistema
    global continuar  # variable global para saber si se puede continuar o no
    for admin in admins:  # recorre la lista de usuarios
        if usuario.lower() == admin["usuario"] and contrasena.lower() == admin["contrasena"]:  
          # si el usuario y la contraseña son iguales a los de la lista
            continuar = True  # se puede continuar
            print("Acceso concedido al sistema, Bienvenido", usuario)  # imprime que se puede continuar
            break  # se sale del ciclo
        else:
            continuar = False  # si no se puede continuar
            print("Usuario y/o contraseña incorrectos")  # imprime que no se puede continuar
            break  # se sale del ciclo

def main():
  while True:
    print("------------------------- Bienvenido al e-commerce -------------------------")
    print("1. Cliente")
    print("2. Administrador")
    print("3. Salir")
    opcion = input("Elija un usuario para continuar: ")
    if opcion == "1":
      limpiarTerminal()
      print("------------------------- Bienvenido al e-commerce -------------------------")
      nombre = input("Ingrese su nombre: ")
      clienteFuncion(nombre)
    elif opcion == "2":
      limpiarTerminal()
      print("------------------------- Bienvenido al panel de administrador -------------------------")
      usuario = input("Ingrese el usuario: ")  # pide el usuario
      contrasena = input("Ingrese la contraseña: ")  # pide la contraseña
      acceso(usuario,contrasena)
      if continuar:
        while True:
          print("1. Productos")
          print("2. Cupones")
          print("3. Salir")
          opcion = input("Elija una opcion para continuar: ")
          if opcion == "1":
            while True:
              print("------------------------- Productos -------------------------")
              print("1. Agregar Producto")
              print("2. Eliminar Producto")
              print("3. Actualizar Producto")
              print("4. Salir")
              cupon = input("Elija una opcion para continuar: ")
              if cupon == "1":
                administradorFuncion("productos","agregar")
              elif cupon == "2":
                administradorFuncion("productos","eliminar")
              elif cupon == "3":
                administradorFuncion("productos","actualizar")
              elif cupon == "4":
                break
              else:
                input("Opcion no valida, presione enter para continuar")
                limpiarTerminal()
          elif opcion == "2":
            while True:
              print("------------------------- Cupones -------------------------")
              print("1. Agregar cupon")
              print("2. Eliminar cupon")
              print("3. Actualizar cupon")
              print("4. Salir")
              cupon = input("Elija una opcion para continuar: ")
              if cupon == "1":
                administradorFuncion("cupones","agregar")
              elif cupon == "2":
                administradorFuncion("cupones","eliminar")
              elif cupon == "3":
                administradorFuncion("cupones","actualizar")
              elif cupon == "4":
                break
              else:
                input("Opcion no valida, presione enter para continuar")
                limpiarTerminal()
          elif opcion == "3":
            break
          else:
            input("Opcion no valida, presione enter para continuar")
            limpiarTerminal()
    elif opcion == "3":
      print("Gracias por visitarnos")
      break
    else:
      input("Opcion no valida, presione enter para continuar")
      limpiarTerminal()

main()