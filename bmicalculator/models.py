from django.db import models
from main.models import User
# Create your models here.
class BmiCalculator(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date = models.DateField(auto_now_add=True)
    weight = models.FloatField()
    height = models.FloatField()
    bmi = models.FloatField(default=0)
    status = models.BooleanField(default=False)
   
    
