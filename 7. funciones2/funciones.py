def funciones_Externa(mensaje):
  print(f"mensaje desde la función externa: {mensaje}")
  
  def funcion_Interna():
    print(f"mensaje desde la función interna: {mensaje}")
  funcion_Interna()

funciones_Externa("Hola mundo")