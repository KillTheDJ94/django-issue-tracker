from django.shortcuts import render, get_object_or_404, redirect
from .models import Bugs
from .forms import BugReportForm
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def bugs(request):
    """ create a view for list of Bugs prior to now
    and render to bugs.html
    """
    bugs = Bugs.objects.filter(tag='Bug').order_by('-published_date')
    query = request.GET.get("q")
    if query:
        bugs = bugs.filter(
            Q(title__icontains=query)|
            Q(tag__icontains=query)|
            Q(priority__icontains=query)|
            Q(development_status__icontains=query)|
            Q(id__icontains=query)
            ).distinct()
    paginator = Paginator(bugs, 10)

    page = request.GET.get('page')
    try:
        bugs = paginator.page(page)
    except PageNotAnInteger:
        bugs = paginator.page(1)
    except EmptyPage:
        bugs = paginator.page(paginator.num_pages)
    return render(request, "bugs.html", {'bugs': bugs})

def bug_detail(request, pk):
    """
    Create a view that returns a single Bug object based on the Bugs ID(PK)
    and render it to bugdetail.html template, or return 404 if not found
    """
    bugs = get_object_or_404(Bugs, pk=pk)
    bugs.save()
    
    return render(request, 'bugdetail.html', {'bugs': bugs})
    
def create_or_edit_bug(request, pk=None):
    """
    create a view that allows us to create or edit a post depending on pk being
    none or not
    """
    bugs = get_object_or_404(Bugs, pk=pk) if pk else None
    if request.method == "POST":
        form = BugReportForm(request.POST, request.FILES, instance=bugs)
        
        if form.is_valid():
            
            bugs = form.save()
            return redirect(bug_detail, bugs.pk)
    else:
        form = BugReportForm(instance=bugs)

    return render(request, 'bugform.html', {'form': form})
    
def bug_like(request, pk):
    bugs = Bugs.objects.get(pk=pk)
    bugs.likes += 1
    bugs.save()
    messages.success(request, "Thank you for reporting that you have this Bugs.")
    return render(request, 'bugdetail.html', {'bugs': bugs})
    
def bug_dislike(request, pk):
    bugs = Bugs.objects.get(pk=pk)
    bugs.dislikes += 1
    bugs.save()
    messages.success(request, "Thank you for reporting that you do not have this Bugs")
    return render(request, 'bugdetail.html', {'bugs': bugs})
    
def bug_status_to_do(request):
    bugs = Bugs.objects.filter(development_status= 'To Do', tag='Bug')
    paginator = Paginator(bugs, 10)

    page = request.GET.get('page')
    try:
        bugs = paginator.page(page)
    except PageNotAnInteger:
        bugs = paginator.page(1)
    except EmptyPage:
        bugs = paginator.page(paginator.num_pages)
    return render(request, "bug_status_to_do.html", {'bugs': bugs})
    
def bug_status_investigated(request):
    bugs = Bugs.objects.filter(development_status= 'Currently Being Investigated', tag='Bug')
    query = request.GET.get("q")
    if query:
        bugs = bugs.filter(
            Q(title__icontains=query)|
            Q(tag__icontains=query)|
            Q(priority__icontains=query)|
            Q(development_status__icontains=query)|
            Q(id__icontains=query)
            ).distinct()
    paginator = Paginator(bugs, 10)

    page = request.GET.get('page')
    try:
        bugs = paginator.page(page)
    except PageNotAnInteger:
        bugs = paginator.page(1)
    except EmptyPage:
        bugs = paginator.page(paginator.num_pages)
    return render(request, "bug_status_investigated.html", {'bugs': bugs})
    
def bug_status_in_development(request):
    bugs = Bugs.objects.filter(development_status= 'In Development', tag='Bug')
    query = request.GET.get("q")
    if query:
        bugs = bugs.filter(
            Q(title__icontains=query)|
            Q(tag__icontains=query)|
            Q(priority__icontains=query)|
            Q(development_status__icontains=query)|
            Q(id__icontains=query)
            ).distinct()
    paginator = Paginator(bugs, 10) 

    page = request.GET.get('page')
    try:
        bugs = paginator.page(page)
    except PageNotAnInteger:
        bugs = paginator.page(1)
    except EmptyPage:
        bugs = paginator.page(paginator.num_pages)
    return render(request, "bug_status_in_development.html", {'bugs': bugs})  
    
def bug_status_in_testing(request):
    bugs = Bugs.objects.filter(development_status= 'In Testing', tag='Bug')
    query = request.GET.get("q")
    if query:
        bugs = bugs.filter(
            Q(title__icontains=query)|
            Q(tag__icontains=query)|
            Q(priority__icontains=query)|
            Q(development_status__icontains=query)|
            Q(id__icontains=query)
            ).distinct()
    paginator = Paginator(bugs, 10)

    page = request.GET.get('page')
    try:
        bugs = paginator.page(page)
    except PageNotAnInteger:
        bugs = paginator.page(1)
    except EmptyPage:
        bugs = paginator.page(paginator.num_pages)
    return render(request, "bug_status_in_testing.html", {'bugs': bugs})