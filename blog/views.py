from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Posts
from .forms import NewPostForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.db.models import Q


def post_list(request):
    posts = Posts.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')
    return render(request, 'postlist.html', {"posts" : posts})

def post_detail(request, pk):
    posts = get_object_or_404(Posts, pk=pk)
    return render(request, 'postdetail.html', {'posts': posts})
    
def create_or_edit_post(request, pk=None):
    """
    create a view that allows us to create or edit a post depending on pk being
    none or not
    """
    posts = get_object_or_404(Posts, pk=pk) if pk else None
    if request.method == "POST":
        form = NewPostForm(request.POST, request.FILES, instance=posts)
        
        if form.is_valid():
            
            posts = form.save()
            return redirect(post_detail, posts.pk)
    else:
        form = NewPostForm(instance=posts)

    return render(request, 'newpost.html', {'form': form})
    
def post_like(request, pk):
    posts = Posts.objects.get(pk=pk)
    posts.likes += 1
    posts.save()
    messages.success(request, "Thank you liking this blog post")
    return render(request, 'postdetail.html', {'posts': posts})
    
def post_dislike(request, pk):
    posts = Posts.objects.get(pk=pk)
    posts.dislikes += 1
    posts.save()
    messages.success(request, "Thank you for feedback, please leave a comment so that we can imporve")
    return render(request, 'postdetail.html', {'posts': posts})