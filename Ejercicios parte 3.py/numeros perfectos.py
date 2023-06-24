'''Usando la función anterior, escribir una función que imprima los primeros m números
tales que la suma de sus divisores sea igual a sí mismo (es decir los primeros m
números perfectos).'''

'''def suma_divisores(n):
    suma = 0
    for i in range(1, n):
        if n % i == 0:
            suma += i
    return suma
def imprimir_numeros_perfectos(m):
    contador = 0
    numero = 1

    while contador < m:
        if suma_divisores(numero) == numero:
            print(numero)
            contador += 1
        numero += 1

n =int(input("Ingresar el numero para suma de los divisores: "))
m =int(input("Escriba el numero de perfectos que desea ver: "))
resultado = suma_divisores(n)
perfectos = imprimir_numeros_perfectos(m)
print("La suma de los divisores de", n,"es: ", resultado)
print("los ", m, "Perfectos son: ", perfectos)'''

def suma_divisores(n):
    suma = 0
    for i in range(1, n):
        if n % i == 0:
            suma += i
    return suma

def imprimir_numeros_perfectos(m):
    contador = 0
    numero = 1
    perfectos = []

    while contador < m:
        if suma_divisores(numero) == numero:
            perfectos.append(numero)
            contador += 1
        numero += 1

    return perfectos

n = int(input("Ingresar el número para la suma de los divisores: "))
m = int(input("Escriba el número de números perfectos que desea ver: "))

resultado = suma_divisores(n)
perfectos = imprimir_numeros_perfectos(m)
#aplica de forma rapida hasta 4 numeros perfectos, si incrementa tardara mucho mas timepo en encontrarlos.

print("La suma de los divisores de", n, "es:", resultado)
print("Los", m, "números perfectos son:", perfectos)