from django.urls import path
from user_profile.views import *

app_name = 'user_profile'

urlpatterns = [
    path('<int:pk>', show_profile, name='show_profile'),
    path("get_user/<int:pk>", get_user, name="get_user"),
    path("change_profile/<int:pk>", change_profile, name="change_profile"),
    path("create_rating/<int:pk>", create_rating, name="create_rating"),
    path("delete_rating/<int:id>", delete_rating, name="delete_rating"),
    path("get_normal_user/<int:pk>", get_normal_user, name="get_normal_user"),
    path("change_bio/<int:pk>", change_bio_flutter, name="change_bio_flutter"),
    path("get_doctor_user/<int:pk>", get_doctor_user, name="get_doctor_user"),
    path("get_rating/<int:pk>", get_rating, name="get_rating"),
    path("handle_rating_flutter/<int:pk>", handle_rating_flutter, name="handle_rating_flutter"),
]