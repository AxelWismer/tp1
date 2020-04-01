### Script para la generacion de numeros pseudo aleatorios segun el metodo de congruencia multiplicativa
from support import *

# k = 2
# g = 7
x = input_int("Ingrese la semilla: ")
k = input_int("Ingrese el valor de k: ")
g = input_int("Ingrese el valor de g: ")
m = 2 ** g
a = 3 + 8 * k

def cong_multiple():
    global a, x, m
    x = (a * x) % m
    return truncate(x / (m - 1), 4)


# Se itera el algoritmo obteniendo los valores de los numeros pseudo aleatorios
v = []
for i in range(20):
    v.append(cong_multiple())
print(v)

print("Presione enter para ver un nuevo numero: ", end="")
while True:
    input()
    print(cong_multiple(), end="")
