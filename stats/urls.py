from django.conf.urls import url
from stats.views import stats

urlpatterns =[
    url(r'^$', stats, name='stats'),
    ]