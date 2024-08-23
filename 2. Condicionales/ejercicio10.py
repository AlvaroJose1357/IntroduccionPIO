# 10 Calcular el salario semanal de un trabajador según sus horas trabajadas.
# Condiciones: Las primeras 40 horas se pagan a tarifa normal, las horas adicionales se pagan al 1.5 de la tarifa normal.
tarifa = int(input("Ingrese el tarifa Hora"))
horasTrabajadas = int(input("Ingrese las horas trabajadas: "))

if(horasTrabajadas > 40):
  horasExtra = horasTrabajadas - 40
  tarifaExtra = horasExtra * tarifa * 1.5
  salarioTotal = (40 * tarifa) + tarifaExtra
else:
  salarioTotal = tarifa * horasTrabajadas

print(f"El salario extra es: {tarifaExtra}")
print(f"El salario total es: {salarioTotal}")