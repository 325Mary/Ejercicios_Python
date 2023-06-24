'''Elabora un programa que lea 3 numeros por teclado y me los muestre organizados de
mayor a menor, por ejemplo si ingreso 53, 10 y 24  debera mostrar, los numeros ingresados son 53,10 y 24
y organizados de forma descendente son 53, 24, 10.'''

n1 = int(input("Ingrese el primer numero: "))
n2 = int(input("Ingrese el segundo numero: "))
n3 = int(input("Ingrese el tercer numero: "))

print("Los numeros ingresados son: ", n1, n2, n3)


if n1 > n2 and n1 > n3:
    print("Organizados de forma descendente es: ", n1, n2,n3)
elif n2 > n1 and n2 > n3:
    print("Organizados de forma descendente es : ", n2, n1, n3)
else:
    print("Organizados de forma descendente es : ", n3,n1,n2)