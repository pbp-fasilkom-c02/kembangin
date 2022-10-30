from dataclasses import fields
from django.forms import ModelForm
from .models import Rekomendasi

class FormRekomendasi(ModelForm):
    class Meta:
        model = Rekomendasi
        fields = ['nama_barang', 'harga_barang', 'deskripsi', 'url', 'gambar']