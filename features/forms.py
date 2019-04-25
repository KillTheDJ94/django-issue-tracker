from django import forms
from datetimepicker.widgets import DateTimePicker
from .models import Features
from django_issue_tracker import settings

class FeaturePostForm(forms.ModelForm):
    class Meta:
        
        model = Features
        fields = ('title', 'feature_details', 'tag', 'published_date', 'priority', 'users')
        
    