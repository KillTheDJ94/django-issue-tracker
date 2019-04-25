from django import forms
from datetimepicker.widgets import DateTimePicker
from .models import Bugs
from django_issue_tracker import settings

class BugReportForm(forms.ModelForm):
    class Meta:
        
        model = Bugs
        fields = ('title', 'bug_details', 'tag', 'published_date', 'users', 'priority')
        
    