'''Utiliza la forma matemática para calcular los numeros pares e impares imprimir la
secuencia de los  200 primeros numeros  pares partiendo desde 0'''


for n in range(201):

    if n % 2 == 0:
        print("El número es par", n)
    else:
        print("El número es impar")