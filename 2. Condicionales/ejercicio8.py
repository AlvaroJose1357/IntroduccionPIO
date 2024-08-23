#8 Calcular el precio final de una compra con descuento.
#Condiciones: Si el total es mayor a $100, se aplica un 10% de descuento. Si es mayor a $200, se aplica un 20% de descuento. Si es mayor a $500, se aplica un 30% de descuento.
total = float(input("Ingresa el total de la compra: "))
descuento = 0
valorTotal = 0
if(100 < total < 199):
  descuento = total * 0.10
elif(200 < total < 499):
  descuento = total * 0.20
elif(total > 500):
  descuento = total * 0.30
valorTotal = total - descuento

print(f"El total de la compra es de ${total}, con un descuento de ${descuento} para un total de ${valorTotal}.")