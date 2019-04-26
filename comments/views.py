from django.shortcuts import render
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from bugs.models import Bugs
from features.models import Features
from comments.forms import NewCommentForm
from .models import Comments


def new_bug_comment(request, pk):
    if request.method == "POST":
        form = NewCommentForm(request.POST)
        if form.is_valid():
            add_comment = form.save(commit = False)
            add_comment.users = request.user
            add_comment.bugs = get_object_or_404(Bugs, pk = pk)
            add_comment.save()
            messages.success(request, "Your comment has been added.")
            bugs = Bugs.objects.get(pk=pk)
            comments = Comments.objects.filter(bugs = bugs)
            return render(request, 'issuedetail.html', {"bugs": bugs, "comments":comments, "form":form})
    return render(request, 'bugs.html')

def new_feature_comment(request, pk):
    if request.method == "POST":
        form = NewCommentForm(request.POST)
        if form.is_valid():
            add_comment = form.save(commit = False)
            add_comment.users = request.user
            add_comment.feature = get_object_or_404(Features, pk = pk)
            add_comment.save()
            messages.success(request, "Your comment has been added.")
            feature = Features.objects.get(pk=pk)
            comments = Comments.objects.filter(feature = feature)
            return render(request, 'feature_detail.html', {"feature": feature, "comments":comments, "form":form})
    return render(request, 'features.html')
    