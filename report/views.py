from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404
from report.models import Report
from django.core import serializers
import datetime

@login_required(login_url='/login/')
def show_reports(request):
    data_report = Report.objects.filter(user=request.user).all()

    context = {
    'reports': data_report,
    }
    return render(request, "report-progress.html", context)

def show_json(request):
    data = Report.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

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