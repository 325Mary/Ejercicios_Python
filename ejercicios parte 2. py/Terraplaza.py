'''Tatiana tiene  ganas  de salir  con su amiga Paola a tomar un cafe  pero ella  sabe
que si va al  centro comercial Campanario deberá pagar transporte ida y regreso  y los
cafes de ambas, pero  si va a Terraplaza se ahorra el transporte,  pero  tambien debe
tener encuenta que  el  cafe  en Terraplaza es 2 veces mas costoso que en
campanario el cual  tiene un costo de 4000 y tambien cuenta con  20000 el  tranporte
seria en bus por un valor  de 1600  el  programa le debe decir a Tatiana cual seria la
mejor opcion que debe tomar'''

Transporte = 1600 * 4
cafeTerraplaza = 8000 
monetaria= 20000
cafeCampanario= 4000
terraplaza = (cafeTerraplaza* 2)
campanario = (cafeCampanario * 2) + Transporte 

if campanario < terraplaza:
    print("La mejor opcion es Campanario.")
else:
    print("La mejor opcion es Terraplaza.")