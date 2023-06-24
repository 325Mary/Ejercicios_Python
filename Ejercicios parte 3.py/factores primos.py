'''Escribir una aplicación que reciba un número entero k e imprima su descomposición
en factores primos.'''

x= 2
n = int(input("Ingresar el numero a calcular factores primos: "))

while n != 0:
    if n % x ==0:
        print(str(x) + "")
        n = n / x
    else:
        x = x+1
