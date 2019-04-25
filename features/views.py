from django.shortcuts import render, get_object_or_404, redirect
from .models import Features
from django.utils import timezone
from .forms import FeaturePostForm
from django.contrib import messages

def features(request):
    features = Features.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, "features.html", {'features': features})

def feature_detail(request, pk):
    """
    Create a view that returns a single feature object based on the feature ID(PK)
    and render it to featuredetail.html template, or return 404 if not found
    """
    feature = get_object_or_404(Features, pk=pk)
    feature.save()
    return render(request, 'featuredetail.html', {'feature': feature})
    
def create_or_edit_feature(request, pk=None):
    """
    create a view that allows us to create or edit a post depending on pk being
    none or not
    """
    features = get_object_or_404(Features, pk=pk) if pk else None
    if request.method == "POST":
        form = FeaturePostForm(request.POST, request.FILES, instance=features)
        
        if form.is_valid():
            features = form.save()
            return redirect(feature_detail, features.pk)
    else:
        form = FeaturePostForm(instance=features)

    return render(request, 'featuresform.html', {'form': form})
    
def feature_like(request, pk):
    feature = Features.objects.get(pk=pk)
    feature.likes += 1
    feature.save()
    messages.success(request, "Thank you for liking this feature request.")
    return render(request, 'feature_detail.html', {'feature': feature})
    
def feature_dislike(request, pk):
    feature = Features.objects.get(pk=pk)
    feature.dislikes += 1
    feature.save()
    messages.success(request, "Thank you for reporting that you do not have this feature")
    return render(request, 'featuredetail.html', {'feature': feature})