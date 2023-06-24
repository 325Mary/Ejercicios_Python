'''Usando la primera función, escribir una función que imprima las primeras m parejas
de números (a,b), tales que la suma de los divisores de a es igual a b y la suma de los
divisores de b es igual a a (es decir las primeras m parejas de números amigos).
Proponer optimizaciones a las funciones anteriores para disminuir el tiempo de
ejecución.'''

def suma_divisores(n):
    suma = 0
    for i in range(1, n):
        if n % i == 0:
            suma += i
    return suma

def encontrar_parejas_amigos(m):
    parejas = []
    a = 1
    while len(parejas) < m:
        b = suma_divisores(a)
        if a != b and suma_divisores(b) == a:
            parejas.append((a, b))
        a += 1
    return parejas

n = int(input("Introduce el numero: "))
resultado = suma_divisores(n)
print("La suma de los divisores de", n,"es: ", resultado)
m = int(input("Introduce el numero de parejas: "))
parejas = encontrar_parejas_amigos(m)
print("Las primeras ", m, "parejas  son:", parejas)
