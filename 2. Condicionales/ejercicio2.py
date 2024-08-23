#2 Calcular la tarifa de un taxi según la distancia recorrida.
#Condiciones: La tarifa es de $5 por el primer kilómetro, $2 por cada kilómetro adicional hasta 5 km, y $1.5 por cada kilómetro adicional después de 5 km
Distancia = float(int("Ingresa la distancia en kilometros"))
if(Distancia<= 1):
  tarifa = 5
elif (Distancia <= 5):
  tarifa = 5 + (Distancia - 1) * 2
else:
  # 5 + 4 * 2 = 13
  # 5 de la tarifa base + 4 km adicionales * 2 que cuesta cada km adicional
  tarifa = 13 + (Distancia - 5) * 1.5
