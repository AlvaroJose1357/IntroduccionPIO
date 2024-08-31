import os
import time
import itertools
# Programa de venta de joyas y reloj 
productos = [{
  "nombre": "anillo de oro",
  "precio": 600,
  "stock": 15
}, {	
  "nombre": "collar de plata",
  "precio": 400,
  "stock": 10
}, {
  "nombre": "reloj de pulsera",
  "precio": 800,
  "stock": 5
}, {
  "nombre": "pendientes de diamante",
  "precio": 1000,
  "stock": 3
}, {
  "nombre": "pulsera de oro",
  "precio": 700,
  "stock": 5
}, {
  "nombre": "collar de oro",
  "precio": 900,
  "stock": 10
}, {
  "nombre": "reloj de bolsillo",
  "precio": 1200,
  "stock": 2
}, {
  "nombre": "pendientes de plata",
  "precio": 500,
  "stock": 5
}, {
  "nombre": "pulsera de plata",
  "precio": 600,
  "stock": 10
}, {
  "nombre": "collar de diamante",
  "precio": 1500,
  "stock": 3
}]

carrito = []

def limpiarTerminal():
    if os.name == 'nt': os.system('cls') #Windows
    else: os.system('clear') #Linux o Mac
    
def listProduct():
  # for i, producto in enumerate(productos):
  #   if name.lower() in producto["nombre"].lower():
  #     print(f"{i + 1}. {producto['nombre']} - Precio: ${producto['precio']} - Stock: {producto['stock']}")
  if not productos:
    print("No hay productos disponibles")
  else:
    print("-------------------------Productos Disponibles-------------------------")
    print(f"{'ID':<3} {'Nombre':<25} {'Precio':<7} {'Stock'}")
    print("\n".join(f"{i + 1:<3} {producto['nombre']:<25}{producto['precio']:<7} Stock: {producto['stock']}" for i, producto in enumerate(productos)))

def addProduct_Cart(name, cant):
  try:
    product = next((producto for producto in productos if producto["nombre"] == name), None)
    itemCart = next((cart for cart in carrito if cart["nombre"].lower() == name), None)
    if not product:
      print("Producto no encontrado. Verifica el nombre del producto")
    if product["stock"] >= cant:
      confirm = input(f"¿Desea agregar {cant} unidades de {product['nombre']} al carrito? (s/n): ").lower()
      if confirm == "s":
        if itemCart:
          itemCart["cantidad"] += cant
          itemCart["precio"]  = product["precio"] * itemCart["cantidad"]
          product["stock"] -= cant
          print(f"Se ha agregado {cant} unidades de {product['nombre']} al carrito")
        else: 
          carrito.append({
            "nombre": product["nombre"],
            "cantidad": cant,
            "precio": product["precio"] * cant
          })
          product["stock"] -= cant
          print(f"Se ha agregado {cant} unidades de {product['nombre']} al carrito")
      else:
        print("Operación cancelada")
    else:
      print("No hay suficiente stock")
  except Exception as e:
    print("Se ha presentado un error al añadir al carrito", e)

def updateCart(name, cant):
  try:
    # esta linea de código es para buscar el producto en la lista de productos
    product = next((producto for producto in productos if producto["nombre"] == name), None)
    # esta linea de código es para buscar el producto en la lista de carrito
    itemCart = next((cart for cart in carrito if cart["nombre"].lower() == name), None)
    if not itemCart:
      print("Producto no encontrado en el carrito")
    
    # Si la cantidad actual es mayor a la nueva cantidad a ingresar, disminuye y se devuelve el stock sobrante
    if itemCart["cantidad"] > cant:
      # se coloca primero la cantidad del carrito para que la cantidad no sea negativa
      diferencia = itemCart["cantidad"] - cant
      product["stock"] += diferencia
      itemCart["cantidad"] = cant
      itemCart["precio"] = product["precio"] * itemCart["cantidad"]
      print(f"La cantidad de {itemCart['nombre']} ha sido reducida a {cant} unidades.")
    
    # Si la cantidad actual es menor a la nueva cantidad a ingresar, aumenta y se resta del stock
    elif itemCart["cantidad"] < cant:
      # se coloca primero la nueva cantidad para que este no sea negativa
      diferencia = cant - itemCart["cantidad"]
      # verificamos si hay suficiente stock
      if product["stock"] >= diferencia:
        product["stock"] -= diferencia
        itemCart["cantidad"] = cant
        itemCart["precio"] = product["precio"] * itemCart["cantidad"]
        print(f"La cantidad de {itemCart['nombre']} ha sido aumentada a {cant} unidades.")
      else:
        print(f"No hay suficiente stock disponible, Solo hay {product['stock']} unidades disponibles")
    else:
      print("La cantidad ingresada es igual a la cantidad actual, por ende no se realizara la actualización")
  except Exception as e:
    print("Se ha presentado un error al actualizar el carrito", e)

