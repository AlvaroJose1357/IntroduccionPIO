'''Crea una función llamada fibonacci que reciba un número n y 
devuelva el n-ésimo número de la secuencia de Fibonacci utilizando 
recursión.'''

def fibonacci(n: int) :
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Ejemplo de uso
numero = int(input("Ingrese un número: "))
print(f"El {numero}-ésimo número de la secuencia de Fibonacci es: {fibonacci(numero)}")