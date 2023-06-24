'''Realice un programa que acumule todo numero  ingresado  por  el  usuario, el
programa  deberá  finalizar cuando el  usuario ingrese el numero 0,  el  programa  al
final  debe mostrar cual  es el numero acumulado'''

acumulador= 0
while True != 0:
    
    numero = int(input("Ingresa un numero ('0' para salir): "))
    acumulador += 1
    if numero == 0:
        break
print("El numero acumulado es: ", acumulador)