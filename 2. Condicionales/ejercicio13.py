# Calcular el impuesto a pagar según el salario.
# Condiciones: Si el salario es menor o igual a $1000, no se paga impuesto. Si es mayor a $1000 pero menor o igual a $2000, se paga un 5% del salario. Si es mayor a $2000, se paga un 10%.

salario = int(input("Ingresa tu salario: "))
impuestos = 0
salarioTotal = 0
if(0 <=  salario <= 1000):
  salario
elif (1001 <= salario <= 2000):
  impuestos = salario * 0.05
  salarioTotal = salario - impuestos
elif(salario > 2000):
  impuestos = salario * 0.1
  salarioTotal = salario - impuestos
else: 
  print("DaTo invalido")
print(f"tu salario de {salario} - {impuestos} da como total: {salarioTotal}")