def removeProduct(name):
  try:
    if not carrito:
      print("No hay productos en el carrito")
    else:
      product = next((producto for producto in productos if producto["nombre"].lower() == name), None)
      itemCart = next((cart for cart in carrito if cart["nombre"].lower() == name), None)
      if itemCart:
        confirm = input(f"¿Está seguro de eliminar {itemCart['nombre']} del carrito? (s/n): ").lower()
        if confirm == "s":
          product["stock"] += itemCart["cantidad"]
          carrito.remove(itemCart)
          print(f"Producto {product['nombre']} eliminado del carrito.")
  except Exception as e:
    print("Se ha presentado un error al eliminar del carrito", e)

def viewCart():
  if not carrito:
    print("No hay productos en el carrito")
  else:
    print("-------------------------Productos en el Carrito-------------------------")
    print(f"{'ID':<3} {'Nombre':<20} {'Cantidad':<10} {'Precio'}")
    print("\n".join(f"{i + 1:<3} {producto['nombre']:<25}{producto['cantidad']:<7} ${producto['precio']}" for i,producto in enumerate(carrito)))
    print(f"Total a pagar: ${sum(producto['precio'] for producto in carrito)}")

def finishBuy():
  if not carrito:
    print("No hay productos en el carrito")
    return
  else:
    viewCart()
    confirm = input("¿Desea finalizar la compra? (s/n): ").lower()
    if confirm == "s":
      show_loading()
      print("\nProcesando compra. Espera unos momentos..")
      show_loading()
      print("\nCompra finalizada. Gracias por su compra. Disfruta de tus productos")
    else:
      print("Operación cancelada")

def continuar():
  input("Enter para continuar........")
  limpiarTerminal()
  
def show_loading():
    total_steps = 50  # Número de pasos en la barra de carga
    barras = itertools.cycle(['|', '/', '-', '\\'])  # Ciclo infinito de barras deslizantes
    print("Cargando...", end="", flush=True)
    
    for i in range(total_steps):
        time.sleep( 5 / total_steps)
        porcentaje = (i + 1) * 100 // total_steps
        barra_progreso = "█" * (i + 1) + "-" * (total_steps - i - 1)
        barra_dinamica = next(barras)  # Obtiene el siguiente símbolo en el ciclo
        print(f"\r[{barra_progreso}] {porcentaje}% {barra_dinamica}", end="", flush=True)

def main():
  while True:
    print("------------------------- E-Commerce Joyas y Relojes -------------------------")
    print("1. Ver productos")
    print("2. Agregar producto al carrito")
    print("3. Actualizar cantidad de producto en el carrito")
    print("4. Eliminar producto del carrito")
    print("5. Ver carrito")
    print("6. Finalizar compra")
    print("7. Salir")
    try:
      opcion = int(input("Ingrese una opción: "))
      if opcion == 1:
        listProduct()
        continuar()
      elif opcion == 2:
        name = input("Ingrese el name del producto: ").lower()
        cant = int(input("Ingrese la cantidad: "))
        addProduct_Cart(name, cant)
        continuar()
      elif opcion == 3:
        name = input("Ingrese el nombre del producto a actualizar: ").lower()
        cant = int(input("Ingrese la nueva cantidad: "))
        updateCart(name, cant)
        continuar()
      elif opcion == 4:
        name = input("Ingrese el nombre del producto a eliminar: ").lower()
        removeProduct(name)
        continuar()
      elif opcion == 5:
        viewCart()
        continuar()
      elif opcion == 6:
        finishBuy()
        seguirComprando = input("¿Desea seguir comprando? (s/n): ").lower()
        if seguirComprando == "s":
          carrito.clear()
          limpiarTerminal()
        else:
          print("Gracias por su compra")
          break
      elif opcion == 7:
        print("Saliendo del programa...")
        break
      else:
        print("Opción no válida")
    except Exception as e:
      print("Se ha presentado el siguiente error en el programa principal", e)
      continuar()

main()