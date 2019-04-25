from django import forms
from blog.models import Posts


class NewPostForm(forms.ModelForm):

    class Meta:
        model = Posts
        fields = ('title', 'text')