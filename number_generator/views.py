from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
# Create your views here.
# Forms
from .forms import DataForm
from .models import Data
import math


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
    model = Data
    template_name = 'number_generator/data_detail.html'
    data = get_object_or_404(Data, pk=pk)
    context = {}
    context['object'] = data
    context['numbers'] = data.number_set.all()
    return render(request, template_name, context)


# Agrega el proximo numero a la lista
def add_number(request, pk):
    data = get_object_or_404(Data, pk=pk)
    data.next_number()
    data.save()
    return data_detail(request, data.pk)
