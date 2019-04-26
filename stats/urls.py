from django.conf.urls import url
from stats.views import all_charts

urlpatterns =[
    url(r'^$', all_charts, name='all_charts'),
    ]