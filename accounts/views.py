from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from accounts.forms import UserLoginForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from bugs.models import Bugs
from features.models import Features
from django.contrib.auth.models import User
from django.db.models import Q


def index(request):
    """Return the index.html file"""
    return render(request,  'index.html')
    
    
def login(request):
    """Return a login page"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                    password=request.POST['password'])
            messages.success(request, "You have successfully logged in!", extra_tags='alert')

            if user:
                auth.login(user=user, request=request)
                return redirect(reverse('index'))
            else:
                login_form.add_error(None, "Your username or password is incorrect")
    else:
        login_form = UserLoginForm()
    return render(request, 'login.html', {'login_form': login_form})
    
    
@login_required
def logout(request):
    """Log the user out"""
    auth.logout(request)
    messages.success(request, "You have successfully been logged out")
    return redirect(reverse('index'))
    
    
def registration(request):
    """Render the registration page"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)

        if registration_form.is_valid():
            registration_form.save()

            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully registered", extra_tags='alert')
                return redirect(reverse('index'))
            else:
                messages.error(request, "Unable to register your account at this time", extra_tags='alert')
    else:
        registration_form = UserRegistrationForm()
    return render(request, 'index.html', {
        "registration_form": registration_form})
        
def user_bug_profile(request):
    """The user's profile page"""
    user = User.objects.get(email=request.user.email)
    bugs = Bugs.objects.filter(users = user).order_by('-published_date')
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
    return render(request, 'bugprofile.html', {"user": user, "bugs": bugs})
    
def user_feature_profile(request):
    user = User.objects.get(email=request.user.email)
    features = Features.objects.filter(users = user).order_by('-published_date')
    paginator = Paginator(features, 10)
    query = request.GET.get("q")
    if query:
        features = features.filter(
            Q(title__icontains=query)|
            Q(tag__icontains=query)|
            Q(priority__icontains=query)|
            Q(development_status__icontains=query)|
            Q(id__icontains=query)
            ).distinct()

    page = request.GET.get('page')
    try:
        features = paginator.page(page)
    except PageNotAnInteger:
        features = paginator.page(1)
    except EmptyPage:
        features = paginator.page(paginator.num_pages)
    return render(request, 'featureprofile.html', {"user": user, "features": features})
