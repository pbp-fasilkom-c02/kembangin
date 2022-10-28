from django.urls import path
from .views import show_rekomendasi, add_rekomendasi, show_json
app_name = 'rekomendasi'

urlpatterns = [
    path('', show_rekomendasi, name='show_rekomendasi'),
    path('add/', add_rekomendasi, name='add_rekomendasi'),
    path('json/', show_json, name='show_json'),
    # path('delete/<str:id>/', delete_rekomendasi, name='delete_rekomendasi'),
]