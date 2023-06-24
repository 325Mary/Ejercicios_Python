'''Al programa anterior debe modificarlo y agregarle que al final  muestre el numero
acumulado y la cantidad de numeros ingresados por el usuario'''

'''acumulador= 0
cant_Num = 0
while True != 0:
    
    numero = int(input("Ingresa un numero ('0' para salir): "))
    acumulador += 1
    cant_Num += numero

    if numero == 0:
        break
print("El numero acumulado es: ", acumulador)
print("Cantidad de números ingresados:", cant_Num)'''

acumulador = 0
cantidad_numeros = 0

while True :
    
    numero = int(input("Ingresa un numero ('0' para salir): "))
    acumulador += 1

    if numero != 0:
        
        cantidad_numeros +=1 
        
    elif numero == 0:
        break
  


print("El número acumulado es:", acumulador)
print("Cantidad de números ingresados:", cantidad_numeros)