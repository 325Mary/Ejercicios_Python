'''Dada la siguiente secuencia, hallar la expresión matemática para  realizar el  calculo
de tal forma que el  usuario  pueda  ingresar un numero y  la  calcule la secuencia
hasta ese numero ingresado1 2 4 8 16 32 64 128 256 512 1024 2048 ......si el  usuario
ingresa 200 debe mostrar la  secuencia  así,  1 2 4 8 16 32 64 128'''

numero = int(input("Ingrese el número para calcular la secuencia: "))

for n in range(1, numero+1):
    termino = 1 * 2**(n-1)
    if termino > numero:
        break
    print(termino, end=" ")