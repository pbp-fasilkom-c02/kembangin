from django.urls import path
from bmicalculator.views import show_bmicalculator, hapus_input, add_calculate_ajax, show_json
app_name = "bmicalculator"
urlpatterns = [
    path('', show_bmicalculator, name="show_bmicalculator"),
    path('hapus/<int:pk>/', hapus_input, name="hapus"),
    path('add/', add_calculate_ajax, name='add_calculate'),
    path('json/', show_json, name='show_json'),
]
