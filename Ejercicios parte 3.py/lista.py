'''Elabora un programa que muestre una lista de números la cual pida al usuario desde
que numero quiere y hasta que numero quiere mostrar por ejemplo si  ingresa  2  y 10
debería mostrar  2,3,4,5,6,7,8,9,10 o si  ingresa  2  y -10  debería mostrar
2,1,0,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10'''

n1 = int(input("Ingrese el numero inicial: "))
n2 = int(input("Ingrese el numero final: "))

if n1 <  n2:
    for i in range (n1, n2 + 1):
        print(i)
elif n1 > n2:
    for x in range (n1, n2 -1,-1):
        print(x)
else:
    print("Numero iguales")
