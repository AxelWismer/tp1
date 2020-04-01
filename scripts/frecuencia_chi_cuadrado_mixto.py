### Del metodo para la generacion de numeros pseudo aleatorios segun el metodo de congruencia mixta
k = 3
# Se debe aumentar g si se quiere aumentar el intervalo con el que se repiten los numeros
g = 7
c = 7
m = 2 ** g
a = 1 + 4 * k

# Se ingresa la semilla
while True:
    try:
        x = int(input("Ingrese la semilla: "))
        break
    except ValueError:
        print("No se ingreso un numero valido")

def cong_mix():
    global a, x, c, m
    x = (a * x + c) % m
    return round(x / (m - 1), 4)

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
    datos.append(cong_mix())
print(datos)

# Se ingresa la cantidad de intervalos
while True:
    try:
        num_interv = int(input("Ingrese la cantidad de intervalos: "))
        break
    except ValueError:
        print("No se ingreso un numero valido")

# Conteo de frecuencias
intervalos = [0] * num_interv
for i in range(num_interv):
    for dato in datos:
        if i * (1 /num_interv) <= dato < (i + 1) * (1 /num_interv):
            intervalos[i] += 1

print("frecuencia por intervalos:", intervalos)

# Calculo de c
fe = num_datos / num_interv
c = []
for f0 in intervalos:
    c.append(((fe-f0) ** 2) / fe)

# Se devuelve el valor de c acumulado
print(round(sum(c), 4))