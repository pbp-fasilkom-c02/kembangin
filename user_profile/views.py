from django.shortcuts import render
from django.contrib.auth.models import User
from main.models import Doctor

def show_profile(request):
    current_user = request.user
    if (Doctor.objects.filter(user=current_user)):
        is_doctor = True
    else:
        is_doctor = False
    context = {
        "user" : current_user,
        "is_doctor" : is_doctor
    }
    return render(request, "profile.html", context)