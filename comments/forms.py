from django import forms
from comments.models import Comments
from issues.models import Issues
from django.contrib.auth.models import User

class NewCommentForm(forms.ModelForm):
    
    text = forms.CharField(label="Add your own Comment", widget=forms.Textarea)

    class Meta:
        model = Comments
        fields = ['text']