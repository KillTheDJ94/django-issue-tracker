from django.shortcuts import render
from .models import Bugs

def bugs(request):
    """ create a view for list of issue prior to now
    and render to bugs.html
    """
    bugs = Bugs.objects.filter(tag='Bug').order_by('-published_date')
    return render(request, "bugs.html", {'bugs': bugs})
