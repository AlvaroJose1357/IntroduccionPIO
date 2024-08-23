#5 Clasificar a un estudiante según su calificación.
#Condiciones: Si la calificación es 90 o más, el estudiante tiene una "A". Si está entre 80 y 89, tiene una "B". Si está entre 70 y 79, tiene una "C". Si está entre 60 y 69, tiene una "D". Si es menor a 60, tiene una "F".
calificacion = float(input("Ingrese la calificación del estudiante (0-100): "))
if 0 <= calificacion <= 100:
    if calificacion >= 90:
        print("Tienes una 'A'.")
    elif calificacion >= 80:
        print("Tienes una 'B'.")
    elif calificacion >= 70:
        print("Tienes una 'C'.")
    elif calificacion >= 60:
        print("Tienes una 'D'.")
    else:
        print("Tienes una 'F'.")
else:
    print("Calificación no válida. Debe estar entre 0 y 100.")
