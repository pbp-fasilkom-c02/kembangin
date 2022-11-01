from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import get_object_or_404
from .forms import FormRekomendasi
from .models import Rekomendasi
import datetime
import json
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from user_profile.views import show_profile

# Create your views here.
# @login_required(login_url='login/')
def show_rekomendasi(request):
    list_rekomendasi = Rekomendasi.objects.filter()
    context = {
        'list_rekomendasi': list_rekomendasi,
        'user': request.user,
    }
    return render(request, "rekomendasi.html", context)

@login_required(login_url='login/')
def add_rekomendasi(request):
    if request.method == "POST":
        data = json.loads(request.POST['data'])

        new_rekomendasi = Rekomendasi(nama_barang=data["nama_barang"], harga_barang=data["harga_barang"], deskripsi=data["deskripsi"], url=data["url"], gambar=data["gambar"])
        new_rekomendasi.save()

        return HttpResponse(serializers.serialize("json", [new_rekomendasi]), content_type="application/json")

    return HttpResponse()

# @login_required(login_url='login/')
def show_json(request):
    rekomendasi = Rekomendasi.objects.filter()
    data = serializers.serialize('json', rekomendasi)

    return HttpResponse(data, content_type='application/json')
