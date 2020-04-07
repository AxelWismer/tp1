from django.urls import path
from .views import DataEntry, add_number, ChiEntry

app_name = 'number_generator'

urlpatterns = [
    path('data/entry', DataEntry.as_view(), name='data_entry'),
    path('data/add_number/<int:pk>', add_number, name='data_add_number'),
    path('chi/entry', ChiEntry.as_view(), name='chi_entry'),
]