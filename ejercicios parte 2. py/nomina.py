'''se desea obtener la nomina semanal --salario neto-- de los empleados de una empresa cuyo
trabjo se paga a una tarifa determinada que se debe introducir por teclado al igual que el numero
de horas y el nombre del trabajador,
-las horas <= 35 hrs (normales), se pagan a una tarifa determinada que se debe introducir por teclado
al igual que el numero de hrs y nombre de trabajador
- las hrs >35 hrs se pagaran como extras a un promedio de 1.5 hrs normales
- los impuestos a deducir a los trabajadores varian en funcion de sus sueldo mensual
  *sueldo <= 2.000, libre de impuestos
  *los siguientes 220 euros al 20 por 100
  *el resto, al 30 por 300'''


nombre = input("ingrese el nombre del trabajador: ")
tarifa = int(input("ingrese tarifa: "))
horas = int(input("ingrese las horas: "))
salario = horas* tarifa
impuesto = 0
salarioNeto = salario - impuesto

while horas > 0:
    if horas <=35 :
         salario = horas * tarifa
    elif horas >35:
         salario = horas * 1.5 * tarifa
    if salario <= 2000:
        print("libre de impuestos")
    elif salario <= 2220:
        if salario <= 2220:
            impuesto = (salario - 2000)* 0,20
        else :
            impuesto = (salario - 22200) * 0.30
    break
print("nombre:", nombre ,
"su salario es: ", salarioNeto,
"con impuestos de: ", impuesto,
"para un total de: ", salarioNeto)
