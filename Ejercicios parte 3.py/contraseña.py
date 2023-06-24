'''Escribir un programa que contenga una contraseña inventada, que le pregunte al
usuario la contraseña, y no le permita continuar hasta que la haya ingresado
correctamente.'''

usuario = input("Ingrese su nombre de usuario: ")
contraseña = input("Ingrese su contraseña: ")
print("Bienvenido ingrese sus datos")
print("Usuario")
usu = input()
print("Contraseña")
cont = input()


if usu == usuario and cont == contraseña:
    print("Acceso permitido")
else:
    print("Datos incorrectos!!!")

