from datetime import datetime
from multiprocessing import context
from urllib import request
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from bmicalculator.models import BmiCalculator
from bmicalculator.forms import BmiCalculatorForm
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.urls import reverse
import json
from django.views.decorators.csrf import csrf_exempt



# Create your views here.
# @login_required(login_url='/login/')
def show_bmicalculator(request):
    form = BmiCalculatorForm()
    return render(request, "bmicalculator.html",{'form' : form, 'nama' : request.user})
   

# @login_required(login_url='/login/')
def show_json(request):
    # bmicalculator_data = BmiCalculator.objects.filter(user=request.user) 
    # return HttpResponse(serializers.serialize("json", bmicalculator_data), content_type='application/json')
    # handle for anonymous user
    if request.user.is_authenticated:   # jika user sudah login
        bmicalculator_data = BmiCalculator.objects.filter(user=request.user) 
        return HttpResponse(serializers.serialize("json", bmicalculator_data), content_type='application/json')
    else:
        bmicalculator_data = BmiCalculator.objects.filter(user__isnull=True) 

        return HttpResponse(serializers.serialize("json", bmicalculator_data), content_type='application/json')



def delete_task(request, pk):
    if request.user.is_authenticated:
        data = BmiCalculator.objects.get(pk=pk)
        data.delete()
        response = HttpResponseRedirect(reverse('bmicalculator:show_bmicalculator'))
        return response
    else:
        data = BmiCalculator.objects.filter(user__isnull=True, pk=pk)
        data.delete()
        response = HttpResponseRedirect(reverse('bmicalculator:show_bmicalculator'))
        return response


# @login_required(login_url='/login/')
def add_calculate_ajax(request):
    if request.method == "POST":
        context = {}
        weight = request.POST.get('weight')
        height = request.POST.get('height')
        # bmi = float(weight) / ((float(height))/100 * (float(height))/100)
        # hitung bmi dan convert ke integer
        bmi = int(int(weight) / ((int(height))/100 * (int(height))/100))
        user = request.user
        
        # handle for anonymous user
        if request.user.is_authenticated:
            data = BmiCalculator.objects.create(user=user, weight=weight, height=height, bmi=bmi, date=datetime.today(), author=request.user.username)
            data.save()
            return JsonResponse({
                "pk" : data.pk,
                "fields" : {
                    "weight" : data.weight,
                    "height" : data.height,
                    "bmi" : data.bmi,
                    "date" : data.date,
                    "status" : data.status,
                    "author" : data.author,
                },
            },
            status=200
            )
        else:
            data = BmiCalculator.objects.create(weight=weight, height=height, bmi=bmi, date=datetime.today(), author="Anonymous")
            return JsonResponse({
            
                "pk" : data.pk,
                "fields" : {
                    "weight" : data.weight,
                    "height" : data.height,
                    "bmi" : data.bmi,
                    "date" : data.date,
                    "status" : data.status,
                    "author" : data.author,
                },
            },
            status=200
            )
       
@csrf_exempt
def add_calculate_flutter(request):
    if request.method == "POST":
        newCalculate = json.loads(request.body)
        weight = newCalculate['weight']
        height = newCalculate['height']
        bmi = int(int(weight) / ((int(height))/100 * (int(height))/100))
        bmi = newCalculate['bmi']
        
        user = user.objects.get(pk=newCalculate['user'])
        
        # handle for anonymous user
        if request.user.is_authenticated:
            newCalculate = BmiCalculator(user=user, weight=weight, height=height, bmi=bmi, date=datetime.today(), author=request.user.username)
            newCalculate.save()
            return JsonResponse({
                "pk" : newCalculate.pk,
                "fields" : {
                    "weight" : newCalculate.weight,
                    "height" : newCalculate.height,
                    "bmi" : newCalculate.bmi,
                    "date" : newCalculate.date,
                    "status" : newCalculate.status,
                    "author" : newCalculate.author,
                },
            },
            status=200
            )
        else:
            newCalculate = BmiCalculator(weight=weight, height=height, bmi=bmi, date=datetime.today(), author="Anonymous")
            newCalculate.save()
            return JsonResponse({
                "pk" : newCalculate.pk,
                "fields" : {
                    "weight" : newCalculate.weight,
                    "height" : newCalculate.height,
                    "bmi" : newCalculate.bmi,
                    "date" : newCalculate.date,
                    "status" : newCalculate.status,
                    "author" : newCalculate.author,
                },
            },
            status=200
            )





            
        



