'''Realiza un programa que muestre los numeros pares desde un numero
predeterminado hasta otro numero predeterminado'''

n1 = int(input("Ingrese el numero inicial: "))
n2 = int(input("Ingrese el numero final: "))

for i in range (n1, n2):
    if i % 2 == 0:
         print("El numero ", i, "es par")

