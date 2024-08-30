import os
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

def limpiarTerminal():
    if os.name == 'nt': os.system('cls') #Windows
    else: os.system('clear') #Linux o Mac

def ver_productos():
  print("-------------------------Productos Disponibles-------------------------")
  print("\n".join(f"Nombre: {p['nombre']} Precio: {p['precio']} Stock: {p['stock']}" for p in productos))

  # for producto in productos:
  #   print(f"Nombre: {producto['nombre']} Precio: {producto['precio']} Stock: {producto['stock']}")

def ver_carrito():
  print("-------------------------Productos en el carrito-------------------------")
  if not carrito:
    print("Carrito vacío")
  else:
    # headers = ["ID","Nombre", "Cantidad", "Precio"]
    # rows = [[i + 1, item['nombre'], item['cantidad'], item['precio']] for i, item in enumerate(carrito)]
    # print(tabulate(rows, headers, tablefmt="github"))
    carrito_info = [f"Nombre: {item['nombre']} Cantidad: {item['cantidad']} Precio: {item['precio']}" for item in carrito]
    print("\n".join(carrito_info))
    # for item in carrito:
    #   print(f"Nombre: {item['nombre']} Cantidad: {item['cantidad']} Precio: {item['precio']}")

def add_productosCarrito(nombre, cantidad):
  # recorre 
  producto = next((p for p in productos if p['nombre'] == nombre), None)
  itemCarrito = next((c for c in carrito if c['nombre'] == nombre), None)
  if producto:
    if producto['stock'] >= cantidad:
      if itemCarrito:
        itemCarrito['cantidad'] += cantidad
        itemCarrito['precio'] = producto['precio'] * itemCarrito['cantidad']
        producto['stock'] -= cantidad
        print("Producto agregado al carrito")
      else:
        carrito.append({
          "nombre": nombre, 
          "cantidad": cantidad, 
          "precio": producto['precio'] * cantidad})
        producto['stock'] -= cantidad
        print("Producto agregado al carrito")
    else:
      input("No hay suficiente stock. Enter para continuar")
  else:
    input("Producto no encontrado. Enter para continuar")
  
  # for producto in productos:
  #   if producto['nombre'] == nombre:
  #     if producto['stock'] >= cantidad:
  #       carrito.append({"nombre": nombre, "cantidad": cantidad, "precio": producto['precio']})
  #       producto['stock'] -= cantidad
  #       print("Producto agregado al carrito")
  #     else:
  #       print("No hay suficiente stock")
  #     break

def remove_productosCarrito():
  pass

def vaciarCarrito():
  carrito.clear()
  print("Carrito vaciado")
def comprar_Productos():
  pass

def main():
  while True:
    print("-------------------------Bienvenidos al E-Commerce-------------------------")
    print("1. Ver productos")
    print("2. Ver carrito")
    print("3. Agregar productos al carrito")
    print("4. Eliminar productos del carrito")
    print("5. Vaciar carrito")
    print("6. Comprar productos")
    print("7. Salir")
    opcion = int(input("Ingrese la opcion:\n"))
    limpiarTerminal()
    if opcion == 1:
      ver_productos()
      input("Enter para continuar")
      limpiarTerminal()
    elif opcion == 2:
      ver_carrito()
      input("Enter para continuar")
      limpiarTerminal()
    elif opcion == 3:
      print("-------------------------Agregando productos al carrito-------------------------")
      nombre = input("Ingrese su nombre:\n")
      cantidad = int(input("Ingrese la cantidad de productos:\n"))
      add_productosCarrito(nombre, cantidad)
      ver_carrito()
      input("Enter para continuar")
      limpiarTerminal()
    elif opcion == 4:
      remove_productosCarrito(nombre)
      ver_carrito()
      input("Enter para continuar")
      limpiarTerminal()
    elif opcion == 5:
      vaciarCarrito()
    elif opcion == 6:
      comprar_Productos()
    elif opcion == 7:
      print("Espero verte pronto!!!")
      break
    else:
      print("Opcion invalida")
main()