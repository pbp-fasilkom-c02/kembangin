from django.db import models
from main.models import User
# Create your models here.
class BmiCalculator(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date = models.DateField(auto_now_add=True)
    weight = models.IntegerField()
    height = models.IntegerField()
    bmi = models.IntegerField(default=0)
    author = models.CharField(max_length=100, default="Anonymous")
   
    
