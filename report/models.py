from django.db import models
from main.models import User
from django.utils import timezone

class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    name = models.CharField(max_length=255)
    age = models.CharField(max_length=15)
    height = models.CharField(max_length=15)
    weight = models.CharField(max_length=15)
    eat = models.CharField(max_length=15, choices=[("Tidak Baik", "Tidak baik"), ("Kurang Baik", "Kurang baik"), ("Cukup Baik", "Cukup baik"), ("Sangat Baik", "Sangat baik")])
    drink = models.CharField(max_length=15, choices=[("Tidak Baik", "Tidak baik"), ("Kurang Baik", "Kurang baik"), ("Cukup Baik", "Cukup baik"), ("Sangat Baik", "Sangat baik")])
    progress = models.TextField()