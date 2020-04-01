import random
from support import *
# Se ingresa la cantidad de datos
while True:
    try:
        num_datos = int(input("Ingrese la cantidad de numeros: "))
        break
    except ValueError:
        print("No se ingreso un numero valido")

# Genera los numeros aleatorios
datos = []
for i in range(num_datos):
    datos.append(round(random.random(), 4))

# Ejemplo para 30 numero con intervalo de 5
# datos = [0.15, 0.22, 0.41, 0.65, 0.84, 0.81, 0.62, 0.45, 0.32, 0.07, 0.11, 0.29, 0.58, 0.73, 0.93, 0.97, 0.79, 0.55, 0.35, 0.09, 0.99, 0.51, 0.35, 0.02, 0.19, 0.24, 0.98, 0.1, 0.31, 0.17]
# Para estps datps ña frecuencia por intervalos tiene que dar [8, 7, 5, 4, 6]
# Y el valor de c acumulado tiene que dar 1.6667
print(datos)

# Se ingresa la cantidad de intervalos las opciones tienen que ser 5, 10, 15 y 20
num_interv = input_int("Ingrese la cantidad de intervalos: ")

# Conteo de frecuencias
intervalos = [0] * num_interv
for i in range(num_interv):
    for dato in datos:
        if i * (1 / num_interv) <= dato < (i + 1) * (1 / num_interv):
            intervalos[i] += 1

print("frecuencia por intervalos:", intervalos)

# Calculo de c
fe = num_datos / num_interv
c = []
for f0 in intervalos:
    c.append(((fe-f0) ** 2) / fe)

sumatoria = truncate(sum(c), 4)
# Se devuelve el valor de c acumulado

# No hace falta que lo eliga el usuario se elige un error de 0.5
tabla = [18.4662, 16.4238, 14.8602, 13.2767, 11.1433, 9.4877, 7.7794]
while True:
    print("Seleccione el porcentaje de error")
    print("1- 0,001")
    print("2- 0,0025")
    print("3- 0,005")
    print("4- 0,01")
    print("5- 0,025")
    print("6- 0,05")
    print("7- 0,1")
    op = input_int("Seleccione: ") - 1
    if 0 <= op <= 6:
        print("El valor es:", sumatoria)
        print("El valor de tabla es:", tabla[op])
        if sumatoria < tabla[op]:
            print("No se rechaza la hipotesis")
        else:
            print("Se rechaza la hipotesis")
        break
    else:
        print("valor en rango incorrecto")
