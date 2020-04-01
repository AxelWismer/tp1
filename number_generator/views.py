from django.shortcuts import render
from django.views import generic
# Create your views here.
# Forms
from .forms import DataForm
from .models import Data


class DataEntry(generic.FormView):
    model = Data
    form_class = DataForm
    template_name = 'number_generator/data_form.html'

    def form_valid(self, form):
        data = self.object = form.save()
        # Si no se completa a o m se calculan los valores con k y g
        if data.a == 0 or data.m == 0:
            if data.method == 'Mi':
                data.a = 1 + 4 * data.k
            else:
                data.a = 3 + 8 * data.k
            data.m = 2 ** data.g
        print(data)
        data.delete()
        return render(self.request, self.template_name, self.get_context_data())
