'''Elabora un programa que Dados tres números deduzca cuál es el central'''
n1 = int( input("Ingresar n1: "))
n2 = int( input("Ingresar n2: "))
n3 = int( input("Ingresar n3: "))

if n1 > n2 and n1 > n3:
    print("numero central es : ", n1)
elif n2 > n1 and n2 < n3:
    print("numero central es : ", n2)
else: 
    print("numero central es : ", n3)