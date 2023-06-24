'''Elabora un propgrama que me muestre en pantalla de forma ordenada de menor a mayor dos  numeros ingresados
por teclado, por ejemplo si ingreso 5 y 4 debera mostrar, "los numeros ingresados son 5 y 4 y organizados son 4,5'''

n1 = int(input("ingresa n1: "))
n2 = int(input("ingresa n2: "))

print(" los numeros ingresados son: ", n1, n2)

if n1 < n2 :
    print("Ordenados son: ", n1 , n2)
elif n1 > n2 :
    print("Ordenados son: ", n2 , n1)
else:
    print("Los numeros son iguales.")