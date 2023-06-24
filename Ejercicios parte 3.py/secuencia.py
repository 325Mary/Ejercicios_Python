'''Realiza un programa que imprima una secuencia de numeros de uno en uno desde el
que el usuario desee, el programa debe pedirle al usuario después de que imprima un
numero en pantalla le pregunte si desea continuar o no mostrando en pantalla'''

while   True:
    n= int(input("Ingrese el numero inicial: "))
    x =int(input("Ingrese el numero final: "))
    print(n)


    opcion = input("desea continuar (s/n): ")
    if opcion == "s":
        for i in range(n, x+1):
             print(i)
        break
 