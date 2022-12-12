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
from django.http import JsonResponse

# Create your views here.
# @login_required(login_url='/login')
def show_rekomendasi(request):
    list_rekomendasi = Rekomendasi.objects.filter()
    context = {
        'list_rekomendasi': list_rekomendasi,
        'user': request.user,
    }
    return render(request, "rekomendasi.html", context)


# @login_required(login_url='/login')
@csrf_exempt
def add_rekomendasi(request):
    if request.method == "POST":
        print(request.POST['nama_barang'])

        data = request.POST

        # data = json.loads(request.POST['data'])
        # print(data)
        # print(data['nama_barang'])
        

        new_rekomendasi = Rekomendasi(nama_barang=data["nama_barang"], harga_barang=data["harga_barang"], deskripsi=data["deskripsi"], url=data["url"], gambar=data["gambar"])
        new_rekomendasi.save()

        return JsonResponse({
        "status": True,
        "message": "Berhasil menambahkan rekomendasi"
        # Insert any extra data if you want to pass data to Flutter
        }, status=200)

    return JsonResponse({
        "status": False,
        "message": "Cek kembali input anda"
        # Insert any extra data if you want to pass data to Flutter
        }, status=401)

# @login_required(login_url='/login')
@csrf_exempt
def show_json(request):
    # rekomendasi = Rekomendasi.objects.filter()
    rekomendasi = Rekomendasi.objects.all()
    data = serializers.serialize('json', rekomendasi)

    # return JsonResponse({
    #     "status": True,
    #     "message": "Data berhasil diambil",
        
    # }, status=200)
    return HttpResponse(data, content_type='application/json')