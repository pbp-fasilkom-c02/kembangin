from email.policy import default
from django.db import models
from main.models import User

class Artikel(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    upvote = models.IntegerField(default=0)
    downvote = models.IntegerField(default=0)
    photo = models.CharField(max_length=300)

class Comment(models.Model):
    comment = models.TextField()
    artikel = models.ForeignKey(Artikel, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)