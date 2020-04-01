from django.db import models
import math
# Create your models here.
def truncate(number, digits) -> float:
    stepper = 10.0 ** digits
    return math.trunc(stepper * number) / stepper


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

    METHOD_CHOICES = (('Mi', 'Congruencial Mixto'), ('Mu', 'Congruencial Multiplicativo'))
    method = models.CharField(u'Metodo', max_length=2, choices=METHOD_CHOICES, default=METHOD_CHOICES[0][0])

    @property
    def numbers(self):
        return self.number_set.all()

    # De acurdo al metodo seleccionado genera el numero correcto
    def next_number(self):
        if self.method == 'Mi':
            return self.cong_mix()
        else:
            return self.cong_multiple()

    # Calcula el siguiente numero segun el metodo congruencial mixto
    def cong_mix(self):
        # Calcula el nuevo valor de x
        self.x = (self.a * self.x + self.c) % self.m
        # Obtiene el numero truncado a 4 cifras
        num = truncate(self.x / self.m, 4)
        # Lo agrego a la coleccion de numeros y lo devuelvo para utilizarlo
        Number(value=num, data=self).save()
        return num

    # No realiza la suma de c
    def cong_multiple(self):
        # Calcula el nuevo valor de x
        self.x = (self.a * self.x) % self.m
        # Obtiene el numero truncado a 4 cifras
        num = truncate(self.x / self.m, 4)
        # Lo agrego a la coleccion de numeros y lo devuelvo para utilizarlo
        Number(value=num, data=self).save()
        return num

    def __str__(self):
        return "x: " + str(self.x) + " c: " + str(self.c) + " a: " + str(self.a) + " m: " + str(self.m) + " k: " + str(self.k) + " g: " +\
               str(self.g) + " metodo: " + str(self.method)


class Number(models.Model):
    value = models.FloatField(u'valor',max_length=4)
    data = models.ForeignKey("Data", on_delete=models.CASCADE, verbose_name='Data')

    def __str__(self):
        return str(self.value)