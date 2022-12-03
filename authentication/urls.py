from django.urls import path
from authentication.views import login_user

app_name = 'main'

urlpatterns = [
    path('login', login_user, name='login'),
]