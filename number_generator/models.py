from django.db import models

# Create your models here.


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

    def __str__(self):
        return "x: " + str(self.x)  + " c: " + str(self.c) + " a: " + str(self.a) + " m: " + str(self.m) + " k: " + str(self.k) + " g: " +\
               str(self.g) + " metodo: " + str(self.method)