'''El  usuario ingresa por  teclado  una  oración por  ejemplo 'Estaba sentada la  pájara
pinta' el  programa debe  permitir contar cuantas vocales  hay en esa frase a = 9, e =
2, i = 1, o = 0, u = 0'''

def contar_vocales(oracion):
   
    oracion = oracion.lower()

    # Inicializar contadores de cada vocal
    a = 0
    e = 0
    i= 0
    o= 0
    u= 0

    for letra in oracion:
        if letra == 'a':
            a += 1
        elif letra == 'e':
            e+= 1
        elif letra == 'i':
            i+= 1
        elif letra == 'o':
            o += 1
        elif letra == 'u':
            u += 1

    print("a=",a, "e=",e, "i=",i, "o=",o, "u=",u)

oracion_usuario = input("Ingresa una oración: ")
contar_vocales(oracion_usuario)