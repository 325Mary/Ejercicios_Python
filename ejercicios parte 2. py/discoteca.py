'''Elabora un programa para una discoteca que necesita controlar el acceso a las
personas la  cual pida el nombre a una persona y su edad, en caso  que  sea  mayor
de  18  lo deje ingresar, si es  menor  de edad debe  mostrar un  mensaje diciendole
que no puede ingresar y si  tiene 18 años  debera  preguntar por su  identificación'''

nombre = input("Ingrese el nombre: ")
edad = int(input("Ingrese la edad: "))

if edad > 18 :
    print("Ingreso permitido")
elif edad == 18 :
    identificacion = int(input("ingrese su identificacion: "))
    if identificacion > 0: 
        print("Ingreso permitido.")
    elif identificacion == 0: 
        print("Acceso denegado.")
else: 
    print("Acceso Denegado.!!")