from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
# Create your views here.
# Forms
from .forms import DataForm, ChiForm, ChiMixForm
from .models import Data
import math
import numpy as np
import matplotlib.pyplot as plt


class DataEntry(generic.FormView):
    model = Data
    form_class = DataForm
    template_name = 'number_generator/data_form.html'

    def form_valid(self, form):
        data = self.object = form.save()
        # Si no se completa a o m se calculan los valores con k y g
        if data.a == 0:
            if data.method == 'Mi':
                data.a = 1 + 4 * data.k
            else:
                data.a = 3 + 8 * data.k
        if data.m == 0:
            data.m = 2 ** data.g
        # Guardo el valor de la semilla de x
        data.semilla = data.x
        # Crea los primeros 20 valores de data
        for i in range(20):
            data.next_number()
        data.save()
        return data_detail(self.request, data.pk)


# Muestra todos los numeros creados hasta el momento
def data_detail(request, pk):
    template_name = 'number_generator/data_detail.html'
    data = get_object_or_404(Data, pk=pk)
    context = {}
    context['object'] = data
    context['numbers'] = data.numbers
    return render(request, template_name, context)


# Agrega el proximo numero a la lista
def add_number(request, pk):
    data = get_object_or_404(Data, pk=pk)
    data.next_number()
    data.save()
    return data_detail(request, data.pk)


# CHI cuadrado
class ChiEntry(generic.FormView):
    model = Data
    form_class = ChiForm
    template_name = 'number_generator/chi_form.html'

    def form_valid(self, form):
        data = self.object = form.save()
        # Si no se completa a o m se calculan los valores con k y g
        data.generate_random_numbers()
        data.set_intervals()
        data.save()
        return chi_detail(self.request, data.pk)


# Muestra todos los numeros creados hasta el momento
def chi_detail(request, pk):
    template_name = 'number_generator/chi_detail.html'
    data = get_object_or_404(Data, pk=pk)
    context = {}
    context['object'] = data
    context['numbers'] = data.numbers
    context['intervals'] = data.intervals
    return render(request, template_name, context)


def add_graphic(request, pk):
    data = get_object_or_404(Data, pk=pk)
    frec_esperada = []
    for i in range(data.number_amount):
        frec_esperada.append( i / data.number_amount)
    plt.xlabel('rango')
    plt.ylabel('cant. apariciones')
    plt.title('Conteo de frecuecias')
    plt.hist([data.numbers, frec_esperada], bins=data.interval_amount, rwidth=0.9,
             label=['frecuencia observada', 'frecuencia esperada'])
    plt.legend()
    plt.show()
    return chi_detail(request, data.pk)


class ChiMixEntry(generic.FormView):
    model = Data
    form_class = ChiMixForm
    template_name = 'number_generator/chi_mix_form.html'

    def form_valid(self, form):
        data = self.object = form.save()
        # Si no se completa a o m se calculan los valores con k y g
        if data.a == 0:
            if data.method == 'Mi':
                data.a = 1 + 4 * data.k
            else:
                data.a = 3 + 8 * data.k
        if data.m == 0:
            data.m = 2 ** data.g
        # Guardo el valor de la semilla de x
        data.semilla = data.x
        # Crea los primeros 20 valores de data
        for i in range(data.number_amount):
            data.next_number()
        data.save()
        data.set_intervals()
        data.save()
        return chi_detail(self.request, data.pk)
