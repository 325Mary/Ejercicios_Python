'''Se desea obtener la nómina semanal —salario neto— de los empleados de una
empresa cuyo trabajo se paga por horas y del modo siguiente:
las horas inferiores o iguales a 35 horas (normales) se pagan a una tarifa
determinada que se debe introducir por teclado al igual que el número de horas y el
nombre del trabajador,
las horas superiores a 35 se pagarán como extras a un promedio de 1,5 horas
normales,
los impuestos a deducir a los trabajadores varían en función de su sueldo mensual:
sueldo <= 2.000, libre de impuestos,
las siguientes 220 euros al 20 por 100,
el resto, al 30 por 100.'''
nombre = input("Ingresar nombre: ")
horas_sem = int(input("Ingresar horas  por semana: "))
tarifa = float(input("Ingresar tarifa: "))
horas_extras = horas_sem - 35
salario_sem = 0
impuesto = 0

if horas_sem <= 35 :
    salario_sem = horas_sem * tarifa
elif horas_sem > 35 :
    salario_sem = (35* tarifa) + (horas_extras * 1.5) * tarifa
salario_mes = salario_sem * 4

if salario_mes <= 2000:
    impuesto = 0
elif salario_mes > 2000 and salario_mes <= 2220:
    impuesto = salario_mes* 0.20
elif salario_mes> 2220 :
    impuesto = salario_mes * 0.30

salario_neto = (salario_mes - impuesto)
print("nombre: ", nombre, "Total salario mensual: ", salario_neto, "impuesto : ", impuesto)

