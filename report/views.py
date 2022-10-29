from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from report.forms import ReportForm
from report.models import Report
from django.core import serializers
import datetime

def show_reports(request):
    form = ReportForm()
    return render(request, "report-progress.html", {'form':form})

@login_required(login_url='/login/')
def show_json(request):
    data = Report.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@login_required(login_url='/login/')
@csrf_exempt
def add_report(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        height = request.POST.get('height')
        weight = request.POST.get('weight')
        eat = request.POST.get('eat')
        drink = request.POST.get('drink')
        progress = request.POST.get('progress')
        report = Report.objects.create(name=name, age=age, height=height, weight=weight, eat=eat, drink=drink, progress=progress, date=datetime.date.today(), user=request.user)
        reports = {
            'pk':report.pk,
            'fields':{
                'date':report.date,
                'name':report.name,
                'age':report.age,
                'height':report.height,
                'weight':report.weight,
                'eat':report.eat,
                'drink':report.drink,
                'progress':report.progress,
            }
        }
        return JsonResponse(reports)

@login_required(login_url='/login/')
def delete_report(request, id):
    if request.method == 'DELETE':
        report = Report.objects.get(pk=id)
        report.delete()
        reports = {
            'pk':report.pk,
            'fields':{
                'date':report.date,
                'name':report.name,
                'age':report.age,
                'height':report.height,
                'weight':report.weight,
                'eat':report.eat,
                'drink':report.drink,
                'progress':report.progress,
            }
        }
        return JsonResponse(reports)