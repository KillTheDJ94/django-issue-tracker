from django import forms
from datetimepicker.widgets import DateTimePicker
from .models import Bugs
from issue_tracker_auth import settings

class BugReportForm(forms.ModelForm):
    class Meta:
        
        model = Bugs
        fields = ('title', 'issue_details', 'tag', 'published_date', 'users', 'priority')
        
    