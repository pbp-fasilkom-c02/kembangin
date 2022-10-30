from django.db import models

# Create your models here.
class Rekomendasi(models.Model):
    gambar = models.URLField()
    nama_barang = models.CharField(max_length=50)
    harga_barang = models.TextField()
    deskripsi = models.TextField()
    url = models.URLField()

