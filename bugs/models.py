from django.db import models
from django_issue_tracker import settings
from django.utils import timezone
from django.contrib.auth.models import User
import datetime

priority_choices = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
        ('Urgent', 'Urgent')
        ]
        
development_status = [
        ('To Do', 'To Do'),
        ('Currently Being Investigated', 'Currently Being Investigated'),
        ('In Development', 'In Development'),
        ('In Testing', 'In Testing'),
        ('Issue Resolved', 'Issue Resolved')
        ]
        
bug_tag = [
        ('Bug', 'Bug'),
        ]


class Bugs(models.Model):
    
    """
    A single Bug
    """
    
    title = models.CharField(max_length = 200)
    bug_details = models.TextField()
    published_date = models.DateField(("Date"), default=datetime.date.today)
    tag = models.CharField(max_length=30, choices=bug_tag, default='Bug')
    priority = models.CharField(max_length=6, choices=priority_choices, default='Low')
    users = models.ForeignKey(User, blank=True, null=True, default='User')
    development_status = models.CharField(max_length=50, choices=development_status, default='To Do')
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    def __str__(self):
        return 'Bug: ' + self.title
