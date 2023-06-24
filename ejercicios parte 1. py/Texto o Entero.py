'''Elabore un  programa me muestre en  pantalla el  tipo de  dato  que el usuario  ha
ingresado, por  ejemplo si  ingresa Juan el  deberá decir que es texto, en caso  que
ingrese 2018 deberá decir que es  entero'''

caracteres = input("ingrese algo: " )
if caracteres.isdigit():   
    print(" es numero")
else :
    print("es texto")

    