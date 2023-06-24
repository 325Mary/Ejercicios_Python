'''Escribir una función que devuelva la suma de todos los divisores de un número n, sin
incluirlo.'''

def suma_divisores(n):
    suma = 0
    for i in range(1, n):
        if n % i == 0:
            suma += i
    return suma

n = int(input("Introduce el numero: "))
resultado = suma_divisores(n)
print("La suma de los divisores de", n,"es: ", resultado)