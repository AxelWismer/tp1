from django.db import models
import math
import random
import csv
# Create your models here.
def truncate(number, digits) -> float:
    stepper = 10.0 ** digits
    return math.trunc(stepper * number) / stepper

def list_to_string(list):
    return ",".join([str(x) for x in list]) + ','

def string_to_list(string):
    start = 0
    list = []
    for i in range(len(string)):
        if string[i] == ',':
            list.append(float(string[start:i]))
            start = i + 1
    return list

class Data(models.Model):
    class Meta:
        verbose_name = 'Dato'
        verbose_name_plural = 'Datos'

    x = models.PositiveIntegerField(u'Semilla "X0"', default=0)
    c = models.PositiveIntegerField(u'constante aditiva "c"', blank=True, null=True, default=0)
    # Se deben elegir estos
    a = models.PositiveIntegerField(u'constante multiplicativa "a"', blank=True, null=True, default=0)
    m = models.PositiveIntegerField(u'modulo "m"', blank=True, null=True, default=0)
    # O estos y los anteriores se calculan automaticamente
    k = models.PositiveIntegerField(u'coeficiente "k" que modifica a "a"', blank=True, null=True, default=0)
    g = models.PositiveIntegerField(u'coeficiente "g" que modifica a "m"', blank=True, null=True, default=0)
    numbers_csv = models.TextField(u'Numeros en formato csv', default='')

    METHOD_CHOICES = (('Mi', 'Congruencial Mixto'), ('Mu', 'Congruencial Multiplicativo'))
    method = models.CharField(u'Metodo', max_length=2, choices=METHOD_CHOICES, default=METHOD_CHOICES[0][0])

    # Chi-Cuadrado
    number_amount = models.PositiveIntegerField(u'Cantidad de numeros', default=0)
    INTERVAL_CHOICES = ((5, '5'), (10, '10'), (15, '15'), (20, '20'))
    interval_amount = models.PositiveSmallIntegerField(u'cantidad de intervalos', choices=INTERVAL_CHOICES, default=INTERVAL_CHOICES[0][0])
    c_acum = models.FloatField('c acumulado', max_length=4, default=0)
    @property
    def numbers(self):
        return string_to_list(self.numbers_csv)

    @property
    def intervals(self):
        return self.interval_set.all()

    # De acurdo al metodo seleccionado genera el numero correcto
    def next_number(self):
        if self.method == 'Mi':
            self.cong_mix()
        else:
            self.cong_multiple()

    def add_number(self, number):
        numbers = self.numbers
        numbers.append(number)
        self.numbers_csv = list_to_string(numbers)

    # Calcula el siguiente numero segun el metodo congruencial mixto
    def cong_mix(self):
        # Calcula el nuevo valor de x
        self.x = (self.a * self.x + self.c) % self.m
        # Obtiene el numero truncado a 4 cifras
        num = truncate(self.x / self.m, 4)
        self.add_number(num)

    # No realiza la suma de c
    def cong_multiple(self):
        # Calcula el nuevo valor de x
        self.x = (self.a * self.x) % self.m
        # Obtiene el numero truncado a 4 cifras
        num = truncate(self.x / self.m, 4)
        # Lo agrego a la coleccion de numeros y lo devuelvo para utilizarlo
        # Number(value=num, data=self).save()
        self.add_number(num)


    # Chi-Cuadrado
    def generate_random_numbers(self):
        for i in range(self.number_amount):
            # Number(value = truncate(random.random(), 4), data=self).save()
            self.add_number(truncate(random.random(), 4))

    def set_intervals(self):
        interval_len = 1 / self.interval_amount
        frec_esperada = self.number_amount / self.interval_amount
        intervals = [0] * self.interval_amount
        self.c_acum = 0
        # Defino cada intervalo pasando sus atributos y los datos necesarios para calcular c y la frecuencia observada
        for i in range(self.interval_amount):
            intervals[i] = interv = Interval(interval_number=i, minimum= round(i * interval_len, 4), maximum=round((i + 1) * interval_len - 0.0001, 4),
                                    frec_esperada=frec_esperada, data=self)
            interv.set_frec_observada()
            self.c_acum = interv.set_c(self.c_acum)


    def __str__(self):
        return "x: " + str(self.x) + " c: " + str(self.c) + " a: " + str(self.a) + " m: " + str(self.m) + " k: " + str(self.k) + " g: " +\
               str(self.g) + " metodo: " + str(self.method)



class Interval(models.Model):
    interval_number = models.PositiveIntegerField(u'numero de intervalo')
    minimum = models.FloatField(u'minimo',max_length=4)
    maximum = models.FloatField(u'maximo',max_length=4)
    frec_esperada = models.IntegerField(u'frecuencia esperada', default=0)
    frec_observada = models.IntegerField(u'frecuencia observada', default=0)
    data = models.ForeignKey("Data", on_delete=models.CASCADE, verbose_name='Data')
    c = models.FloatField(u'c', max_length=4)

    @property
    def calculo_1(self):
        return self.frec_observada - self.frec_esperada

    @property
    def calculo_2(self):
        return truncate(self.calculo_1 ** 2, 4)

    @property
    def calculo_3(self):
        return truncate(self.calculo_2 / self.frec_esperada, 4)

    def set_c(self, c_prev):
        self.c = truncate(self.calculo_3 + c_prev, 4)
        self.save()
        return self.c

    def set_frec_observada(self):
        self.frec_observada = 0
        for num in self.data.numbers:
            if self.minimum <= num <= self.maximum:
                self.frec_observada += 1