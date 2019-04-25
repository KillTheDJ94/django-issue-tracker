from blog.views import post_list, post_detail, create_or_edit_post, post_like, post_dislike
from django.conf.urls import url

urlpatterns = [
    url(r'^$', post_list, name='post_list'),
    url(r'^(?P<pk>\d+)/$', post_detail, name='post_detail'),
    url(r'^new_blog_post/$', create_or_edit_post, name="new_post"),
    url(r'^(?P<pk>\d+)/edit$', create_or_edit_post, name='edit_post'),
    url(r'^(?P<pk>\d+)/like$', post_like, name='post_like'),
    url(r'^(?P<pk>\d+)/dislike$', post_dislike, name='post_dislike'),
    ]