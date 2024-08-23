"""Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:

Menos de 100.000 COP 5%
Entre 100.000 COP y 200.000 COP 15%
Entre 200.000 COP y 350.000 COP 20%
Entre 350.000 COP y 600.000 COP 30%
Más de 600000 COP.  45%"""

declaracionRenta = float(input("ingresa tu declaracion: "))
impuestos = 0

if(1 <= declaracionRenta <= 100000):
  impuestos = declaracionRenta * 0.05
elif(100001<= declaracionRenta <=200000):
  impuestos = declaracionRenta * 0.15
elif(200001 <= declaracionRenta <= 350000):
  impuestos = declaracionRenta * 0.2
elif(350001 <= declaracionRenta <= 600000):
  impuestos = declaracionRenta * 0.3
elif(declaracionRenta < 600001 ):
  impuestos = declaracionRenta * 0.45
else: 
  print("ingresaste el mal tu declaracion")


declaracionTotal = declaracionRenta - impuestos
print(f"Su declaracion de renta por valor de {declaracionRenta} se le aplico un porcentaje de impuestos por un impuestos de {impuestos} para un total de: {declaracionTotal}")