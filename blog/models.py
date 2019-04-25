from django.db import models

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Posts(models.Model):
    title = models.CharField(max_length= 150)
    author = models.ForeignKey(User, blank= True, null = True)
    text = models.TextField(max_length = 5000)
    created_date = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title