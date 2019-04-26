from django.db import models
from bugs.models import Bugs
from features.models import Features
from django.contrib.auth.models import User
from blog.models import Posts

class Comments(models.Model):
    users = models.ForeignKey(User, null=True, blank=True, default=User)
    bugs = models.ForeignKey(Bugs, null=True, blank=True)
    feature = models.ForeignKey(Features, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    text = models.TextField(blank=False, max_length=200)
    def __str__(self):
        return 'Comment: ' + self.text