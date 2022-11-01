from django.db import models
from django.conf import settings

# Create your models here.
class Rekomendasi(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    gambar = models.URLField()
    nama_barang = models.CharField(max_length=50)
    harga_barang = models.TextField()
    deskripsi = models.TextField()
    url = models.URLField()

