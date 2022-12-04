from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from main.models import User
from user_profile.models import UserProfile, DoctorProfile
# Create your views here.
@csrf_exempt
def login_user(request):
    if (request.method == "POST"):
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                # Redirect to a success page.
                return JsonResponse({
                "status": True,
                "message": "Successfully Logged In!"
                # Insert any extra data if you want to pass data to Flutter
                }, status=200)
            else:
                return JsonResponse({
                "status": False,
                "message": "Failed to Login, Account Disabled."
                }, status=401)

        else:
            return JsonResponse({
            "status": False,
            "message": "Failed to Login, check your email/password."
            }, status=401)

@csrf_exempt
def register_user(request):
    if (request.method == "POST"):
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        repeat_password = request.POST.get("repeat_password")
        if (User.objects.filter(username=username) or User.objects.filter(email=email)):
            return JsonResponse({
                "status": False,
                "message": "Failed to , Account exist!"
                }, status=401)
        elif (password == repeat_password):
            user = User.objects.create_user(username=username, email=email, password=password)
            user_profile = UserProfile.objects.create(user=user)
            if (request.POST.get("doctor_choice") == "yes"):
                user.is_doctor = True
                doctor_profile = DoctorProfile.objects.create(profile = user_profile)
                doctor_profile.save()
            user.save()
            user_profile.save()
            return JsonResponse({
                "status": True,
                "message": "Successfully create account!"
                # Insert any extra data if you want to pass data to Flutter
                }, status=200)
        else:
            return JsonResponse({
            "status": False,
            "message": "Password and repeat password is different!"
            }, status=401)
           
   