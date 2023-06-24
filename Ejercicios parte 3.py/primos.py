'''Escribir una aplicación que reciba un número natural e imprima todos los números
primos que hay hasta ese número.'''

numero = int(input("Ingrese un número natural: "))

print("Números primos en el número", numero, "son :")

for i in range(2, numero + 1):
    es_primo = True
    
    
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            es_primo = False
            break
    
    if es_primo:
        print(i)

