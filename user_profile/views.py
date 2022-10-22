from django.shortcuts import render



def show_profile(request):
    current_user = request.user

    context = {
        "user" : current_user,
        "is_doctor" : current_user.is_doctor
    }
    return render(request, "profile.html", context)