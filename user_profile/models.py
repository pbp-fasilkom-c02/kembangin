from django.db import models
from main.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    bio = models.TextField(default="")
    post_amount = models.IntegerField(default=0)
    upvote_amount = models.IntegerField(default=0)

class DoctorProfile(models.Model):
    profile = models.OneToOneField(UserProfile, on_delete = models.CASCADE)
    comment_amount = models.IntegerField(default=0)
    rating_average = models.FloatField(default=0)

class Rating(models.Model):
    doctor = models.ForeignKey(DoctorProfile, on_delete = models.CASCADE)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    rating = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(max_length=150)
