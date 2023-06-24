'''Calcular la raíz cuadrada de un número y escribir su resultado. Considerando el caso
en que el número sea negativo'''

n = int(input("Ingresa el numero: "))

import math
#math, proporciona una función llamada math.sqrt() que puede ser utilizada para calcular la raíz cuadrada de un número.
raiz = math.sqrt(n)

if n == 0 :
    print("OPERACION IMPOSIBLE!!!!!!")
print("La raiz cuadra de ", n , " es", raiz)