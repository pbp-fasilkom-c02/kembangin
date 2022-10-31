from django.urls import path
from bmicalculator.views import show_bmicalculator, add_calculate_ajax, show_json, delete_task
app_name = "bmicalculator"
urlpatterns = [
    path('', show_bmicalculator, name="show_bmicalculator"),
    path('delete/<int:pk>/', delete_task, name="delete"),
    path('add/', add_calculate_ajax, name='add_calculate'),
    path('json/', show_json, name='show_json'),
]
