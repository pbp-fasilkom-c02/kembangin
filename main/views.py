from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from .models import User
from user_profile.models import UserProfile, DoctorProfile
from django.contrib import messages
from artikel.models import Artikel
import operator
from django.views.decorators.csrf import csrf_exempt

def show_landing(request):
    artikel = {}
    top_3 = []
    data = Artikel.objects.all()

    if (len(data) != 0):
        for i in range(0, len(data)):
            artikel[data[i]] = data[i].upvote
        
        sorted_d = dict( sorted(artikel.items(), key=operator.itemgetter(1),reverse=True))
        
        i = 1
        if (len(sorted_d) < 3):
            for key, value in sorted_d.items():
                top_3.append(key)
                     
        else:
            for key, value in sorted_d.items():
                if (i == 4):
                    break
                else:
                    top_3.append(key)
                    i += 1
                    
    context = {
        "data" : top_3
    }

    return render(request,"main.html", context)

def login_user(request):
    if (request.method == "POST"):
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main:show_landing')
        messages.info(request, "Wrong username or password!")
    return render(request, "login.html")

@csrf_exempt
def register_user(request):
    if (request.method == "POST"):
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        repeat_password = request.POST.get("repeat_password")
        if (User.objects.filter(username=username) or User.objects.filter(email=email)):
            messages.info(request, "Username or email already taken!")
        elif (password == repeat_password):
            user = User.objects.create_user(username=username, email=email, password=password)
            user_profile = UserProfile.objects.create(user=user)
            if (request.POST.get("doctor_choice") == "yes"):
                user.is_doctor = True
                doctor_profile = DoctorProfile.objects.create(profile = user_profile)
                doctor_profile.save()
            user.save()
            user_profile.save()
            return redirect("main:login")
        else:
            messages.info(request, "Password and repeat password is different!")
    return render(request, "register.html")

def logout_user(request):
    logout(request)
    return redirect("main:login")
