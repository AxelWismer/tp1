### Script para la generacion de numeros pseudo aleatorios segun el metodo de congruencia mixta
##lucas
from .support import *

# El usuario debe elegir el k y el g >= 20
# k = 3
# g = 3
x = input_int("Ingrese la semilla: ")
k = input_int("Ingrese el valor de k: ")
g = input_int("Ingrese el valor de g: ")
c = 7
m = 2 ** g
a = 1 + 4 * k


def cong_mix():
    global a, x, c, m
    x = (a * x + c) % m
    # return truncate(x / (m-1), 4) # cambio m-1 por m para que el rango sea entre 0 y 0,9999
    return truncate(x / m, 4)

# Se itera el algoritmo obteniendo los valores de los numeros pseudo aleatorios
v = []
for i in range(20):
    v.append(cong_mix())
print(v)

print("Presione enter para ver un nuevo numero: ", end="")
while True:
    input()
    print(cong_mix(), end="")
