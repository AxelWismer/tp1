from django.urls import path
from .views import DataEntry, add_number

app_name = 'number_generator'

urlpatterns = [
    path('data/entry', DataEntry.as_view(), name='data_entry'),
    path('data/add_number/<int:pk>', add_number, name='data_add_number'),
]