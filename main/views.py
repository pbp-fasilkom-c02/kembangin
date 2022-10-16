from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import messages

def show_landing(request):
    return render(request,"main.html")

def login_user(request):
    if (request.method == "POST"):
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main:show_landing')
        messages.info(request, "Wrong username or password")
    return render(request, "login.html")

def register_user(request):
    if (request.method == "POST"):
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        repeat_password = request.POST.get("repeat_password")
        if (User.objects.filter(username=username, email=email)):
            messages.info(request, "Username or email already taken")
        elif (password == repeat_password):
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            return redirect("main:login")
        else:
            messages.info(request, "Password and repeat password is different")
    return render(request, "register.html")

def logout_user(request):
    logout(request)
    return redirect("main:login")
