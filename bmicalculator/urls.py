from django.urls import path
from bmicalculator.views import *
app_name = "bmicalculator"
urlpatterns = [
    path('', show_bmicalculator, name="show_bmicalculator"),
    path('delete/<int:pk>/', delete_task, name="delete"),
    path('add/', add_calculate_ajax, name='add_calculate'),
    path('json/', show_json, name='show_json'),
    path('add_calculate_flutter/', add_calculate_flutter, name='add_calculate_flutter'),
]
