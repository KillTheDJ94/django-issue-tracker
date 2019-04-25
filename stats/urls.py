from django.conf.urls import url
from stats.views import stats

urlpatters =[
    url(r'^/$', stats, name='stats'),
    ]