'''Modificar el programa anterior para que sea una función que devuelva si el usuario
ingresó o no la contraseña correctamente, mediante un valor booleano (True o False).'''

def verificacion(cont):

    import time
    usuario = input("Ingrese su nombre de usuario: ")
    contraseña = input("Ingrese su contraseña: ")
    intentos= 0 
    tiempo_de_espera = 5
    factor_incremento = 2          
    while intentos <3:

        print("ingrese sus datos")
        print("Usuario")
        usu = input()
        print("Contraseña")
        cont = input()



        if usu == usuario and cont == contraseña:
            print("Acceso permitido")
            break
            return  True
        else:
            print("Datos incorrectos!!!")
            intentos +=1
        

            if intentos ==1 :
                print("Intentelo nuevamente")
                time.sleep(tiempo_de_espera)
            
                
            elif intentos ==2 :
                print("Ultimo intento")
                tiempo_de_espera *= factor_incremento
            elif intentos == 3:
                print("Hasta luego")
                tiempo_de_espera *= factor_incremento
                return False
autenticado = verificacion("cont")
if autenticado:
     print("Ingresos los datos correctamente")
else: 
        print("ingreso la incorrectamente la contraseña")
