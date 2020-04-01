import math


def truncate(number, digits) -> float:
    stepper = 10.0 ** digits
    return math.trunc(stepper * number) / stepper


def input_int(txt) -> int:
    while True:
        try:
            value = int(input(txt))
            break
        except ValueError:
            print("No se ingreso un numero valido")
    return value

