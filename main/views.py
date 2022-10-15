from django.shortcuts import render

def show_landing(request):
    return render(request,"main.html")

