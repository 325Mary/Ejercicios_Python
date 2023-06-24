'''Elabore una minicalculadora que al ingresar 2 numeros me calcule el resultado de la
suma, resta, producto, division, exponenciaxion, modulo de la division'''

n1 = int(input("ingrese primer numero: "))
n2 = int(input("ingrese segundo numero: "))

opcion = 0
while True :
    print("""
    ¿qué quieres hacer?
    
    1) Sumar 
    2) Restar 
    3) Producto
    4) Division
    5) Exponenciaxion
    6) Modulo de la division
    7) apagar calculadora
    """)

    opcion = int(input("Elige una opción: ") )     

    if opcion == 1:
        print("El resultado es: " + str(n1 + n2))
    elif opcion ==2:
        print("El resultado es: " + str(n1 - n2))
    elif opcion == 3:
        print("El resultado es: " + str(n1 * n2))
    elif opcion == 4:
        print("El resultado es: " + str(n1 / n2))
    elif opcion == 5:
         if n1 == 0 and n2 < 0 :
             print("no es posible realizar la operacion")
         else :
             print("El resultado es: " + str(n1 ** n2))
    elif opcion == 6:
        print("El resultado es: " + str(n1 % n2))
    elif opcion == 7:
        break
    else:
        print("opcion incorrecta")
