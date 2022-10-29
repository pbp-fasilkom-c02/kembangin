from django.db import models
from main.models import User
from django.utils import timezone

class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    name = models.CharField(max_length=255)
    age = models.CharField(max_length=15, default="0 Tahun")
    height = models.CharField(max_length=15, default="0cm")
    weight = models.CharField(max_length=15, default="0kg")
    eat = models.CharField(max_length=15, choices=[("Tidak Baik", "Tidak baik"), ("Kurang Baik", "Kurang baik"), ("Cukup Baik", "Cukup baik"), ("Sangat Baik", "Sangat baik")])
    drink = models.CharField(max_length=15, choices=[("Tidak Baik", "Tidak baik"), ("Kurang Baik", "Kurang baik"), ("Cukup Baik", "Cukup baik"), ("Sangat Baik", "Sangat baik")])
    progress = models.TextField(default="-")