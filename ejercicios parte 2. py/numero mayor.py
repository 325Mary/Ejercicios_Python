'''elabora un programa que me muestre en pantalla cual de los dos numeros ingresados por teclado es mayor'''

n1 = int(input("ingresa n1: "))
n2 = int(input("ingresa n2: "))

if n1>n2:
  print("El primer numero es mayor")
elif n1<n2:
  print("El segundo numero es mayor.")
else :
    print ("es el mismo numero")