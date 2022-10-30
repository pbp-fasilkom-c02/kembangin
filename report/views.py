from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest
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
        form = ReportForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            height = form.cleaned_data['height']
            weight = form.cleaned_data['weight']
            eat = form.cleaned_data['eat']
            drink = form.cleaned_data['drink']
            progress = form.cleaned_data['progress']
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
        return HttpResponseBadRequest()

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