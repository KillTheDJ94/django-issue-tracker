from django.conf.urls import url
from .views import bugs, bug_detail, create_or_edit_bug, bug_like, bug_dislike, bug_status_to_do, bug_status_investigated, bug_status_in_development, bug_status_in_testing

urlpatterns = [
    url(r'^bugs/$', bugs, name='bugs'),
    url(r'^(?P<pk>\d+)/$', bug_detail, name="bug_detail"),
    url(r'^new/$', create_or_edit_bug, name="new_bug"),
    url(r'^(?P<pk>\d+)/edit/$', create_or_edit_bug, name= "edit_bug"),
    url(r'^(?P<pk>\d+)/likes/$', bug_like, name='bug_like'),
    url(r'^(?P<pk>\d+)/dislikes/$', bug_dislike, name='bug_dislike'),
    url(r'^to_do/$', bug_status_to_do, name='bug_status_to_do'),
    url(r'^investigated/$', bug_status_investigated, name='bug_status_investigated'),
    url(r'^in_development/$', bug_status_in_development, name='bug_status_in_development'),
    url(r'^in_testing/$', bug_status_in_testing, name='bug_status_in_testing'),
    url(r'^(?P<pk>\d+)/delete/$', delete_issue, name="delete_issue"),
    ]