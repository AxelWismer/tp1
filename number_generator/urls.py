from django.urls import path
from .views import DataEntry

app_name = 'number_generator'

urlpatterns = [
    path('data/entry', DataEntry.as_view(), name='data_entry'),
]