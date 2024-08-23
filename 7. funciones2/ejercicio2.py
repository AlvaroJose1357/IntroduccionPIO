'''Funciónes Anidades para Validar y Filtrar Datos'''

def procesar_numeros(numeros:list):
    def es_positivo(n):
        return n > 0

    def filtro_pro(lista):
        totalPositivos = 0
        totalNegativos = 0

        for numero in lista:
            if es_positivo(numero):
                totalPositivos += numero
            else:
                totalNegativos += numero

        '''
        Ejemeplos Diccionario
        return {
            "Positivos": totalPositivos,
            "Negativos": totalNegativos
            }
        '''
        return [totalPositivos,totalNegativos]

    return filtro_pro(numeros)

numeros = [-6,5,-4,5,4]

resultados = procesar_numeros(numeros)
'''
Ejemeplos Diccionario
print(f"La suma de números positivos es: {resultados["Positivos"]}")
print(f"La suma de números negativos es: {resultados["Negativos"]}")
'''
print(f"La suma de números positivos es: {resultados[0]}")
print(f"La suma de números negativos es: {resultados[1]}")