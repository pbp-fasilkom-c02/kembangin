from django.urls import path
from main.views import  show_landing, register_user, login_user, logout_user

app_name = 'main'

urlpatterns = [
    path('', show_landing, name='show_landing'),
    path('login', login_user, name='login' ),
    path('register', register_user, name='register'),
    path('logout', logout_user, name='logout')
]