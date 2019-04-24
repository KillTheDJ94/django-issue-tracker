from django.contrib import admin
from .models import Bugs

admin.site.register(Bugs)

class bugs_user(admin.ModelAdmin):
    list_display = ('User', 'Email')
    fieldsets = [
        (None, { 'fields': [('User','Email')] } ),
    ]

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'User', None) is None:
            obj.user= request.user.username
        obj.save()
