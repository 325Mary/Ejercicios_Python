'''Modificar el programa anterior para que solamente permita una cantidad fija de
intentos.'''

usuario = input("Ingrese su nombre de usuario: ")
contraseña = input("Ingrese su contraseña: ")
intentos= 0           
while intentos <3:
    print("ingrese sus datos")
    print("Usuario")
    usu = input()
    print("Contraseña")
    cont = input()



    if usu == usuario and cont == contraseña:
        print("Acceso permitido")
        break
    else:
        print("Datos incorrectos!!!")
        intentos +=1

        if intentos ==1 :
            print("Intentelo nuevamente")
            
        elif intentos ==2 :
            print("Ultimo intento")
           
        elif intentos == 3:
            print("Hasta luego")
            break


        


