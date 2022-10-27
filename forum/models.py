from email.policy import default
from django.db import models
from main.models import User


# User can create many forums, forum can have many reply

class Forum(models.Model):
    question = models.CharField(max_length=250)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    upvote = models.IntegerField(default=0)
    downvote = models.IntegerField(default=0)

class ForumReply(models.Model):
    comment = models.CharField(max_length=100)
    forum = models.ForeignKey(Forum,on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)




