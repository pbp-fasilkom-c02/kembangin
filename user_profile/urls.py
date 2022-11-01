from django.urls import path
from user_profile.views import show_profile, get_user, change_profile, create_rating, delete_rating

app_name = 'user_profile'

urlpatterns = [
    path('<int:pk>', show_profile, name='show_profile'),
    path("get_user/<int:pk>", get_user, name="get_user"),
    path("change_profile/<int:pk>", change_profile, name="change_profile"),
    path("create_rating/<int:pk>", create_rating, name="create_rating"),
    path("delete_rating/<int:id>", delete_rating, name="delete_rating"),
]